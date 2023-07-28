import uvicorn
from fastapi import FastAPI
import json
from Request import Request
from MySql import getService

def create_app() -> FastAPI:
    app = FastAPI(title='List Data User', debug=True) #for dev only

    return app

app = create_app()

@app.post('/getData')
async def GetData(req: Request):
    result = ''
    channel = req.channel
    
    data = getService()
    # data
    if(data) :
        result = {
            "statusCode": "200",
            "statusDesc": "Success Get Data",
            "data": json.loads(data)
        }

        print(data)

        return result
    
    else:
        result = {
            "statusCode": "9001",
            "statusDesc": "Failed get data Mysql",
            "data": [],
        }

        return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3838)

    