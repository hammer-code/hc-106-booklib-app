from .base import BaseRepo

class AuthorRepo(BaseRepo):
  def __init__(self, cnx):
    BaseRepo.__init__(self, cnx)

  def findAll(self, limit = 10):
    def transform (row):
      (id, name) = row
      return { 'id': id, 'name': name }

    return self.execute("SELECT * from authors")\
      .to_array(transform)

  def create(self, name):
    return self.execute("INSERT INTO authors (name) VALUES (%s)", (name,))\
      .commit()

  def findById(self, id):
    return self.execute("SELECT * FROM authors WHERE id = %s", (id,))\
      .to_item(lambda row: dict(id=row[0], name=row[1]))

  def update(self, id, data):
    query = "UPDATE authors SET "
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
    return self.execute("DELETE FROM authors WHERE id = %s", (id,))\
      .commit()
