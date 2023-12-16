"""
Crud simples em sqllite e peewee ORM

"""
from peewee import *

db = SqliteDatabase('guide.db')

class Contact(Model):
    name = CharField()
    telefone = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Contact])

pessoa1 = Contact(name='pessoa 1', telefone='(00) 0 0000-0000')
pessoa1.save()

pessoa1.name = "Pessoa 2"
pessoa1.save()

p = Contact.get_by_id(1)
p.delete_instance()

db.close()