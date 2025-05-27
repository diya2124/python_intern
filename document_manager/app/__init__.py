import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecret'
    app.config['UPLOAD_FOLDER'] = 'uploads'

    os.makedirs(app.instance_path, exist_ok=True)

    from .models import init_db
    with app.app_context():
        init_db()

    from .routes import routes
    app.register_blueprint(routes)

    return app
