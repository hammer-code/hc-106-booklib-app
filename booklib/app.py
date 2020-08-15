from flask import Flask
from .modules import author

def setup_routes(app):
  @app.route('/')
  def home():
    return 'Hi!'

def create_app():
  app = Flask(__name__)

  setup_routes(app)

  app.register_blueprint(author.bp)

  return app
