import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):  # Estas dos lineas para comprobar que no haya ningun usuario repetido
            return {"message": "A user with that username already existd"}, 400

        #user = UserModel(data['username'], data['password'])  # La siguiente linea es como se simplifica esta
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

