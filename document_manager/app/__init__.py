from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecret'  # You can load from environment if needed
    app.config['UPLOAD_FOLDER'] = 'uploads'

    from .routes import routes
    app.register_blueprint(routes)

    return app
