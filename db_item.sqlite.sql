-- Apaga as tabelas caso existam.

DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS owner;
DROP TABLE IF EXISTS contact;

-- Cria a tabela owner.

CREATE TABLE owner (
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    owner_name TEXT,
    owner_email TEXT,
    owner_password TEXT,
    owner_birth DATE,
    owner_status TEXT DEFAULT 'on',
    owner_field1 TEXT,
    owner_field2 TEXT
);

-- Popular a tabela owner com dados fake.

INSERT INTO owner (owner_id, owner_date, owner_name, owner_email, owner_password, owner_birth, owner_status) VALUES 
('1', '2023-09-29 10:11:12', 'Joca da Silva', 'joca@silva.com', '123', '1988-12-14', 'on'),
('2', '2023-10-15 08:30:45', 'Maria Oliveira', 'maria@oliveira.com', 'abc456', '1995-05-22', 'on'),
('3', '2023-11-02 14:20:30', 'Pedro Santos', 'pedro@santos.com', '789xyz', '1980-07-08', 'on'),
('4', '2023-11-08 18:45:22', 'Ana Souza', 'ana@souza.com', 'qwerty123', '1992-03-30', 'on'),
('5', '2023-11-13 09:05:17', 'Carlos Pereira', 'carlos@pereira.com', 'pass123', '1985-09-18', 'on'),
('6', '2023-11-20 12:40:55', 'Fernanda Costa', 'fernanda@costa.com', 'p@ssw0rd', '1998-08-05', 'on'),
('7', '2023-12-01 16:55:38', 'Ricardo Almeida', 'ricardo@almeida.com', 'a1b2c3', '1983-11-25', 'on');

-- Criação tabela item

CREATE TABLE item (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    item_name TEXT,
    item_description TEXT,
    item_location TEXT,
    item_owner INTEGER,
    item_status TEXT DEFAULT 'on',
	FOREIGN KEY (item_owner) REFERENCES owner (owner_id)
);

INSERT INTO item (item_id, item_date, item_name, item_description, item_location, item_owner, item_status) VALUES 
('1', '2023-05-12 14:15:00', 'Sapato', 'Sapato social', 'Gaveta', '1', 'on'),
('2', '2023-06-20 09:30:45', 'Bolsa', 'Bolsa de couro', 'Armário', '2', 'on'),
('3', '2023-07-05 16:45:22', 'Relógio', 'Relógio de pulso', 'Cômoda', '3', 'on'),
('4', '2023-08-15 11:05:17', 'Óculos de Sol', 'Óculos escuros', 'Prateleira', '4', 'on'),
('5', '2023-09-02 08:20:30', 'Livro', 'Romance contemporâneo', 'Estante', '5', 'on');

CREATE TABLE contact (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	date DATETIME DEFAULT CURRENT_TIMESTAMP,
	name TEXT,
	email TEXT,
	subject TEXT,
	message TEXT,
	status TEXT DEFAULT 'received'
);

-- Update tabela item

/*UPDATE item
SET item_status = 'on'
WHERE item_status = 'off';

ALTER TABLE item
DROP item_owner
*/
