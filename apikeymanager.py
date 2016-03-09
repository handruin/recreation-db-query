import configparser
import os


class APIKeyManager(object):
    RIDB_KEY_SECTION = 'RIDBAPIAccessKey'
    RIDB_KEY_NAME = 'user.ridbkey'

    def __init__(self, file_loc='./ridb-api.key'):
        self.apikey_property_location = file_loc

    @property
    def key(self):
        key_config = self._load_config(self.apikey_property_location)
        return key_config[self.RIDB_KEY_SECTION][self.RIDB_KEY_NAME]

    @key.setter
    def key(self, key):
        self._save_config(self.apikey_property_location, str(key))

    def is_key_set(self):
        if self.key:
            return True
        return False

    def _load_config(self, file_loc):
        if os.path.exists(file_loc):
            config = configparser.ConfigParser()
            config.read(file_loc)
            return config
        else:
            raise FileNotFoundError('Error: API key properties file not found!')

    def _save_config(self, file_loc, key_val):
        if os.path.exists(file_loc) and key_val:
            config = configparser.ConfigParser()
            config[self.RIDB_KEY_SECTION] = {}
            config[self.RIDB_KEY_SECTION][self.RIDB_KEY_NAME] = key_val
            with open(file_loc, 'w') as configfile:
                config.write(configfile)
        else:
            raise ValueError('Missing file location and/or key value!')


