from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

# Flask-RESTful initialize
api = Api(app)


class UserList(Resource):

    def get(self):

        return {
            "message": "Get All Users"
        }

    def post(self):

        return {
            "message": "Create User"
        }


class UserDetail(Resource):

    def get(self, user_id):

        return {
            "message": f"Get User {user_id}"
        }

    def put(self, user_id):

        return {
            "message": f"Update User {user_id}"
        }

    def delete(self, user_id):

        return {
            "message": f"Delete User {user_id}"
        }


# Register Resources
api.add_resource(
    UserList,
    '/users'
)

api.add_resource(
    UserDetail,
    '/users/<int:user_id>'
)


if __name__ == "__main__":
    app.run(debug=True)