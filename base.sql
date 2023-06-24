-- Criação da tabela 'Clientes'
CREATE TABLE Clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(100),
    telefone VARCHAR(15)
);

-- Criação da tabela 'Produtos'
CREATE TABLE Produtos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10, 2),
    quantidade INT
);

-- Criação da tabela 'Pedidos'
CREATE TABLE Pedidos (
    id INT PRIMARY KEY,
    cliente_id INT,
    data_pedido DATE,
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);

-- Criação da tabela 'ItensPedido'
CREATE TABLE ItensPedido (
    id INT PRIMARY KEY,
    pedido_id INT,
    produto_id INT,
    quantidade INT,
    subtotal DECIMAL(10, 2),
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);

-- Criação da tabela 'Estoque'
CREATE TABLE Estoque (
    id INT PRIMARY KEY,
    produto_id INT,
    quantidade INT,
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);

-- Criação da tabela 'Funcionarios'
CREATE TABLE Funcionarios (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(50),
    salario DECIMAL(10, 2)
);

-- Criação da tabela 'Vendas'
CREATE TABLE Vendas (
    id INT PRIMARY KEY,
    cliente_id INT,
    funcionario_id INT,
    data_venda DATE,
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (funcionario_id) REFERENCES Funcionarios(id)
);

-- Criação da tabela 'ItensVenda'
CREATE TABLE ItensVenda (
    id INT PRIMARY KEY,
    venda_id INT,
    produto_id INT,
    quantidade INT,
    subtotal DECIMAL(10, 2),
    FOREIGN KEY (venda_id) REFERENCES Vendas(id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);

-- Criação da tabela 'Promocoes'
CREATE TABLE Promocoes (
    id INT PRIMARY KEY,
    produto_id INT,
    data_inicio DATE,
    data_fim DATE,
    desconto DECIMAL(5, 2),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);

-- Criação da tabela 'Pagamentos'
CREATE TABLE Pagamentos (
    id INT PRIMARY KEY,
    venda_id INT,
    tipo_pagamento VARCHAR(50),
    valor DECIMAL(10, 2),
    FOREIGN KEY (venda_id) REFERENCES Vendas(id)
);
