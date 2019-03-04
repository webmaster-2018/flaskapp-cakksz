from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required
from wtforms import BooleanField, SelectField
from wtforms import StringField, HiddenField, IntegerField
from wtforms.validators import DataRequired

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
  id = HiddenField()
  nazwa = StringField('Nazwa klasy:', validators=[DataRequired(message=blad1)])
  rok_naboru = IntegerField('Rok naboru:', validators=[DataRequired(message=blad1)])
  rok_matury = IntegerField('Rok matury:', validators=[DataRequired(message=blad1)])


class UczenForm(FlaskForm):
    pass
  id = HiddenField()
  imie = StringField('Imię ucznia:', validators=[DataRequired(message=blad1)])
  nazwisko = StringField('Nazwisko ucznia:', validators=[DataRequired(message=blad1)])
  plec = BooleanField('Płeć ucznia:', validators=[DataRequired(message=blad1)])
  klasa = SelectField('Klasa', coerce=int)
