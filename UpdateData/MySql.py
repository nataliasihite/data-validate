from Request import Request
from bson.json_util import dumps
import mysql.connector


def UpdateData(req: Request):
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
        
        sql = "UPDATE user SET username = %s, no_rekening = %s, nama = %s, no_hp = %s, email = %s WHERE id = %s"
        val = (data["username"], data["no_rekening"], data["nama"], data["no_hp"], data["email"], data["id"])
        cursor.execute(sql, val)
        
        mydb.commit()
        
        print(cursor.rowcount, "Success Update Data.")
        
        cursor.close()
        mydb.close()
        
        return 'Success Update Data.'
        
        # return dumps(result)

    except Exception as e:
        print(e.args[0])
        return 'Failed'
