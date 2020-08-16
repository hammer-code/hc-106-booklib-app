from flask import(
  Blueprint, render_template, request, redirect, jsonify
)
from booklib.db import cnx
from booklib.repo.publisher import PublisherRepo

bp = Blueprint('publisher', __name__, url_prefix='/publishers', template_folder="views")
repo = PublisherRepo(cnx)

@bp.route('/')
def index():
  publishers = repo.findAll()

  return render_template('publisher/index.html',publishers=publishers)

@bp.route('/create', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    data = { 'name': request.form['name'] }
    repo.create(request.form['name'])
    return redirect('/publishers')
  
  return render_template('publisher/create.html')

@bp.route('/edit/<id>', methods=('GET', 'POST'))
def edit(id):
  if request.method == 'POST':
    name = request.form['name']
    repo.update(id, { 'name': name })
    return redirect('/publishers')
  
  publisher = repo.findById(id)
  return render_template('publisher/edit.html', publisher=publisher)


@bp.route('/delete/<id>', methods=['POST'])
def delete(id):
  repo.delete(id)
  return jsonify({ 'message': 'success '})