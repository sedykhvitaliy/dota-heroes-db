from sqlalchemy import create_engine, MetaData
from db.settings import *
from db.models import Heroes, Heroes_info, Stats


def get_engine():
    eng = None
    if DB_ENGINE == "postgresql":
        eng = create_engine(
            f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=True)

    return eng


def get_meta(engine):
    return MetaData(engine)


engine = get_engine()

if engine is None:
    print('error!')
    exit()

Heroes.metadata.create_all(engine)
Heroes_info.metadata.create_all(engine)
Stats.metadata.create_all(engine)
