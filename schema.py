

dbkey_block_start = 'block_start'
dbkey_block_end = 'block_end'

dbkey_srs = 'super_representative_list'

dbkey_sr_trans = 'sr_out_of_time_transactions'






def dbkey_block_number_sr_oft_cnts(number, sr):
    return 'block_number_sr_oft_cnts_%d_%s' %(number, sr)

def dbkey_block_number_sr_oft_txs(number, sr):
    return 'block_number_sr_oft_txs_%d_%s' %(number, sr)

def dbkey_block_number_to_time(number):
    return 'block_number_to_time %d' % number

def dbkey_sr_oft_cnts(sr):
    return 'sr_oft_cnts_%s' % sr

def dbkey_sr_blocks_cnts(sr):
    return 'sr_blocks_%s' % sr
