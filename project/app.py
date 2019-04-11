from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask import render_template, redirect
from flask_mail import Mail,  Message
from decouple import config

from forms import ContactsForm


app = Flask(__name__)

mail_settings = {
    'MAIL_SERVER': config('MAIL_SERVER'),
    'MAIL_PORT': 587,
    'MAIL_DEFAULT_SENDER': config('MAIL_DEFAULT_SENDER'),
    'MAIL_USERNAME': config('MAIL_USERNAME'),
    'MAIL_PASSWORD': config('MAIL_PASSWORD'),
    'MAIL_USE_TLS': True,
    'MAIL_SEND_TO': config('MAIL_SEND_TO')
}

app_settings = {
    'WTF_CSRF_ENABLED': True,
    'SECRET_KEY': config('SECRET_KEY'),
}

app.config.update(mail_settings)
app.config.update(app_settings)
CSRFProtect(app)

mail = Mail(app)


@app.route('/', methods=('GET', 'POST'))
def main():
    form = ContactsForm()
    if form.validate_on_submit():

        send_mail(form)
        return render_template('base.html')
    return render_template('base.html', form=form)


def send_mail(form):
    letter = render_template('letter.html', data=form)
    msg = Message("Заявка с сайта http://horizons.co.ua/",
                  recipients=[app.config['MAIL_SEND_TO']])
    msg.html = letter
    mail.send(msg)
