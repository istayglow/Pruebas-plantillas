from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login/login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')

@app.route('/registerUser')
def registerUser():
    return render_template('login/registerUser.html')

@app.route('/registroEmpleado')
def registroEmpleado():
    return render_template('dashboard/empleados/registroEmpleado0.html')

@app.route('/registroCliente')
def registroCliente():
    return render_template('dashboard/clientes/registroCliente.html')

@app.route('/nuevoPedido')
def nuevoPedido():
    return render_template('dashboard/pedidos/nuevoPedido.html')

@app.route('/perfil')
def perfil():
    return render_template('dashboard/perfil/perfil.html')
