from sqlalchemy import create_engine
from settings import *
from models import Heroes, Heroes_info, Stats

engine = None

if DB_ENGINE == "postgresql":
    engine = create_engine(
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=True)

if engine == None:
    print('error!')
    exit()

Heroes.metadata.create_all(engine)
Heroes_info.metadata.create_all(engine)
Stats.metadata.create_all(engine)
