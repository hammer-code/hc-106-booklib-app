import mysql.connector

class BaseRepo:
  def __init__(self):
    self.cnx = mysql.connector.connect(
      user='root',
      password='password',
      host='127.0.0.1',
      database='book-lib-app'
    )

  def execute(self, query, params = None):
    self.cursor = self.cnx.cursor()
    self.cursor.execute(query, params)

    return self

  def commit(self):
    self.cnx.commit()

    return self

  def to_array(self, transform_cb):
    result = []

    for row in self.cursor:
      item = transform_cb(row)
      result.append(item)
    
    self.cursor.close()
    
    return result
