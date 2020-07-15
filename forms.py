from flask_wtf import FlaskForm

from wtforms import (
    StringField, 
    TextAreaField, 
    SubmitField, 
    BooleanField,
    IntegerField,
    SelectField,
)

from wtforms.validators import (
    DataRequired, 
    Length, 
    Email
) #Have to install email_validator for Email validator to work

class ContactForm(FlaskForm):
    '''Contact form'''

    name = StringField('Name', validators=[DataRequired(), Length(min=4)])

    email = StringField('Email', validators=[
        Email(message=('Not a valid email address')),
        DataRequired()])

    body = TextAreaField('Your message', validators=[
        DataRequired(),
        Length(min=2, message=('Your message is too short.'))
    ])

    agree = BooleanField('Agree to Terms', validators=[
        DataRequired(),
    ])

    submit = SubmitField('SEND MESSAGE')

class RequestForm(FlaskForm):
    '''Request Form'''

    name = StringField('Full name', validators=[
        DataRequired(), 
        Length(min=4)
    ])

    email = StringField('Email', validators=[
        DataRequired(), 
        Email(message=('This is an invalid email'))
    ])

    phone = IntegerField('Phone', validators=[
        DataRequired()
    ])

    select = SelectField('Interested In', 
        validators=[DataRequired()], 
        choices=(
            ('starter', 'Starter'),
            ('medium', 'Medium'),
            ('complete', 'Complete'),
        )
    )

    agree = BooleanField('Agree to Terms',  validators=[
        DataRequired(),
    ])
    
    submit = SubmitField('REQUEST')

