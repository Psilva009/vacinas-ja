from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

app.config.from_object('config')

from app.routes import routes