from flask import (Flask, redirect)
from .modules import author

def setup_routes(app):
  @app.route('/')
  def home():
    return redirect('/authors')

def create_app():
  app = Flask(__name__, static_folder='static')

  setup_routes(app)

  app.register_blueprint(author.bp)

  return app
