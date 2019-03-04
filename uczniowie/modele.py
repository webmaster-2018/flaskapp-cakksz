from peewee import *

baza_plik = 'uczniowie.db'
############## MODEL
# MODEL
baza = SqliteDatabase(baza_plik)


class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
  nazwa = CharField(null=False)
  roknaboru = IntegerField(default=0)
  rokmatury = IntegerField(default=0)
  rok_naboru = IntegerField(default=0)
  rok_matury = IntegerField(default=0)


class Uczen(BazaModel):
