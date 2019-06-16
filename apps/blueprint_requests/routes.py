from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import InputRequired, Optional
from programs.course import get_course_id

mod = Blueprint('blueprints', __name__, template_folder="templates")


class RequestForm(FlaskForm):
    source = TextAreaField('Make a blueprint', validators=[InputRequired()])
    target = TextAreaField('Use a blueprint', validators=[Optional()])


@mod.route('/', methods=['GET', 'POST'])
def request_form():
    form = RequestForm()
    if form.validate_on_submit():
        print(form.data)
        print(get_course_id(form.data['source']))
        return 'Form OK'

    return render_template('index_blu.html', form=form)
