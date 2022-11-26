from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Heroes(Base):

    __tablename__ = "db_heroes"

    id_heroes = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cost = Column(Integer, nullable=False)
    role = Column(Integer, nullable=False)


class Stats(Base):

    __tablename__ = "db_stats"

    id_Stats = Column(Integer, primary_key=True)
    heroes_id = Column(Integer, ForeignKey("db_heroes.id_heroes"))
    hp = Column(Integer, nullable=False)
    mana = Column(Integer, nullable=False)
    damage = Column(Integer, nullable=False)
    speed = Column(Float, nullable=False)
    distance = Column(Integer, nullable=False)
    armor = Column(Integer, nullable=False)
    magic_resistance = Column(Integer, nullable=False)


class Heroes_info(Base):

    __tablename__ = "db_heroes_info"

    id_heroes_info = Column(Integer, primary_key=True)
    heroes_id = Column(Integer, ForeignKey("db_heroes.id_heroes"))
    class_heroes = Column(Integer, nullable=False)
    meta = Column(Integer, nullable=False)
    is_alliance = Column(Integer, nullable=False)
