import sys
import fire
import util
import signal
from sr import get_witnesses

from tqdm import tqdm
from db import Store
from trongrid import ApiClient, APIError



def parse_one_block(client, store, number):
    # arleady parsed
    if store.get_block_time(number) != 0:
        return
    block = client.get_block_by_number(number)
    trxs = []
    if block.has_key('transactions'):
        trxs = block['transactions']
    time_stamp = 0
    if number != 0:
        time_stamp = block['block_header']['raw_data']["timestamp"]
    oft_trxs = []
    for trx in trxs:
        if trx['ret'][0]['contractRet'] == 'OUT_OF_TIME':
            oft_trxs.append(trx)

    witness_address = block['block_header']['raw_data']["witness_address"]

    store.try_add_sr(witness_address)

    trxs_cnt = len(oft_trxs)
    if trxs_cnt > 0:
        store.add_oft_cnts(witness_address, trxs_cnt)
        store.update_sr_block_oft_trxs(witness_address, number, oft_trxs)
    store.update_sr_block_oft_cnts(witness_address, number, trxs_cnt)
    store.add_sr_blocks_cnts(witness_address, 1)
    store.update_block_time(number, time_stamp)


def parse(start = -1, end=10000000000):
    if start < -1:
        print fire.core.formatting.Error('err: start parameter must be greater than 0.')
        return
    if end < 0:
        print fire.core.formatting.Error('err: end parameter must be greater than 0.')
        return
    if start >= end:
        print fire.core.formatting.Error('err: the value of the start parameter must be less than the end parameter.')
        return

    store = Store()
    client = ApiClient()
    now = client.get_now_blocknumber()

    db_start = store.start_point()
    db_end = store.end_point()

    if start == -1:
        start = db_end + 1
    if end == 10000000000:
        end = now

    new_db_start = db_start
    new_db_end = db_end

    process_start = 0
    process_end = 0

    if db_start == -1:
            process_start = new_db_start = start
            process_end = new_db_end = end
    else:
        if start > db_end + 1:
            print fire.core.formatting.Error('err: the start parameter cannot be greater than %d' % db_end)
            return 
        else :
            process_start = start
            if start < db_start:
                new_db_start = start

        if end < db_start - 1:
            print fire.core.formatting.Error('err: the end parameter cannot be less than %d' % db_start)
            return
        else:
            process_end = end
            if end >= db_end:
                new_db_end = end

    size = end - start + 1
    util.progress_msg('parsing Blocks from trongrid, from %d to %d' %(process_start, process_end))
    with tqdm(total=size, unit='blocks') as pbar:
        for i in range(start, end+1):
            parse_one_block(client, store, i)
            pbar.update(1)
        store.update_start_point(new_db_start)
        store.update_end_point(new_db_end)
        pbar.close()

def status():
    store = Store()
    client = ApiClient()
    start = store.start_point()
    end = store.end_point()
    srs = store.get_srs()
    witnesses = get_witnesses(client)


    print ''
    templ = '%-11s'
    print  fire.core.formatting.Bold(templ % 'Start Block') + ': ' + str(start)
    print  fire.core.formatting.Bold(templ % '  End Block') + ': ' + str(end)
    print ''
    templ = '%-45s %-40s %-30s %-10s'
    print fire.core.formatting.Bold(
        templ % ('SR Address', 'SR NAME','OutOfTime Txs', 'Total Blocks')
    )
    for sr in srs:
        oft_cnt = store.get_sr_oft_cnts(sr)
        if witnesses.has_key(sr):
            sr_name = witnesses[sr]['url']
        else:
            sr_name = '-'
        block_cnt = store.get_sr_blocks_cnts(sr)
        print(templ %(sr, sr_name, oft_cnt, block_cnt))


def query(recent_days = 0, min_block = 0, max_block = 0):
    store = Store()
    srs = store.get_srs()
    srs_cnts_map = {}
    def add_srs_cnts(sr, counter):
        if not srs_cnts_map.has_key(sr):
            srs_cnts_map[sr] = 0
        srs_cnts_map[sr] += counter
    def traversing_blocks(start, end):
        for block_number in range(start, end+1):
            for sr in srs:
                cnts = store.get_sr_block_oft_cnts(sr, block_number)
                add_srs_cnts(sr, cnts)

    db_start = store.start_point()
    db_end = store.end_point()
    db_min_timestamp = 0
    db_max_timestamp = 0
    if db_start != -1:
        db_min_timestamp = store.get_block_time(db_start)
    if db_end != -1:
        db_max_timestamp = store.get_block_time(db_end)
    client = ApiClient()
    witnesses = get_witnesses(client)


    process_start = db_start
    process_end = db_end
    if recent_days == 0 and min_block == 0 and max_block == 0:
        pass
    elif recent_days != 0:
        sec = recent_days * 24 * 60 * 60
        blocks = int(sec / 3)
        start = db_end - blocks
        if start < db_start:
            print fire.core.formatting.Error('specified blocks span is too large and needs '
                                             'to be parsed from block %d and currently %d' % (start, db_start))
            return
        process_start = start
        process_end = db_end

    elif recent_days == 0 and  min_block != 0 or max_block != 0:
        if min_block >= max_block:
            print fire.core.formatting.Error('min_block must be less than max_block')
            return

        if min_block < db_start or max_block > db_end:
            print fire.core.formatting.Error('The specified time range is incorrect and '
                                             'must be between %d and %d' %(db_start, db_end))
            return
        process_start = min_block
        process_end = max_block

    else:
        print fire.core.formatting.Error('min_block and max_block specify errors')
        return


    traversing_blocks(process_start, process_end)

    start_timestamp = store.get_block_time(process_start)
    end_timestamp = store.get_block_time(process_end)

    templ = '%-45s %-40s %-15s'
    util.status_msg_div()
    util.status_msg('     Time Range:', '%s ~ %s' % (util.timestamp_to_strftime(start_timestamp), util.timestamp_to_strftime(end_timestamp)))
    util.status_msg('TimeStamp Range:', '%d ~ %d' % (start_timestamp, end_timestamp))
    util.status_msg('    Block Range:', '%d ~ %d' % (process_start, process_end))
    util.status_msg_div()
    print fire.core.formatting.Bold(
        templ % ('SR Address', 'SR NAME','OutOfTime Txs')
    )
    for sr in srs:
        if witnesses.has_key(sr):
            sr_name = witnesses[sr]['url']
        else:
            sr_name = '-'
        if srs_cnts_map.has_key(sr):
            oft_cnt = srs_cnts_map[sr]
            print(templ %(sr, sr_name, oft_cnt))

def txs(witness, recent_days = 0, min_block = 0, max_block = 0):
    store = Store()
    srs = store.get_srs()
    trx_list = []
    def extend_trx(trxs):
        trx_list.extend(trxs)

    def traversing_blocks(start, end):
        for block_number in range(start, end + 1):
            trxs = store.get_sr_block_oft_trxs(witness, block_number)
            extend_trx(trxs)

    db_start = store.start_point()
    db_end = store.end_point()
    process_start = db_start
    process_end = db_end

    if recent_days == 0 and min_block == 0 and max_block == 0:
        pass
    elif recent_days != 0:
        sec = recent_days * 24 * 60 * 60
        blocks = int(sec / 3)
        start = db_end - blocks
        if start < db_start:
            print fire.core.formatting.Error('specified time span is too large and needs '
                                             'to be parsed from block %d and currently %d' % (start, db_start))
            return
        process_start = start
        process_end = db_end
    elif recent_days == 0 and min_block != 0 or max_block != 0:
        if min_block >= max_block:
            print fire.core.formatting.Error('min_block must be less than max_block')
            return

        if min_block < db_start or max_block > db_end:
            print fire.core.formatting.Error('The specified time range is incorrect and '
                                             'must be between %d and %d' %(db_start, db_end))
            return
        process_start = min_block
        process_end = max_block
    else:
        print fire.core.formatting.Error('min_block and max_block specify errors')
        return

    traversing_blocks(process_start, process_end)

    start_timestamp = store.get_block_time(process_start)
    end_timestamp = store.get_block_time(process_end)
    util.status_msg_div()
    util.status_msg('Time  Range:', '%s ~ %s' % (util.timestamp_to_strftime(start_timestamp), util.timestamp_to_strftime(end_timestamp)))
    util.status_msg('Block Range:', '%d ~ %d' % (process_start, process_end))
    util.status_msg_div()

    templ = '%-70s %-16s %-25s %-20s'
    print fire.core.formatting.Bold(
        templ % ('TxId', 'Ret', 'Time','FuncID')
    )
    for trx in trx_list:
        txid = trx['txID']
        ret = trx['ret'][0]['contractRet']
        funcid = trx['raw_data']['contract'][0]['parameter']['value']['data'][0:8]
        timestamp = trx['raw_data']['timestamp']
        strftime = util.timestamp_to_strftime(timestamp)
        print(templ % (txid, ret, strftime, funcid))





def main():
    fire.Fire({
        'parse': parse,
        'status':status,
        'query':query,
        'txs':txs,
    })

def exit_handler(signum, frame):
    exit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_handler)
    signal.signal(signal.SIGTERM, exit_handler)
    sys.exit(main())