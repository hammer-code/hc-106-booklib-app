from flask import (Flask, redirect)
from .modules import (author, publisher, book)

def setup_routes(app):
  @app.route('/')
  def home():
    return redirect('/authors')

def create_app():
  app = Flask(__name__, static_folder='static')

  setup_routes(app)

  app.register_blueprint(author.bp)
  app.register_blueprint(publisher.bp)
  app.register_blueprint(book.bp)

  return app
