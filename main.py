from typing import Union
from fastapi import FastAPI

from db import checkVersion, findUser

app = FastAPI()

@app.get("/CheckVerson")
def checkVSQL():
    return checkVersion()

@app.post("/GetUser/")
async def getUser(login:str, password:str):
    return findUser()

