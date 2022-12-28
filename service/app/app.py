from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return {"users": []}

@app.put("/users")
async def add_user(user: str = Form()):
    return {"users": []}

@app.delete("/users")
async def delete_user(user: str):
    return {"users": []}

@app.get("/me")
async def get_logged_user():
    return {"user": ""}
