import logging


class Logger(object):

    __base_name = 'task_manna'
    __logger = None
    __level = 'WARNING'

    def __init__(self, name=''):
        if name:
            self.name = '{}.{}'.format(self.__base_name, name)
        else:
            self.name = self.__base_name

    def __getattr__(self, name):
        return getattr(self.get(), name)

    @classmethod
    def set_level(cls, level: str):
        cls.__level = level

    def get(self):
        if not self.__logger:
            logger = logging.getLogger(self.name)
            logger.setLevel(self.__level)

            # log to console
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(self.__level)

            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            stream_handler.setFormatter(formatter)

            logger.addHandler(stream_handler)

            self.__logger = logger
        return self.__logger
