from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)

app.config.from_object('config')

from app.routes import routes