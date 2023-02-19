from flask import Blueprint, render_template, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField, BooleanField
import random
import string

zero = Blueprint('zero', __name__)

class GeneratedPassword(FlaskForm):
    password_text = StringField('Example', id='password-value')
    password_length = IntegerRangeField('Size', render_kw={"min": 6, "max": 66}, id='password-len')
    include_lowercase = BooleanField('Include lowercase', id='include_lowercase')
    include_uppercase = BooleanField('Include uppercase')
    include_numbers = BooleanField('Include numbers')
    include_symbols = BooleanField('Include symbols')
    # generate_password = SubmitField('', id='generate')

def generate(length, use_lower=True, use_upper=True, use_digits=True, use_punctuation=True):
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    passw = ''.join(random.choice(characters) for i in range(length))
    
    return passw

@zero.route('/')
def index():
    return redirect('/password')

@zero.route('/password', methods=['GET', 'POST'])
def pass_generator():
    password = GeneratedPassword()

    if password.is_submitted():
        use_lower = password.include_lowercase.data
        use_upper = password.include_uppercase.data
        use_numbers = password.include_numbers.data
        use_symbols = password.include_symbols.data
        password_length = password.password_length.data

        if use_upper == False and use_lower == False and use_numbers == False and use_symbols == False:
            flash(f'Please, choose an option', category='danger')
            password.password_text.data = 'Choose an option'
        else:
            final_password = generate(password_length, use_lower, use_upper, use_numbers, use_symbols)
            password.password_text.data = final_password

    context = {
        'password': password
    }

    return render_template('zero.html', **context)