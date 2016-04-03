import requests
import json
from apikeymanager import APIKeyManager


# RecAreaAddress > RecArea > Facility > Campsite > Attribute > PermitEntrance
class APIClient:
    def __init__(self, url, extra_params=None, offset=0, limit=0, export_format='json', timeout=10):
        self._url = url
        self._extra_payload_params = extra_params
        self._offset = offset
        self._limit = limit
        km = APIKeyManager(file_loc='./dev-ridb-api.key')
        self._api_key = km.key
        self._export_format = '.' + export_format  # .json | .xml
        self._timeout = timeout

    def make_api_call(self, extra_params=None, append_url=None):
        headers = {'apikey': self._api_key}
        params_payload = {'offset': self._offset, 'limit': self._limit}
        if self._extra_payload_params is not None:
            params_payload.update(self._extra_payload_params)
        if extra_params is not None:
            params_payload.update(extra_params)
        if append_url is not None:
            self.append_url_val(append_url)
        my_response = requests.get(self._url + self._export_format,
                                   verify=True,
                                   headers=headers,
                                   params=params_payload,
                                   timeout=self._timeout)
        if my_response.ok:
            print('Response OK...')
            jdata = my_response.json()
            return json.dumps(jdata)
        else:
            raise Exception('Failed to get valid response of: ', my_response.status_code)

    def append_url_val(self, val):
        self._url += '/' + val


class RecAreaAddress:
    def __init__(self):
        pass


class RecArea:
    def __init__(self):
        pass

    def rec_area_name(self):
        pass

    def rec_area_description(self):
        pass


class Facility:
    def __init__(self):
        self.base_url = "https://ridb.recreation.gov/api/v1/facilities"
        self._api_client = APIClient(self.base_url)

    def query_by_name_param(self, name):
        data = self._api_client.make_api_call({'query': name})
        return data

    def query_by_id(self, facility_id):
        data = self._api_client.make_api_call(append_url=str(facility_id))
        return data


class Campsite:
    def __init__(self):
        pass


class Attribute:
    def __init__(self):
        pass


class PermitEntrance:
    def __init__(self):
        pass