import uvicorn
import os
import urllib
from bson.json_util import dumps
from bson.objectid import ObjectId
import mysql.connector
from flask import Flask, jsonify


app = Flask(__name__)

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="3306",
  user="root",
  password="project@123",
  database="db_userlist"
)

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM user WHERE id = %s", (id,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        user = {
            'id': result[0],
            'username': result[1],
            'no_rekening': result[2],
            'nama': result[3],
            'no_hp': result[4],
            'email': result[5],
        }
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404
    


if __name__ == '__main__':
    app.run()


