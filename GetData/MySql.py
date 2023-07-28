
import os
import urllib
from bson.json_util import dumps
import mysql.connector
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="3306",
  user="root",
  password="project@123",
  database="db_userlist"
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM user")
result = cursor.fetchall()

# for x in result:
#   print(x)

def getService():
  try:
    mydata = result
    # print(mydata)
    return dumps(mydata)
  
  except Exception as e:
    print(e.args[0])
    return 'Failed'


