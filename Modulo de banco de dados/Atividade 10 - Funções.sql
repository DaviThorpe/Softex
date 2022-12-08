create database loja;
use loja;

create table clientes(
nome varchar (30),
reg int,
dia varchar(10)
);

insert into clientes
(nome, reg, dia)
values
('Pedro', '1', '2022-09-19'),
('Ana', '1', '2022-09-19'),
('Julio', '1', '2022-09-19'),
('Paula', '1', '2022-09-19'),
('Lucas', '1', '2022-09-20');

select * from clientes;


create function soma_cli(a int)
returns int 
return sum(a);

select sum(clientes.reg) from clientes;



drop table clientes;