import os

from fastapi import FastAPI, Form

import connectors

app = FastAPI()

TOKEN = os.environ.get("GITLAB_TOKEN")


@app.get("/")
async def root():
    return {"users": []}


@app.get("/group")
async def get_users():
    return {"users": []}


@app.put("/group/add")
async def add_user(user: str = Form()):
    return {"users": []}


@app.delete("/group/remove")
async def delete_user(user: str):
    return {"users": []}


@app.get("/me")
async def get_logged_user():
    gitlab = connectors.Gitlab(TOKEN)
    return {"user": gitlab.logged_user}
