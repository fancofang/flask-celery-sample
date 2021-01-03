import os
from flask import Flask
from main.configs import Config
from main.blueprints.views import test_bp

def make_celery(app):
    from main.extensions import celery
    celery.conf.update(app.config)
    
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    
    celery.Task = ContextTask
    return celery

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    
    app = Flask(__name__)
    app.config.from_object(Config)
    app.celery = make_celery(app)
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(test_bp)