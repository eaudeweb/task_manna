import requests
from task_manna.log import Logger


class Manna(object):
    _api_key = ''
    _url = ''
    _uid = 0


    __data = None


    def __init__(self, url: str, api_key: str, uid: int):
        self._url = url
        self._api_key = api_key
        self._uid = uid


    def __call__(self) -> dict:
        return self.data

    @property
    def data(self) -> dict:
        if self.__data is None:
            self.__data = fetch_remote(self._url, self._api_key, self._uid)
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
        return self._metadata.get(name, None)



def fetch_remote(base_url: str, api_key: str, user_id: int) -> dict:
    url = '{}/issues.json'.format(base_url)

    payload = dict(assigned_to_user_id=user_id, status_id='open')
    headers = {
        'X-Redmine-API-Key': api_key
    }

    resp = requests.get(url, params=payload, headers=headers)

    logger = Logger('fetch_remote')
    logger.debug(resp.url)

    return resp.json()
