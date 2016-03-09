import requests


class RIDBUtils(object):
    def __init__(self):
        pass



class RIDBQuery:
    def __init__(self, ridb_config):
        self.config = ridb_config
        self.key_suffix = '?apikey='
        pass

    def query_endpoint(self, endpoint):
        myResponse = requests.get(self._build_url(endpoint), verify=True)
        if myResponse.ok:
            pass

    def _build_url(self, endpoint):
        return self.config.apiloc + endpoint + self.config.format + self.key_suffix + self.config.key


class RIDBConfig:
    def __init__(self, api_loc, api_key, restformat='.json'):
        self.apiloc = api_loc
        self.key = api_key
        self.format = restformat

    @property
    def key(self):
        return self.key

    @property
    def location(self):
        return self.apiloc
