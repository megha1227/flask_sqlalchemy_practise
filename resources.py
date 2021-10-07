from flask_restful import reqparse, Resource

parse_post_arguments = reqparse.RequestParser()
# parse_post_arguments.add_argument('uname', type=str, help='this field cant be blank', required=True)
# parse_post_arguments.add_argument('email', type=str, help='this field cant be blank', required=True)


class UserRegistration(Resource):

    def post(self):
        data = parse_post_arguments.parse_args()
        print(data)
        import models
        new_user = models.UserModel(
            uname="radhe",
            email="123@yahoo.com")
        print(new_user)
        new_user.save_to_db()
        return {"message": "cool"}
