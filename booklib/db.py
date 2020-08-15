import os
import mysql.connector
from flask import g
from werkzeug.local import LocalProxy

db_config = {
  'user': os.getenv('MYSQL_USER'),
  'password': os.getenv('MYSQL_PASSWORD'),
  'host': os.getenv('MYSQL_HOST'),
  'database': os.getenv('MYSQL_DBNAME'),
}

def get_db():
  if 'cnx' not in g:
    cnx = mysql.connector.connect(**db_config)
    g.cnx = cnx

  return g.cnx

cnx = LocalProxy(get_db)
