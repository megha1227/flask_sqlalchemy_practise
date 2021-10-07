from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ung.db'
app.config[' SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "some-secret-key"

db = SQLAlchemy(app)

import resources

api.add_resource(resources.UserRegistration, '/registration')

@app.route("/")
def home():
    return "radhe"

@app.before_first_request
def create_tables():
    app.logger.info("before_first_request")
    db.create_all()  # db.create_all() method will create all necessary tables for us.


if __name__ == "__main__":
    app.run(debug=True)
