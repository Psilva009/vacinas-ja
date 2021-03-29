from flask import Flask, render_template
from dotenv import load_dotenv
from os import environ, path

app = Flask(__name__)

app.config.from_object('config')

from app.routes import routes