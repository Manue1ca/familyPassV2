from fastapi import FastAPI
from pydantic import BaseModel

from db import checkVersion, findUser, showPasswords

app = FastAPI()

@app.get("/checkVerson")
def check_v_sql():
    return checkVersion()

class User(BaseModel):
    login:str
    password:str

@app.post("/User")
def find_user(user: User):
    res = findUser(user.login, user.password)
    if res == None:
        return "Имя пользователя или пароль не совпадают"
    else:
        return res

class findPass(BaseModel):
    login:str

@app.post("/ShowPasswords")
def show_user(findPass: findPass):
    res = showPasswords(findPass.login)
    if res == None:
        return "Пароли не найдены"
    else:
        return res