from flask import Blueprint

mod = Blueprint('injector', __name__)


@mod.route('/')
def homepage():
    return '<h1>You are on the injector homepage</h1>'
