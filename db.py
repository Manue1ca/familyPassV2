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


def findUser(l,p):
    try:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM "KeyPass"."Users" WHERE login = 'admin' AND password = 'admin'',(l,p))
            return (f'Postgress version:{curs.fetchall()}')
    except Exception as _ex:
        return ("[INFO] Error while working with PostgreSQL", _ex)


print(findUser("admin",'admin'))