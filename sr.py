
def get_witnesses(client):
    srs = client.listwitnesses()
    srs = srs['witnesses']
    srs_map = {}
    for sr in srs:
        addr = sr['address']
        srs_map[addr] = sr
    return srs_map


