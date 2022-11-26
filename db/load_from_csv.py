import csv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from menu_items import get_database
from models import Heroes, Heroes_info, Stats
from operations import select
from settings import *

engine = None

if DB_ENGINE == "postgresql":
    engine = create_engine(
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=True)

if engine is None:
    print('error!')
    exit()

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


def insert_heroes():
    database = get_database()
    table_main = database.get(1)
    table_stats = database.get(3)
    table_hero_info = database.get(2)

    with open(table_main, "r", encoding="UTF-8") as file:
        bd = csv.DictReader(file, delimiter=';')

        for line_hero in bd:
            hero = Heroes(
                name=line_hero['name'],
                cost=int(line_hero['cost']),
                role=int(line_hero['role'])

            )

            session.add(hero)
            session.commit()

            line_hero_stats = select(table_stats, 'id', line_hero['id'])
            hero_stats = Stats(
                hp=int(line_hero_stats['hp']),
                damage=int(line_hero_stats['damage']),
                mana=int(line_hero_stats['mana']),
                distance=int(line_hero_stats['distance']),
                speed=float(line_hero_stats['speed']),
                armor=int(line_hero_stats['armor']),
                magic_resistance=int(line_hero_stats['magic_resistance']),
                heroes_id=hero.id_heroes
            )

            session.add(hero_stats)

            line_hero_info = select(table_hero_info, 'id', line_hero['id'])
            hero_info = Heroes_info(
                class_heroes=int(line_hero_info['class']),
                meta=int(line_hero_info['meta']),
                is_alliance=int(line_hero_info['is_alliance']),
                heroes_id=hero.id_heroes

            )

            session.add(hero_info)
            session.commit()


insert_heroes()
