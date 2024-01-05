#views = routes
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#defining routes
@views.route('/')
def home():
    return render_template("home.html")