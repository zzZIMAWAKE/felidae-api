# app.py


from flask import Flask
from flask import request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from api import api as api_blueprint

app.register_blueprint(api_blueprint, url_prefix='/api')


from models import *


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
#
# @app.route('/category', methods=['POST'])
# def add_category():
#     #get json
#
#     Category(name, person_id, parent_id)

@app.route('/category', methods=['GET'])
def get_categories():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
