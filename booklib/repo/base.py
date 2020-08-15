class BaseRepo:
  def __init__(self, cnx):
    self.cnx = cnx

  def execute(self, query, params = None):
    self.cursor = self.cnx.cursor()
    self.cursor.execute(query, params)

    return self

  def commit(self):
    self.cnx.commit()

    return self
  
  def to_item(self, transform_cb):
    row = self.cursor.fetchone()

    self.cursor.close()

    return transform_cb(row)

  def to_array(self, transform_cb):
    result = []

    for row in self.cursor:
      item = transform_cb(row)
      result.append(item)
    
    self.cursor.close()
    
    return result
