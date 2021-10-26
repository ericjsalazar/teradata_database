import logging

import sqlalchemy
from sqlalchemy.engine.base import Engine

LOGGER = logging.getLogger(__name__)

class TeradataDatabase(object):

    def __init__(self, host: str, username: str, password: str):
        self._host = host
        self._username = username
        self._password = password
        self.uri = f'teradatasql://{self._host}/?user={self._username}&password={self._password}'
        self.engine : Engine = sqlalchemy.create_engine(self.uri)
        self.cursor = None
    
    def __enter__(self):
        self.cursor = self.engine.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        trans = self.cursor.begin()
        if exc_tb is None:
            trans.commit()
        else:
            trans.rollback()
        self.cursor.close()