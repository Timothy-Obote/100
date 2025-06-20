from random import randrange
from typing import Optional
from fastapi import FastAPI,Response,status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel                       

app = FastAPI()

# request Get method url: "/"

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
    
    
my_posts = [{"title": "title of post 1", "content":"content of post 2", "id": 1},{"title":"favourite foods","content": "I like pizza", "id": 2 }]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

#How to change default status code for a specific path operation 
@app.post("/posts", status_code=status.HTTP_201_CREATED)
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
    
    
@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail" : post}


#title, str, content str, category, Bool published 
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    #print(type(id))
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'message': f"post with id: {id} was not found"}
    return{"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #deleting post
    #find the index in the array that has the required ID
    #my_posts.pop(index)
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id:{id} does not exist")
    
    my_posts.pop(index)
    #return{'message' : 'post was succesfully deleted'}
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post:Post):
    
    #print(post)
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id:{id} does not exist")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}
    
    return{"message" : "Updated Post"}
