import requests
import json
import util

trongrid_url = 'https://api.trongrid.io'

#https://api.trongrid.io/wallet/getblockbynum

class ApiClient():
    def __init__(self):
        self.__url = trongrid_url + '/wallet/'


    def send_post(self, url, data=None):
        data = json.dumps(data)
        response = requests.post(url, data)
        if response.status_code > 201:
            try:
                error = response.json()
            except:  # response.content not formatted as JSON
                error = str(response.content)
            raise APIError('TronGrid API returned HTTP %s (%s)' % (response.status_code, error))
        else:
            try:
                return response.json()
            except:  # Nothing to return
                return {}
    def __post(self, url, data=None, retry = True):
        while(True):
            ret = {}
            try:
                ret = self.send_post(url, data)
            except Exception, err:
                if retry:
                    again = True
                    util.log_info('retry https post:%s because of %s' % (url, err.message))
                else:
                    raise err
            return ret

    def get_block_by_number(self, number):
        url = self.__url + 'getblockbynum'
        return self.__post(url, data = {'num':number})

    def get_now_block(self):
        url = self.__url + 'getnowblock'
        return self.__post(url)

    def get_now_blocknumber(self):
        block = self.get_now_block()
        return block['block_header']['raw_data']['number']

    def listwitnesses(self):
        url = self.__url + 'listwitnesses'
        return self.__post(url)


class APIError(Exception):
    pass
