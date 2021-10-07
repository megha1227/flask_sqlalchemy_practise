#exceptions will raise when the integrity is failed

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)

class Member(db.Model):
    print("HareKrishna")
    id = db.Column(db.Integer,primary_key = True)
    uniq = db.Column(db.String(50),unique = True)


@app.route("/")
def index():

    # if Member.query.filter_by(uniq="Krishna").first() != None:
    #     return "already exists!!!!"
    # krishna = Member(uniq="Krishna")
    # db.session.add(krishna)
    # db.session.commit()
    # return "DAtabase entry added"

    try:
        krishna = Member(uniq="Krishna")
        db.session.add(krishna)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()#y we do rollback ---> "https://youtu.be/P-Z1wXFW4Is?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW&t=509"
        # we do rollback , inorder to perform come back from failed state to normal state where we can execute some more db commands, if requred
            
        return "This memeber already exists"


if __name__ == "__main__":
    db.create_all()
    # app.run(debug=True)
    app.run()