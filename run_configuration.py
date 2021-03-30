from alchemy import List, Tweet, User, Hashtag, Mention, Url
from json import load
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session, sessionmaker


# Criando tabelas
with open("config.json") as jsonfile:
    db_config = load(jsonfile)['database_dml']

engine = create_engine(URL(db_config['drivername'],
                           db_config['username'], db_config['password'],
                           db_config['host'], db_config['port'],
                           db_config['database']))

List.__table__.create(bind=engine, checkfirst=True)
User.__table__.create(bind=engine, checkfirst=True)
Tweet.__table__.create(bind=engine, checkfirst=True)
Hashtag.__table__.create(bind=engine, checkfirst=True)
Mention.__table__.create(bind=engine, checkfirst=True)
Url.__table__.create(bind=engine, checkfirst=True)


# Adicionando dados iniciais
with open("config.json") as jsonfile:
    db_config = load(jsonfile)['database_ddl']

engine = create_engine(URL(db_config['drivername'],
                           db_config['username'], db_config['password'],
                           db_config['host'], db_config['port'],
                           db_config['database']))


Session = sessionmaker(bind=engine)
session = Session()


session.add(List(list_id="1280558411680284672", name="Deputados em Exercício", owner_id="1280491692131520515", address="https://twitter.com/i/lists/12805584116802846"))

session.commit()
