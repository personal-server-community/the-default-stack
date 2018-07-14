import redis

from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api, reqparse
from flask_mail import Message, Mail
from flask_sqlalchemy import SQLAlchemy
from minio import Minio
from minio.error import (
    ResponseError,
    BucketAlreadyOwnedByYou,
    BucketAlreadyExists
)

mail = Mail()

app = Flask(__name__)
api = Api(app)


# Postfix config

app.config["MAIL_SERVER"] = "smtp"
app.config["MAIL_USERNAME"] = "user"
app.config["MAIL_PASSWORD"] = "pwd"
mail.init_app(app)

# Redis config

kvstore = redis.StrictRedis(host='kvstore', port=6379, db=0)

# Minio config

minio_client = Minio(
   'files:9000',
    access_key='AKIAIOSFODNN7EXAMPLE',
    secret_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    secure=False
)

try:
    minio_client.make_bucket("myfiles")
except BucketAlreadyOwnedByYou as err:
    print("BucketAlreadyOwnedByYou")
except BucketAlreadyExists as err:
    print("BucketAlreadyExists")
except ResponseError as err:
    raise

# Postgres config

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

engine_url = 'postgresql://postgres:password@database:5432/mydatabase2'
engine = create_engine(engine_url)
if not database_exists(engine.url):
    create_database(engine.url)
    print(database_exists(engine.url))

app.config['SQLALCHEMY_DATABASE_URI'] = engine_url
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    number = db.Column(db.Integer, unique=True, nullable=False)

db.create_all()

# Routes

class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


class KVStore(Resource):
    def get(self, key):
        return {key: kvstore.get(key)}

    def post(self, key):
        parser = reqparse.RequestParser()
        parser.add_argument("value")
        args = parser.parse_args()
        value = args["value"]
        return {key: kvstore.get(key)}


class Mailing(Resource):

    def get(self):
        msg = Message(
            "Hello",
            sender="gelinor@free.fr",
            recipients=["frank.rousseau@free.fr"]
        )
        mail.send(msg)
        return {"mail": "sent"}


class Files(Resource):

    def get(self, key):
        minio_client.fget_object("myfiles", key, "/tmp/" + key)
        return send_from_directory(directory="/tmp", filename=key)

    def post(self, key):
        file_to_save = request.files["file"]
        file_to_save.save("/tmp/" + key)
        minio_client.fput_object("myfiles", key, "/tmp/" + key)
        return {"success": True}, 201


class Users(Resource):
    def get(self):
        users = User.query.all()
        return [
            {"id": user.id, "name": user.name, "number": user.number}
            for user in users
        ]

    def post(self):
        user = User.query.order_by(User.number.desc()).first()
        number = 1
        if user is not None:
            number = user.number + 1
        user = User(
            name="User %d" % number,
            number=number
        )
        db.session.add(user)
        db.session.commit()
        return {"id": user.id, "name": user.name, "number": user.number}


api.add_resource(HelloWorld, "/")
api.add_resource(KVStore, "/kv/<key>")
api.add_resource(Mailing, "/mailing")
api.add_resource(Files, "/files/<key>")
api.add_resource(Users, "/users")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
