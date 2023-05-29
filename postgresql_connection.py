from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings

class HangmanLeaderboard():

    def __init__(self):
        self.engine = self.get_engine(settings["pguser"],
                                      settings["pgpassword"],
                                      settings["pghost"],
                                      settings["pgport"],
                                      settings["pgdb"]
         )
        self.session = self.get_session()

    def get_engine(self, user, password, host, port, db):
        url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
        if not database_exists(url):
            create_database(url)
        self.engine = create_engine(url, pool_size = 50, echo = False)
        return self.engine

    def get_session(self):
        self.session = sessionmaker(bind = self.engine)()
        return self.session
    


