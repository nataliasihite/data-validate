import uvicorn
from fastapi import FastAPI
from Request import Request
from typing import List
from MySql import CreateData


def create_app() -> FastAPI:
    app = FastAPI(title='Documentation Service for Create Data User', debug=True) #for dev only
    return app

app = create_app()


@app.post('/createData')
async def ListUser(req: Request):
    result = ''

    try:
        CreateData(req)
    except:
        result = {
            "statusCode": 9002,
            "statusDesc": "Failed on Create Data."
        }
        return result

    result = {
            "statusCode": 200,
            "statusDesc": "Succes Create Data."
        }
    
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3738)