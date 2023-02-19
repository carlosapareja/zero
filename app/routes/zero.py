from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerRangeField
import random
import string

zero = Blueprint('zero', __name__)

class GeneratedPassword(FlaskForm):
    password = StringField('Example')
    size = IntegerRangeField('Size', render_kw={"min": 6, "max": 66})
    submit = SubmitField('')

def generate(size):
    characters = string.ascii_letters + string.digits + string.punctuation
    passw = ''.join(random.choice(characters) for i in range(size))
    
    return passw

@zero.route('/pass', methods=['GET', 'POST'])
def pass_generator():
    password = GeneratedPassword()

    if password.is_submitted():
        x = password.size.data
        z = generate(x)
        password.password.data = z

    context = {
        'password': password
    }
    return render_template('zero.html', **context)