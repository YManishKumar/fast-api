from fastapi import FastAPI

app = FastAPI()


@app.get('/bb')
def read_root():
    return {"message": "Hello, World!"}