-- Inserindo dados na tabela 'Clientes'
INSERT INTO Clientes (id, nome, endereco, telefone)
VALUES (1, 'João Silva', 'Rua A, 123', '111111111'),
       (2, 'Maria Santos', 'Avenida B, 456', '222222222'),
       (3, 'Pedro Almeida', 'Rua C, 789', '333333333');

-- Inserindo dados na tabela 'Produtos'
INSERT INTO Produtos (id, nome, preco, quantidade)
VALUES (1, 'Camisa', 29.99, 50),
       (2, 'Calça', 59.99, 30),
       (3, 'Tênis', 99.99, 20);

-- Inserindo dados na tabela 'Pedidos'
INSERT INTO Pedidos (id, cliente_id, data_pedido, valor_total)
VALUES (1, 1, '2023-06-01', 100.00),
       (2, 2, '2023-06-02', 150.00),
       (3, 3, '2023-06-03', 200.00);

-- Inserindo dados na tabela 'ItensPedido'
INSERT INTO ItensPedido (id, pedido_id, produto_id, quantidade, subtotal)
VALUES (1, 1, 1, 2, 59.98),
       (2, 1, 2, 1, 59.99),
       (3, 2, 3, 1, 99.99);

-- Inserindo dados na tabela 'Estoque'
INSERT INTO Estoque (id, produto_id, quantidade)
VALUES (1, 1, 50),
       (2, 2, 30),
       (3, 3, 20);

-- Inserindo dados na tabela 'Funcionarios'
INSERT INTO Funcionarios (id, nome, cargo, salario)
VALUES (1, 'Ana Souza', 'Vendedor', 2000.00),
       (2, 'Carlos Oliveira', 'Gerente', 5000.00),
       (3, 'Mariana Costa', 'Caixa', 1500.00);

-- Inserindo dados na tabela 'Vendas'
INSERT INTO Vendas (id, cliente_id, funcionario_id, data_venda, valor_total)
VALUES (1, 1, 2, '2023-06-10', 120.00),
       (2, 2, 3, '2023-06-11', 180.00),
       (3, 3, 1, '2023-06-12', 220.00);

-- Inserindo dados na tabela 'ItensVenda'
INSERT INTO ItensVenda (id, venda_id, produto_id, quantidade, subtotal)
VALUES (1, 1, 1, 1, 29.99),
       (2, 1, 3, 1, 99.99),
       (3, 2, 2, 2, 119.98);

-- Inserindo dados na tabela 'Promocoes'
INSERT INTO Promocoes (id, produto_id, data_inicio, data_fim, desconto)
VALUES (1, 2, '2023-06-01', '2023-06-07', 0.10),
       (2, 3, '2023-06-05', '2023-06-10', 0.15),
       (3, 1, '2023-06-08', '2023-06-15', 0.20);

-- Inserindo dados na tabela 'Pagamentos'
INSERT INTO Pagamentos (id, venda_id, tipo_pagamento, valor)
VALUES (1, 1, 'Cartão de Crédito', 120.00),
       (2, 2, 'Dinheiro', 180.00),
       (3, 3, 'Cartão de Débito', 220.00);