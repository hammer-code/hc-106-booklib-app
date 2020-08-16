from .base import BaseRepo

class BookRepo(BaseRepo):
  def __init__(self, cnx):
    BaseRepo.__init__(self, cnx)

  def findAll(self, limit = 10):
    def transform (row):
      (id, title, publisher_name, published_at) = row
      return dict(id=id, title=title, publisher_name=publisher_name, published_at=published_at)

    return self.execute("SELECT b.id, b.title, p.name as publisher_name, b.published_at FROM books b JOIN publishers p WHERE b.publisher_id = p.id;")\
      .to_array(transform)

  def create(self, payload):
    (title, publisher_id, published_at) = payload
    return self.execute("INSERT INTO books (title, publisher_id, published_at) VALUES (%s,%s,%s)", (title, publisher_id, published_at))\
      .commit()

  def findById(self, id):
    return self.execute("SELECT b.id, b.title, b.publisher_id, b.published_at FROM books b WHERE id = %s", (id,))\
      .to_item(lambda row: dict(id=row[0], title=row[1], publisher_id=row[2], published_at=row[3]))

  def update(self, id, data):
    query = "UPDATE books SET "
    params, sets = [], []

    for key in data:
      sets.append("{} = %s".format(key))
      params.append(data[key])
    
    query += ", ".join(sets)
    query += " WHERE id = %s"
    params.append(id)

    return self.execute(query, tuple(params))\
      .commit()

  def delete(self, id):
    return self.execute("DELETE FROM books WHERE id = %s", (id,))\
      .commit()
