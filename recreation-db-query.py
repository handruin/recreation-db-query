import requests

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
    def __init__(self, api_loc, api_key, format='.json'):
        self.apiloc = api_loc
        self.key = api_key
        self.format = format

    @property
    def key(self):
        return self.key

    @property
    def location(self):
        return self.apiloc


class APIKEY:
    def __init__(self, file_loc):
        self.apikey_location = file_loc
        pass

    @property
    def key(self):
        try:
            with open(self.apikey_location, 'r') as f:
                return f.readline().strip()
        except Exception as ex:
            print("Unable to open key file: ", ex)
