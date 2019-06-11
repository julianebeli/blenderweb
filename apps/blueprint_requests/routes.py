from flask import Blueprint

mod = Blueprint('blueprints', __name__)


@mod.route('/')
def homepage():
    return '<h1>You are on the blueprints homepage</h1>'
