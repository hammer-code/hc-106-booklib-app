from flask import Flask
from .repo import AuthorRepo
from .modules import author

author_repo = AuthorRepo()

def setup_routes(app):
  @app.route('/')
  def home():
    result = author_repo.findAll()

    res = map(lambda x: x['name'], result)
    res = ', '.join(res)
    return res

def create_app():
  app = Flask(__name__)

  setup_routes(app)

  app.register_blueprint(author.bp)

  return app
