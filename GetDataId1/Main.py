from urllib import request
import uvicorn
from fastapi import FastAPI
from Request import Request
from typing import List
from MySql import GetDataId
import json

def create_app() -> FastAPI:
    app = FastAPI(title='List Data User', debug=True) # for dev only
    return app

app = create_app()

@app.post('/getDataId')
async def GetDataById(req: Request):
    result = ''
    id = req.id
    
    data = GetDataId(req)
    
    if (data):
        result = {
            "statusCode": "200",
            "statusDesc": "Success Get Data",
            "data": json.loads(data)
        }
    else:
        result = {
            "statusCode": "9001",
            "statusDesc": "Failed to get data",
            "data": [],
        }

    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7778)