from flask import Flask

# setting up flask aplication
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'

    return app
