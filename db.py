import psycopg2
from configDB import host,user,password,db_name


conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)


def checkVersion():
    try:
        with conn.cursor() as curs:
            curs.execute(
                "SELECT version();"
            )
            return (f'Postgress version:{curs.fetchone()}')
    except Exception as _ex:
        return ("[INFO] Error while working with PostgreSQL", _ex)


def findUser(l, p):
    try:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM "KeyPass"."users" WHERE login = %s AND password = %s',(l,p))
            for res  in curs.fetchall():
                return res
    except Exception as _ex:
        return ("[INFO] Error while working with PostgreSQL", _ex)

def addPassword(login, nameservis, loginservis, passservis):
    try:
        with conn.cursor() as curs:
            curs.execute('')
    except Exception as _ex:
        return ("[INFO] Ошибка при добавлении пароля у пользователя", _ex)

def showPasswords(login):
    response = []
    try:
        with conn.cursor() as curs:
            curs.execute('select * from "KeyPass".users JOIN "KeyPass".passwords ON users.id = passwords.user_id where username=%s',(login))
            for res  in curs.fetchall():
                response.append(res)
            return response
    except Exception as _ex:
        return ("[INFO] Ошибка при получении паролей у пользователя", _ex)