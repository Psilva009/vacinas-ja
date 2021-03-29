from app import environ, path, load_dotenv
import sys
import jinja2

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


