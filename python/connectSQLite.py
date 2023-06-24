import sqlite3
import json
from flask import jsonify
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

@app.route('/inserircliente',methods=['POST'])
def postCliente():
    conexao = sqlite3.connect("FlaskAPI-P2P/Untitled.db")
    connection = conexao.cursor()
    paramentro_id = request.json.get('id')
    paramentro_nome = request.json.get('nome')
    paramentro_endereco = request.json.get('endereco')
    paramentro_telefone = request.json.get('telefone')
    connection.execute(f"INSERT INTO Clientes VALUES ('{paramentro_id}','{paramentro_nome}','{paramentro_endereco}','{paramentro_telefone}');")
    conexao.commit()
    connection.close()
    usuarios_json = [{
        'id': paramentro_id,
        'nome': paramentro_nome,
        'endereco': paramentro_endereco,
        'telefone': paramentro_telefone
    }]
    return json.dumps(usuarios_json)

@app.route('/inserirproduto',methods=['POST'])
def postProduto():
    conexao = sqlite3.connect("FlaskAPI-P2P/Untitled.db")
    connection = conexao.cursor()
    paramentro_id = request.json.get('id')
    paramentro_nome = request.json.get('nome')
    paramentro_preco = request.json.get('preco')
    paramentro_quantidade = request.json.get('quantidade')
    connection.execute(f"INSERT INTO Produtos VALUES ('{paramentro_id}','{paramentro_nome}','{paramentro_preco}','{paramentro_quantidade}');")
    conexao.commit()
    connection.close()
    usuarios_json = [{
        'id': paramentro_id,
        'nome': paramentro_nome,
        'endereco': paramentro_preco,
        'telefone': paramentro_quantidade
    }]
    return json.dumps(usuarios_json)

@app.route('/atualizarproduto/<id>', methods=['PATCH'])
def patchAtualizarProduto(id):
    conexao = sqlite3.connect("FlaskAPI-P2P/Untitled.db")
    connection = conexao.cursor()
    paramentro_nome = request.json.get('nome')
    paramentro_preco = request.json.get('preco')
    paramentro_quantidade = request.json.get('quantidade')
    connection.execute(f"UPDATE Produtos SET nome = '{paramentro_nome}', preco = '{paramentro_preco}', quantidade = '{paramentro_quantidade}' WHERE id = '{id}';")
    conexao.commit()
    connection.close()
    produto_json = [{
        'id': id,
        'nome': paramentro_nome,
        'preco': paramentro_preco,
        'quantidade': paramentro_quantidade
    }]
    return json.dumps(produto_json)

@app.route('/atualizarcliente/<id>', methods=['PATCH'])
def patchAtualizarCliente(id):
    conexao = sqlite3.connect("FlaskAPI-P2P/Untitled.db")
    connection = conexao.cursor()
    paramentro_nome = request.json.get('nome')
    paramentro_endereco = request.json.get('endereco')
    paramentro_telefone = request.json.get('telefone')
    connection.execute(f"UPDATE Clientes SET nome = '{paramentro_nome}', endereco = '{paramentro_endereco}', telefone = '{paramentro_telefone}' WHERE id = '{id}';")
    conexao.commit()
    connection.close()
    cliente_json = [{
        'id': id,
        'nome': paramentro_nome,
        'endereco': paramentro_endereco,
        'telefone': paramentro_telefone
    }]
    return json.dumps(cliente_json)

# Método PUT usuarios
@app.route('/usuarios', methods=['PUT'])
def updateCliente():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    paramentro_id = request.json.get('id')
    nome = request.json.get('nome')
    endereco = request.json.get('endereco')
    telefone = request.json.get('telefone')

    # Verificar se o ID do cliente é fornecido
    if not paramentro_id:
        connection.close()
        return json.dumps({'error': 'É necessário fornecer o ID do cliente para atualização.'}), 400

    # Verificar se o cliente existe antes da atualização
    connection.execute("SELECT * FROM Clientes WHERE id = ?", (paramentro_id,))
    cliente_existente = connection.fetchone()
    if not cliente_existente:
        connection.close()
        return json.dumps({'error': 'O cliente com o ID fornecido não existe.'}), 404

    # Realizar a atualização do cliente
    connection.execute("UPDATE Clientes SET nome = ?, endereco = ?, telefone = ? WHERE id = ?",
                       (nome, endereco, telefone, paramentro_id))
    conexao.commit()
    connection.close()
    return json.dumps({'message': 'Cliente atualizado com sucesso!'})

# Método DELETE para usuários
@app.route('/usuarios', methods=['DELETE'])
def deleteCliente():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    paramentro_id = request.json.get('id')

    # Verificar se o ID do cliente é fornecido
    if not paramentro_id:
        connection.close()
        return json.dumps({'error': 'É necessário fornecer o ID do cliente para exclusão.'}), 400

    # Verificar se o cliente existe antes da exclusão
    connection.execute("SELECT * FROM Clientes WHERE id = ?", (paramentro_id,))
    cliente_existente = connection.fetchone()
    if not cliente_existente:
        connection.close()
        return json.dumps({'error': 'O cliente com o ID fornecido não existe.'}), 404

    # Verificar se o cliente está associado a algum pedido
    connection.execute("SELECT * FROM Pedidos WHERE cliente_id = ?", (paramentro_id,))
    pedidos_cliente = connection.fetchall()
    if pedidos_cliente:
        connection.close()
        return json.dumps({'error': 'Não é possível excluir o cliente porque existem pedidos associados a ele.'}), 409

    # Realizar a exclusão do cliente
    connection.execute("DELETE FROM Clientes WHERE id = ?", (paramentro_id,))
    conexao.commit()
    connection.close()
    return json.dumps({'message': 'Cliente excluído com sucesso!'})


# Método CONNECT para a tabela 'Funcionarios'
@app.route('/funcionarios', methods=['CONNECT'])
def connectFuncionarios():
    conexao = sqlite3.connect("Untitled.db")
    connection = conexao.cursor()
    connection.close()
    return json.dumps({'message': 'Conexão estabelecida com sucesso!'})


if __name__ == '__main__':
    app.run(port=8002)
