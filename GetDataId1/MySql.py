from Request import Request
from bson.json_util import dumps
import mysql.connector

def GetDataId(req: Request):
    try:
        data = {
            "id": req.id
        }
        
        db = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="project@123",
            database="db_userlist"
        )
        
        cursor = db.cursor()
        sql = "SELECT * FROM user WHERE id = %s"
        val = (data["id"],)
        cursor.execute(sql, val)
        
        result = cursor.fetchall()
        
        data_list = []
        for row in result:
            data_dict = {
                "id": row[0],
                "username": row[1],
                "no_rekening": row[2],
                "nama": row[3],
                "no_hp": row[4],
                "email": row[5]
            }
            data_list.append(data_dict)
        
        cursor.close()
        db.close()
        
        return dumps(data_list)

    except Exception as e:
        print(e.args[0])
        return 'Failed'