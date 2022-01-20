from flask import Flask


def create_app():
     app = Flask(__name__)
     app.conf['SECRET_KEY'] = 'sfjftyujhgyj stugyyd'

     return app