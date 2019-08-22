import leveldb
import os
import schema
import json
from util import db_path




class DB():
    def __init__(self, filename = db_path):
        self.filename = filename
        dirname = os.path.dirname(self.filename)
        if not os.path.exists(dirname):
           os.makedirs(dirname)
        self.db = leveldb.LevelDB(self.filename)

    def put(self, *args, **kwargs):
        self.db.Put(*args, **kwargs)

    def has_key(self, key):
        try:
            self.db.Get(key)
        except KeyError:
            return False
        return True

    def get(self, *args, **kwargs):
        return self.db.Get(*args, **kwargs)


class Store():
    def __init__(self):
        self.db = DB()
        self.srs = self.__get_srs()
        self.oft_cnts = {}
        self.sr_blocks = {}

    def update_start_point(self, start):
        self.db.put(schema.dbkey_block_start, str(start))

    def start_point(self):
        if self.db.has_key(schema.dbkey_block_start):
            return int(self.db.get(schema.dbkey_block_start))
        return -1

    def update_end_point(self, end):
        self.db.put(schema.dbkey_block_end, str(end))

    def end_point(self):
        if self.db.has_key(schema.dbkey_block_end):
            return int(self.db.get(schema.dbkey_block_end))
        return -1

    def get_srs(self):
        return self.__get_srs()

    def __get_srs(self):
        if self.db.has_key(schema.dbkey_srs):
            srs_string = self.db.get(schema.dbkey_srs)
            try:
                return json.loads(srs_string)
            except Exception:
                return []
        else:
            return []

    def try_add_sr(self, sr):
        if sr not in self.srs:
            self.srs.append(sr)
            self.update_srs(self.srs)

    def update_srs(self, srs):
        srs_string = json.dumps(srs)
        self.db.put(schema.dbkey_srs, srs_string)


    def get_sr_oft_cnts(self, witness):
        if self.db.has_key(schema.dbkey_sr_oft_cnts(witness)):
            return int(self.db.get(schema.dbkey_sr_oft_cnts(witness)))
        return 0

    def add_oft_cnts(self, witness, cnt):
        if not self.oft_cnts.has_key(witness):
            db_cnt = self.get_sr_oft_cnts(witness)
            self.oft_cnts[witness] = db_cnt
        self.oft_cnts[witness] += cnt
        self.update_sr_oft_cnts(witness, self.oft_cnts[witness])

    def update_sr_oft_cnts(self, witness, counter):
        self.db.put(schema.dbkey_sr_oft_cnts(witness), str(counter))


    def get_sr_block_oft_cnts(self, witness, number):
        key = schema.dbkey_block_number_sr_oft_cnts(number, witness)
        if self.db.has_key(key):
            return int(self.db.get(key))
        return 0

    def update_sr_block_oft_cnts(self, witness, number, counter):
        key = schema.dbkey_block_number_sr_oft_cnts(number, witness)
        self.db.put(key, str(counter))

    def get_sr_block_oft_trxs(self, witness, number):
        key = schema.dbkey_block_number_sr_oft_txs(number, witness)
        if self.db.has_key(key):
            trxs_string = self.db.get(key)
            try:
                return json.loads(trxs_string)
            except Exception:
                return []
        return []

    def update_sr_block_oft_trxs(self, witness, number, trxs):
        key = schema.dbkey_block_number_sr_oft_txs(number, witness)
        trxs_string = json.dumps(trxs)
        self.db.put(key, trxs_string)

    def update_block_time(self, number, timestamp):
        key = schema.dbkey_block_number_to_time(number)
        self.db.put(key, str(timestamp))

    def get_block_time(self, number):
        key = schema.dbkey_block_number_to_time(number)
        if self.db.has_key(key):
            return int(self.db.get(key))
        return 0

    def get_sr_blocks_cnts(self, witness):
        key = schema.dbkey_sr_blocks_cnts(witness)
        if self.db.has_key(key):
            return int(self.db.get(key))
        return 0

    def add_sr_blocks_cnts(self, witness, cnt):
        key = schema.dbkey_sr_blocks_cnts(witness)
        if not self.sr_blocks.has_key(witness):
            db_cnts = self.get_sr_blocks_cnts(witness)
            self.sr_blocks[witness] = db_cnts
        self.sr_blocks[witness] += cnt
        self.db.put(key, str(self.sr_blocks[witness]))

        self.get_sr_blocks_cnts(witness)


