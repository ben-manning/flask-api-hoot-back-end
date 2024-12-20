from flask import Flask, jsonify, request, g
from flask_cors import CORS
from dotenv import load_dotenv
import os
import jwt
import psycopg2, psycopg2.extras
import bcrypt
from auth_middleware import token_required
from auth_blueprint import authentication_blueprint
from hoots_blueprint import hoots_blueprint
from comments_blueprint import comments_blueprint

load_dotenv()

app = Flask(__name__)

CORS(app)

app.register_blueprint(authentication_blueprint)
app.register_blueprint(hoots_blueprint)
app.register_blueprint(comments_blueprint)

if __name__ == '__main__':
  app.run()