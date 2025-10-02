-- Criação da tabela de Produtos
CREATE TABLE Produtos (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL
);

-- Inserindo registros em Produtos
INSERT INTO Produtos (nome, preco, estoque) VALUES
('Livro - Python Básico', 49.90, 10),
('Livro - Banco de Dados', 59.90, 5),
('Livro - Git e GitHub', 39.90, 8);

-- Criação da tabela de Pedidos
CREATE TABLE Pedidos (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    cliente VARCHAR(100) NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    data_pedido DATE NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);

-- Inserindo registros em Pedidos
INSERT INTO Pedidos (cliente, id_produto, quantidade, data_pedido) VALUES
('João Silva', 1, 2, '2025-10-01'),
('Maria Souza', 2, 1, '2025-10-02'),
('Carlos Lima', 3, 3, '2025-10-02');
