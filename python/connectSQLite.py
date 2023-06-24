import sqlite3
import json
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def home():
    homeapi = {
        'mensagem':'Introdução a API no 1 P2P',
        'comandos':{
            'clientes':'/usuarios',
            'produtos':'/produtos',
            'pedidos':'/pedidos',
            'clientesporid':'/usuariosporid',
            'estoque':'/estoque',
            'funcionarios':'/funcionarios',
            'vendas':'/vendas',
            'funcionariosporid':'/funcionariosporid',
            'pagamentos':'/pagamentos',
            'promocoes':'/promocoes'
        }
    }
    return json.dumps(homeapi)

@app.route('/usuarios',methods=['GET'])
def getClientes():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    tabelas = connection.execute("SELECT * FROM Clientes;")
    usuarios = tabelas.fetchall()
    connection.close()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario[0],
            'nome': usuario[1],
            'endereco': usuario[2],
            'telefone':usuario[3]
        }
        usuarios_json.append(usuario_json)   
    return json.dumps(usuarios_json)

@app.route('/produtos',methods=['GET'])
def getProdutos():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    tabelas = connection.execute("SELECT * FROM Produtos;")
    usuarios = tabelas.fetchall()
    connection.close()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario[0],
            'nome': usuario[1],
            'preco': usuario[2],
            'quantidade':usuario[3]
        }
        usuarios_json.append(usuario_json)   
    return json.dumps(usuarios_json)

@app.route('/pedidos',methods=['GET'])
def getPedidos():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    tabelas = connection.execute("SELECT * FROM Pedidos;")
    usuarios = tabelas.fetchall()
    connection.close()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario[0],
            'cliente_id': usuario[1],
            'data_pedido': usuario[2],
            'valor_total':usuario[3]
        }
        usuarios_json.append(usuario_json)   
    return json.dumps(usuarios_json)

@app.route('/usuariosporid', methods=['POST'])
def getClientesPorId():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    paramentro_id = request.json.get('id')
    if paramentro_id:
        tabelas = connection.execute(f"SELECT * FROM Clientes WHERE id = {paramentro_id};")
    else:
        tabelas = connection.execute("SELECT * FROM Clientes;")
    usuarios = tabelas.fetchall()
    connection.close()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario[0],
            'nome': usuario[1],
            'endereco': usuario[2],
            'telefone': usuario[3]
        }
        usuarios_json.append(usuario_json)
    return json.dumps(usuarios_json)

@app.route('/estoque',methods=['GET'])
def getEstoque():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    tabelas = connection.execute("SELECT * FROM Estoque;")
    usuarios = tabelas.fetchall()
    connection.close()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario[0],
            'produto_id': usuario[1],
            'quantidade': usuario[2]            
        }
        usuarios_json.append(usuario_json)   
    return json.dumps(usuarios_json)

@app.route('/funcionarios',methods=['GET'])
def getFuncionario():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    tabelas = connection.execute("SELECT * FROM Funcionarios;")
    usuarios = tabelas.fetchall()
    connection.close()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario[0],
            'nome': usuario[1],
            'cargo': usuario[2],
            'salario':usuario[3]
        }
        usuarios_json.append(usuario_json)   
    return json.dumps(usuarios_json)

@app.route('/vendas',methods=['GET'])
def getVendas():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    tabelas = connection.execute("SELECT * FROM Vendas;")
    usuarios = tabelas.fetchall()
    connection.close()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario[0],
            'cliente_id': usuario[1],
            'funcionario_id': usuario[2],
            'data_venda':usuario[3],
            'valor_total':usuario[4]
        }
        usuarios_json.append(usuario_json)   
    return json.dumps(usuarios_json)

@app.route('/funcionariosporid', methods=['POST'])
def getFuncionariosPorId():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    paramentro_id = request.json.get('id')
    if paramentro_id:
        tabelas = connection.execute(f"SELECT * FROM Funcionarios WHERE id = {paramentro_id}")
    else:
        tabelas = connection.execute("SELECT * FROM Funcionarios;")
    usuarios = tabelas.fetchall()
    connection.close()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario[0],
            'nome': usuario[1],
            'cargo': usuario[2],
            'salario':usuario[3]
        }
        usuarios_json.append(usuario_json)
    return json.dumps(usuarios_json)

@app.route('/promocoes',methods=['GET'])
def getPromocoes():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    tabelas = connection.execute("SELECT * FROM Promocoes;")
    usuarios = tabelas.fetchall()
    connection.close()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario[0],
            'produto_id': usuario[1],
            'data_inicio': usuario[2],
            'data_fim':usuario[3],
            'desconto':usuario[4]
        }
        usuarios_json.append(usuario_json)   
    return json.dumps(usuarios_json)

@app.route('/pagamentos',methods=['GET'])
def getPagamentos():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    tabelas = connection.execute("SELECT * FROM Pagamentos;")
    usuarios = tabelas.fetchall()
    connection.close()
    usuarios_json = []
    for usuario in usuarios:
        usuario_json = {
            'id': usuario[0],
            'venda_id': usuario[1],
            'tipo_pagamento': usuario[2],
            'valor':usuario[3]
        }
        usuarios_json.append(usuario_json)   
    return json.dumps(usuarios_json)

if __name__ == '__main__':
    app.run(port=8002)
