import os
from importlib import resources

from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import asc, desc, func

from database import Base
from deck_record import DeckRecord
from dice_record import DiceRecord
from card_record import CardRecord
from result_record import ResultRecord
from result_type_record import ResultTypeRecord

def main():
    path_to_db = 'sqlite:///'+os.getcwd()+'/settings.db'
    print(path_to_db)
    engine = create_engine(path_to_db)
    Base.metadata.create_all(engine)


    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    print(session.query(DeckRecord.deck_name).all())

    session.close()



if __name__ == "__main__":
    main()