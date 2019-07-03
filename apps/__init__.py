__all__ = ['blueprint_requests', 'outcome_injector', 'transition_plans']

from apps.outcome_injector.routes import mod
from apps.blueprint_requests.routes import mod
from apps.transition_plans.routes import mod
from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'OurLittleSecret'


app.register_blueprint(blueprint_requests.routes.mod, url_prefix='/blueprints')
app.register_blueprint(outcome_injector.routes.mod, url_prefix='/outcomes')
app.register_blueprint(transition_plans.routes.mod, url_prefix='/transitions')


@app.route('/')
def index():
    return render_template('index.html')
