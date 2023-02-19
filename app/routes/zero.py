from flask import Blueprint, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField
import random
import string

zero = Blueprint('zero', __name__)

class GeneratedPassword(FlaskForm):
    password_text = StringField('Example', id='password-value')
    password_length = IntegerRangeField('Size', render_kw={"min": 6, "max": 66}, id='password-len')
    generate_password = SubmitField('', id='generate')

def generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passw = ''.join(random.choice(characters) for i in range(length))
    
    return passw

@zero.route('/')
def index():
    return redirect('/password')

@zero.route('/password', methods=['GET', 'POST'])
def pass_generator():
    password = GeneratedPassword()

    if password.is_submitted():
        password_length = password.password_length.data
        final_password = generate(password_length)
        password.password_text.data = final_password

    context = {
        'password': password
    }
    return render_template('zero.html', **context)