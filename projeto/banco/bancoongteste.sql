-- Criação do Banco de Dados
CREATE DATABASE cafeteria;
USE cafeteria;

-- Tabela de Produtos
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(6,2) NOT NULL
);

-- Tabela de Pedidos
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    data_pedido DATE NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES produtos(id)
);

-- Inserindo produtos
INSERT INTO produtos (nome, preco) VALUES 
('Café Expresso', 5.00),
('Cappuccino', 7.50),
('Pão de Queijo', 4.00);

-- Inserindo pedidos
INSERT INTO pedidos (id_produto, quantidade, data_pedido) VALUES
(1, 2, '2025-10-02'),
(2, 1, '2025-10-02'),
(3, 3, '2025-10-01');

