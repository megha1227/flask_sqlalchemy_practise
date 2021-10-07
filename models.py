import connection

class UserModel(connection.db.Model):
    __tablename__ = "users"

    id = connection.db.Column(connection.db.Integer, primary_key=True)
    email = connection.db.Column(connection.db.String(100), nullable=False)
    uname = connection.db.Column(connection.db.String(100), nullable=False)

    def save_to_db(self):
        connection.db.session.add(self)
        connection.db.session.commit()