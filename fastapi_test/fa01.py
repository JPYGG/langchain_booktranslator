import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/translation')
def test():
    print('执行接口函数')
    return 'Hello'

if __name__ == '__main__':
    # http://localhost:8000/redoc
    # http://localhost:8000/docs
    uvicorn.run(app, host='0.0.0.0', port=8000)
