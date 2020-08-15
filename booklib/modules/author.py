from booklib.repo import AuthorRepo
from flask import(
  Blueprint, render_template, request, redirect, jsonify
)
from werkzeug.local import LocalProxy
from booklib.db import get_db

bp = Blueprint('author', __name__, url_prefix='/authors', template_folder="views")

cnx = LocalProxy(get_db)
repo = AuthorRepo(cnx)
  
@bp.route('/')
def index():
  authors = repo.findAll()
  return render_template('author/index.html', authors=authors)

@bp.route('/create', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    data = { 'name': request.form['name'] }
    repo.create(request.form['name'])
    return redirect('/authors')
  
  return render_template('author/create.html')

@bp.route('/edit/<id>', methods=('GET', 'POST'))
def edit(id):
  if request.method == 'POST':
    name = request.form['name']
    repo.update(id, { 'name': name })
    return redirect('/authors')
  
  author = repo.findById(id)
  return render_template('author/edit.html', author=author)


@bp.route('/delete/<id>', methods=['POST'])
def delete(id):
  repo.delete(id)
  return jsonify({ 'message': 'success '})
