from Request import Request
from bson.json_util import dumps
import mysql.connector


def DeleteData(req: Request):
    # connect = Connection('0')
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="project@123",
            database="db_userlist"
        )
        cursor = db.cursor()
        
        data = {
            "id" : req.id
        }
        
        sql = "DELETE FROM user WHERE id = %s"
        val = (data["id"],)
        cursor.execute(sql, val)
        
        db.commit()
        
        print(cursor.rowcount, "Success Delete Data.")
        
        cursor.close()
        db.close()
        
        return 'Success Delete Data.'
        # return dumps(result)

    except Exception as e:
        print(e.args[0])
        return 'Failed'
