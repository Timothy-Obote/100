from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

# request Get method url: "/"

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    #rating: Optional[int] = None
    
my_posts = [{"title": "title of post 1", "content":"content of post 2", "id": 2},{"title":"favourite foods","content": "I like pizza", "id": 2 }]

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
#def create_post(payload: dict = Body(...)):
def create_posts(post: Post ):
    print(post.published)
    print(post.dict())
    #return {"new-post" : f"title {payload['title']} content:{payload['content']}"}
    return {"data": "post"}
    #print(new_post) 
    
#title, str, content str, category, Bool published 

