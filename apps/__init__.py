__all__ = ['blueprint_requests', 'outcome_injector']

from apps.outcome_injector.routes import mod
from apps.blueprint_requests.routes import mod
from flask import Flask


app = Flask(__name__)


app.register_blueprint(blueprint_requests.routes.mod, url_prefix='/blueprints')
app.register_blueprint(outcome_injector.routes.mod, url_prefix='/outcomes')


@app.route('/')
def index():
    return '<h1>You are on the app chooser page</h1>'
