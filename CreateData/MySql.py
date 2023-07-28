from operator import concat
from Request import Request
from bson.json_util import dumps
import mysql.connector


def CreateData(req: Request):
    # connect = Connection('0')
    try:
        mydb = mysql.connector.connect(
              host="127.0.0.1",
              port="3306",
              user="root",
              password="project@123",
              database="db_userlist"
            )
        cursor = mydb.cursor()
        
        data = {
            "id" : req.id,
            "username" : req.username, 
            "no_rekening" : req.no_rekening,
            "nama" : req.nama,
            "no_hp" : req.no_hp,
            "email" : req.email
        }
        
        sql = "INSERT INTO user (id, username, no_rekening, nama, no_hp, email) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (data["id"], data["username"], data["no_rekening"], data["nama"], data["no_hp"], data["email"])
        cursor.execute(sql, val)
        
        mydb.commit()
        
        print(cursor.rowcount, "Success Insert Data.")
        
        cursor.close()
        mydb.close()
        
        return 'Success Insert Data.'
        # return dumps(result)

    except Exception as e:
        print(e.args[0])
        return 'Failed'
