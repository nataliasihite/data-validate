from urllib import request
import uvicorn
from fastapi import FastAPI
from Request import Request
from typing import List
from MySql import DeleteData


def create_app() -> FastAPI:
    app = FastAPI(title='Documentation Service for Update Data User', debug=True) #for dev only
    return app

app = create_app()

@app.post('/deleteData')
async def ListUser(req: Request):
    result = ''

    try:
        DeleteData(req)
    except:
        result = {
            "statusCode": 9002,
            "statusDesc": "Failed on Delete Data."
        }
        return result

    result = {
            "statusCode": 200,
            "statusDesc": "Succes Delete Data."
        }
    
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3878)