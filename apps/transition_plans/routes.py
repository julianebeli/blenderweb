from flask import Blueprint, render_template, request, jsonify
# from flask_wtf import FlaskForm
# from wtforms import TextAreaField
# from wtforms.validators import InputRequired, Optional
from programs.course import get_course_id, get_course_name

mod = Blueprint('transitions', __name__, template_folder="templates", )


# class RequestForm(FlaskForm):
#     source = TextAreaField('Add Transition Plan', validators=[InputRequired()])
#     # target = TextAreaField('Use a blueprint', validators=[Optional()])


@mod.route('/', methods=['GET', 'POST'])
def request_form():

    # form = RequestForm()
    # if form.validate_on_submit():
    #     print(form.data)
    #     print(get_course_id(form.data['source']))
    #     return 'Form OK'

    return render_template('index_transition.html',)


@mod.route('/check_course_id', methods=['GET', 'POST'])
def check_input():
    course_input = request.json
    # print("COURSE INPUT", course_input['course'])
    return(jsonify(get_course_name(course_input['course'])))
