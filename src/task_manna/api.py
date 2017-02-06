import requests


class Manna(object):
    _api_key = ''
    _url = ''


    __data = None


    def __init__(self, url: str, api_key: str):
        self._url = url
        self._api_key = api_key


    def __call__(self) -> dict:
        return self.data

    @property
    def data(self) -> dict:
        if self.__data is None:
            self.__data = fetch_remote(self._url, self._api_key)
        return self.__data

    @property
    def tasks(self) -> []:
        for issue in self.data['issues']:
            yield Task(issue)



class Task(object):
    _metadata = None


    def __init__(self, metadata: dict):
        self._metadata = metadata


    def __getattr__(self, name: str):
        return self._metadata[name]



def fetch_remote(base_url: str, api_key: str, user_id='me') -> dict:
    url = '{}/issues.json'.format(base_url)

    payload = dict(assigned_to_user_id='me', status_id='open')
    headers = {
        'X-Redmine-API-Key': api_key
    }

    r = requests.get(url, params=payload, headers=headers)

    return r.json()
