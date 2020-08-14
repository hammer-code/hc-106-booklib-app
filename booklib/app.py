from flask import Flask

def setup_routes(app):
  @app.route('/')
  def home():
    return "Hello"

def create_app():
  app = Flask(__name__)

  setup_routes(app)

  return app
