import os 

from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail, Message

from forms import ContactForm, RequestForm

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ['EMAIL_USER']
app.config['MAIL_PASSWORD'] = os.environ['EMAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def send_mail(email, body, name):
    '''Helper function for sending emails with flask_mail'''

    body_message = '''
Hello {name},

Thank you for contacting us here at evolo.
Please send us details of what you need so we can get to you quickly.

Evolo Team.'''.format(name=name)

    msg = Message(subject='Evolo Message',
                  sender=app.config.get('MAIL_USERNAME'),
                  recipients=[email],
                  body=body_message)

    mail.send(msg)

def reply_request(name, email, option):
    '''Helper function for replying to requests made on the website'''

    subject = 'Evolu - {}'.format(option)
    body = '''
Hello {name},

Thank you for showing you interest in the {option} package.
We'll send you the detail of the {option} package via this email.

Regards,

Evolo Team.
'''.format(name=name, option=option)

    msg = Message(subject=subject,
                  sender=app.config.get('MAIL_USERNAME'),
                  recipients=[email],
                  body=body
                  )

    mail.send(msg)


@app.route('/', methods=('GET', 'POST'))
def index():

    form = ContactForm()
    request_form = RequestForm()

    if form.validate_on_submit():

        name = form.name.data
        body = form.body.data
        email = form.email.data
        
        send_mail(name, email, body)

        return redirect(url_for('index'))
    
    if request_form.validate_on_submit():

        name = request_form.name.data
        email = request_form.email.data
        phone = request_form.email.data
        option = request_form.select.data

        reply_request(name, email, option)

        return redirect(url_for('index'))

    return render_template('index.html', form=form, request_form=request_form)


@app.route('/terms-and-conditions')
def terms():
    return render_template('terms-conditions.html', title='Terms and Conditions')


@app.route('/privacy-policy')
def privacy():
    return render_template('privacy-policy.html', title='Privacy Policy')


#Error handlers...

#Client error
@app.errorhandler(404)
def handle_404(e):
    return redirect(url_for('index'))

#Server error
@app.errorhandler(500)
def handle_500(e):
    return redirect(url_for('index'))