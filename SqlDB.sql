create database prueba;
use prueba;

create table productos(
	id_prod int auto_increment primary key,
    nombre varchar(50),
    provedor varchar(50)
    
);

create table provedor(
	Id_prov int auto_increment primary key,
    nombre varchar(50),
    email varchar(50)
    
);

INSERT INTO provedor (nombre, email) VALUES
('Proveedor A', 'contactoA@email.com'),
('Proveedor B', 'contactoB@email.com'),id_prodnombreId_prov
('Proveedor C', 'contactoC@email.com'),
('Proveedor D', 'contactoD@email.com'),
('Proveedor E', 'contactoE@email.com'),
('Proveedor F', 'contactoF@email.com'),
('Proveedor G', 'contactoG@email.com'),
('Proveedor H', 'contactoH@email.com'),
('Proveedor I', 'contactoI@email.com'),
('Proveedor J', 'contactoJ@email.com');

INSERT INTO productos (nombre, provedor) VALUES
('Laptop', 'Proveedor A'),
('Mouse', 'Proveedor B'),
('Teclado', 'Proveedor C'),
('Monitor', 'Proveedor D'),
('Impresora', 'Proveedor E'),
('Tablet', 'Proveedor F'),
('Smartphone', 'Proveedor G'),
('Cámara', 'Proveedor H'),
('Auriculares', 'Proveedor I'),
('Disco Duro', 'Proveedor J');

SELECT User, Host FROM mysql.user;
