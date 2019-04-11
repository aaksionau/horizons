from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email

REGIONS = (
    ('Vinnytsia', 'Винницкая область'),
    ('Volynska', 'Волынская область'),
    ('Dnepr', 'Днепропетровская область'),
    ('Donetsk', 'Донецкая область'),
    ('Zhitomirskaya', 'Житомирская область'),
    ('Transcarpathian', 'Закарпатская область'),
    ('Zaporozhye', 'Запорожская область'),
    ('Ivano-Frankivsk', 'Ивано-Франковская область'),
    ('Kievskaya', 'Киевская область'),
    ('Kiev', 'Киев'),
    ('Kirovograd', 'Кировоградская область'),
    ('Luhansk', 'Луганская область'),
    ('Lviv', 'Львовская область'),
    ('Mykolayiv', 'Николаевская область'),
    ('Odesa', 'Одесская область'),
    ('Poltava', 'Полтавская область'),
    ('Rivne', 'Ровенская область'),
    ('Sumy', 'Сумская область'),
    ('Ternopil', 'Тернопольская область'),
    ('Kharkivska', 'Харьковская область'),
    ('Kherson', 'Херсонская область'),
    ('Khmelnytskyi', 'Хмельницкая область'),
    ('Cherkasy', 'Черкасская область'),
    ('Chernihiv', 'Черниговская область'),
    ('Chernivtsi', 'Черновицкая область'),
)

CHILDREN_QUANTITY = (
    ('30', 'до 30'),
    ('50', '30-50'),
    ('100', '50-100'),
    ('200', '100-200'),
    ('300', '200-300'),
)


class ContactsForm(FlaskForm):
    school_name = StringField('Повна назва навчального закладу', validators=[
                              DataRequired('Введите название школы')])
    street = StringField('Вулиця', validators=[
                         DataRequired('Введите название улицы')])
    house = IntegerField('Номер будинку', validators=[
                         DataRequired('Введите номер дома')])
    city = StringField('Місто/населений пункт',
                       validators=[DataRequired('Введите город')])
    region = SelectField('Область', choices=REGIONS)
    director_name = StringField(
        'ПІБ директора школи', validators=[DataRequired('Введите имя и фамилию директора')])
    director_phone = IntegerField(
        'Номер телефону директора школи', validators=[DataRequired('Введите номер телефона директора.')])
    director_email = StringField('E-mail директора школи', validators=[
                                 DataRequired(), Email('Вы ввели некорректный email. Попробуйте еще раз.')])
    children_quantity = SelectField(
        'Кількість дітей', choices=CHILDREN_QUANTITY)
    text = TextAreaField(
        'Коротко обґрунтуйте, чому ви хочете взяти участь в проекті «Альфа-горизонт» (За бажанням)')
