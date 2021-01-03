from flask.blueprints import Blueprint
from flask import render_template
from tasks import add_together

test_bp = Blueprint("task",__name__)

@test_bp.route('/')
def index():
    return render_template('index.html')

@test_bp.route('/test_celerty')
def test_celery():
    result = add_together.apply_async(args=[23, 42])
    render_result = str(result.get())
    return render_result