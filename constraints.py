from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test1.db"

db = SQLAlchemy(app)


class MyTable(db.Model):
    print("HAre KRishna")
    id = db.Column(db.Integer, primary_key=True)
    # other_id = db.Column(db.Integer, primary_key=True)#compound/composite primary
    unique_col = db.Column(db.String(50),unique = True)
    not_null = db.Column(db.String(50),nullable  = False)
    # default = db.Column(db.Integer,server_default="10") donno need to explore later ,but he exaplined
    # check = db.Column(db.Integer,db.CheckConstraint("check>5"))#mysql wont suppor this

'''
practise:
>>> row = MyTable(unique_col = "Krishna", not_null=None)
db.session.add(row)
db.session.commit()
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) NOT NULL constraint failed: my_table.not_null
[SQL: INSERT INTO my_table (unique_col, not_null) VALUES (?, ?)]
[parameters: ('Krishna', None)]
(Background on this error at: https://sqlalche.me/e/14/gkpj)
'''

'''
once the exception raises while commiting, u need to roll back to perform 
another transaction with this session,issue roll back and then u can issue new transaction


sqlalchemy.exc.PendingRollbackError: This Session's transaction has been rolled back due to a previous exception during
 flush. To begin a new transaction with this Session, first issue Session.rollback(). Original exception was: (sqlite3.IntegrityError) NOT NULL constraint failed: my_table.not_null
[SQL: INSERT INTO my_table (unique_col, not_null) VALUES (?, ?)]
[parameters: ('Krishna', None)]
'''