from fastapi import  FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class BlogModal(BaseModel):
    title: str
    name: str
    published: bool


def check():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}



@app.get("/blogs")
def getBlog(limit=10,published:bool=True,sort:Optional[str] = None):
    if published:
        return {"message": f"Blog with limit {limit}"}
    else:
        return {"message": f"Blog with limit {limit} and not published"}
    



@app.post("/blog")
def createBlog(req :BlogModal):
    return {"messgae":"Blog Created Sucessfully!!","data":req}    