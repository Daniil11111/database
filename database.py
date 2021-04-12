import sqlite3
import random
global db
global cr
db = sqlite3.connect('server.db')
cr = db.cursor()
cr.execute('''CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
    )''')
db.commit()
def reg():
    user_login = input('login: ')
    user_password = input('password: ')
    user_cash = 1000
    cr.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if cr.fetchone() == None:
        cr.execute("INSERT INTO users VALUES (?,?,?)",(user_login,user_password,user_cash))
        db.commit()
    else:
        print('данный логин уже используется!')
    for user in cr.execute('SELECT * FROM users'):
        print(user)
def log():
    user_lo=input('логин: ')
    user_pa=input('пароль: ')
    cr.execute(f'SELECT login FROM users WHERE login = "{user_lo}"')
    if cr.fetchone() != None:
        pass
    else:
        reg()
    cr.execute(f'SELECT password FROM users WHERE password = "{user_lo}"')
    if cr.fetchone() != None:
        cr.execute(f'SELECT cash FROM users WHERE login = "{user_lo}"')
        aaa = cr.fetchone()[0]
        cr.execute(f'UPDATE users SET cash = {int(aaa)-100} WHERE login = {user_lo} ')
        db.commit()
        a = random.randint(1,2)
        if a == 1:
            cr.execute(f'UPDATE users SET cash = {int(aaa)+1000} WHERE login = {user_lo} ')
            db.commit()
def check():
    for i in cr.execute('SELECT * FROM users'):
        print(i)
def menu():
    log()
    check()
menu()
input()