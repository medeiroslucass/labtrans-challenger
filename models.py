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

def create_database():
    db.connect()
    db.create_tables(
        [
            Results
        ]
    )

    db.close()

