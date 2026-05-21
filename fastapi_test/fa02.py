import uvicorn
from fastapi import FastAPI, Body, UploadFile, File
from pydantic import Field

app = FastAPI()

@app.post('/translation', summary='调用翻译器', description='这是一个调用AI大模型的翻译器')
def test(source_language: str = Body(description='源语言', default='English'), target_language: str = Body(description='目标语言', default='Chinese'), input_file: UploadFile = File(description='选择需要翻译的PDF文件') ):
    print('执行接口函数')
    print(source_language)
    print(target_language)
    print(input_file.filename)
    print(input_file.size)
    return 'Hello'

if __name__ == '__main__':
    # http://localhost:8000/redoc
    # http://localhost:8000/docs
    uvicorn.run(app, host='0.0.0.0', port=8000)
