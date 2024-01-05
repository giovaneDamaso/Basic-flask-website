#views = routes
from flask import Blueprint

views = Blueprint('views', __name__)

#defining routes
@views.route('/')
def home():
    return "<h1>Test</h1>"