from flask import Flask

def setup_routes(app):
  @app.route('/')
  def home():
    return "Hi"

def create_app():
  app = Flask(__name__)

  setup_routes(app)

  return app
