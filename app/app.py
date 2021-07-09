from flask import Flask
from flask_restful import Api, Resource
import datetime
import pytz
import os

app = Flask(__name__)
api = Api(app)

class DateName(Resource):
    def get(self):
        now = datetime.datetime.now(pytz.timezone('Asia/Dubai'))
        date = (now.strftime("%d/%m/%Y %H:%M"))
        NAME = os.environ['NAME']
        PASSWORD = os.environ['PASSWORD']
        return (date + " Hello " + NAME + ", your password is " + PASSWORD) 

api.add_resource(DateName, "/name")

if __name__ == "__main__":
    app.run