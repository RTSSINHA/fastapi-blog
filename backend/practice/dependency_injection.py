from fastapi import FastAPI, Depends, HTTPException, status

blogs = {
    "1": "First Blog",
    "2": "Second Blog",
    "3": "Third Blog"
}

users = {
    "1": "Ritesh",
    "8": "Rajesh",
    "9": "Arpita"
}

app = FastAPI(title="My First Blog")

def get_blog_or_404(id: str):
    blog = blogs.get(id)
    if not blog:
        raise HTTPException(detail=f"Blog with id {id} doesn't exist!", 
                            status_code=status.HTTP_404_NOT_FOUND)
    return blog

class GetObjectOr404:

    def __init__(self, model):
        self.model = model
    
    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(detail=f"Object with id {id} is not available!",
                                status_code=status.HTTP_404_NOT_FOUND)
        return obj
    
blogObject = GetObjectOr404(blogs)
userObject = GetObjectOr404(users)



@app.get("/blogs/{id}")
def get_blog_name(blog_name: str = Depends(blogObject)) -> str:
    return blog_name

@app.get("/users/{id}")
def get_user_name(username: str = Depends(userObject)) -> str:
    return username

