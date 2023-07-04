import logging

from sqlalchemy import (
    create_engine,
    Engine
)
from sqlalchemy.orm import (
    declarative_base,
    Session
)

from kernel.settings import config
from painless.design import Singleton

DB_CONFIG = config['database']
logger = logging.getLogger("core")


class SQLalchemy(metaclass=Singleton):
    """
    Creating a database and session engine using the singleton design pattern
    """
    def __init__(self):
        self.engine = self.create_engine()
        self.Base = declarative_base()
        self.session = self.create_session()

    @staticmethod
    def create_engine() -> Engine:
        """
        It builds an engine using the toml settings information
        """

        engine = create_engine(
            f"{DB_CONFIG['ENGINE']}+{DB_CONFIG['DRIVER']}://"
            f"{DB_CONFIG['USER']}:{DB_CONFIG['PASSWORD']}@{DB_CONFIG['HOST']}:"
            f"{DB_CONFIG['PORT']}/{DB_CONFIG['NAME']}"
        )
        logger.info("The database engine was created")
        return engine

    def create_session(self) -> Session:
        logger.info("The database session was created")
        return Session(self.engine)
