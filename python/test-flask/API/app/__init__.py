from flask import Flask


app = Flask(__name__)


from app import api_only_flask
