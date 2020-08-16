from flask import(
  Blueprint, render_template, request, redirect, jsonify
)
from booklib.db import cnx
from booklib.repo import BookRepo, PublisherRepo

bp = Blueprint('book', __name__, url_prefix='/books', template_folder="views")
bookRepo = BookRepo(cnx)
publisherRepo = PublisherRepo(cnx)

@bp.route('/')
def index():
  books = bookRepo.findAll()

  return render_template('book/index.html',books=books)

@bp.route('/create', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    payload = (
      request.form['title'],
      request.form['publisher_id'],
      request.form['published_at']
    )
    bookRepo.create(payload)
    return redirect('/books')

  publishers = publisherRepo.findAll()
  return render_template('book/create.html', publishers=publishers)

@bp.route('/edit/<id>', methods=('GET', 'POST'))
def edit(id):
  if request.method == 'POST':
    payload = dict(
      title=request.form['title'],
      publisher_id=request.form['publisher_id'],
      published_at=request.form['published_at']
    )
    bookRepo.update(id, payload)
    return redirect('/books')
  
  book = bookRepo.findById(id)
  publishers = publisherRepo.findAll()
  return render_template('book/edit.html', book=book, publishers=publishers)

@bp.route('/delete/<id>', methods=['POST'])
def delete(id):
  bookRepo.delete(id)
  return jsonify({ 'message': 'success '})