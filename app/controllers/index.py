from flask import Blueprint, make_response
index = Blueprint('index', __name__)

@index.route("/")
def get_index():
    return make_response(open('./app/templates/index.html').read())
    # return render_template('index.html')