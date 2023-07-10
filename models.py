from peewee import *

db = SqliteDatabase('labtrans.db')


class BaseModel(Model):
    class Meta:
        database = db


class Results(BaseModel):
    name = CharField()
    km = DoubleField()
    distance = DoubleField()
    highway = IntegerField()
    item = CharField()


# Definição do modelo de tabela "Vídeos"
class Video(BaseModel):
    name = CharField()
    km_ini = DoubleField()
    km_final = DoubleField()


# Definição do modelo de tabela "Rodovias"
class Rodovia(BaseModel):
    highway = CharField()
    km_ini = DoubleField()
    km_final = DoubleField()


def create_database():
    db.connect()
    db.create_tables(
        [
            Results,
            Video,
            Rodovia
        ]
    )

    db.close()

create_database()
