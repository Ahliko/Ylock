from flask import request
from app import app
from user.userController import LoginController, UserController
from utilities.auth import Auth
from tcp import TcpServer


auth = Auth()
tcp = TcpServer()


@app.get('/status')
@auth.middleware
def status():
    return {'status': True, 'msg': tcp.socket_to_server("", "GET", "200")}



@app.get('/lock')
@auth.middleware
def lock():
    tcp.socket_to_server("lock", "POST", "200")
    return {'status': True, 'msg': tcp.socket_to_server("", "GET", "200")}


@app.get('/unlock')
@auth.middleware
def unlock():
    tcp.socket_to_server("unlock", "POST", "200")
    return {'status': True, 'msg': tcp.socket_to_server("", "GET", "200")}


@app.post('/login')
def login():
    return LoginController().login()


@app.get('/logout')
def logOut():
    return LoginController().logOut()


@app.post('/newuser')
def newUser():
    return UserController().insertNewData()
