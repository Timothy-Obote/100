from random import randrange
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel                       

app = FastAPI()

# request Get method url: "/"

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
my_posts = [{"title": "title of post 1", "content":"content of post 2", "id": 2},{"title":"favourite foods","content": "I like pizza", "id": 2 }]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
#def create_post(payload: dict = Body(...)):

def create_posts(post: Post ):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    #print(post.published)
    #print(post.dict())
    #return {"new-post" : f"title {payload['title']} content:{payload['content']}"}
    my_posts.append(post_dict)
    return {"data": post_dict}
    #print(new_post) 
    
#title, str, content str, category, Bool published 
@app.get("/posts/{id}")
def get_post(id):
    print(id)
    post = find_post(id)
    return{"post_detail": post}
    
