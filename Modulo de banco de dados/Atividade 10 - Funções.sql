/* 
Crie uma função que some todos os clientes cadastrados em uma loja durante um dia.
*/

create database loja;
use loja;

create table clientes(
nome varchar (30),
registro int not null auto_increment,
dtCadastro date,
primary key (registro));

insert into clientes
(nome, dtCadastro)
values
('Pedro', '2022-09-19'),
('Ana', '2022-09-19'),
('Julio', '2022-09-19'),
('Paula', '2022-09-19'),
('Lucas', '2022-09-20');

select * from clientes;

delimiter $$

CREATE FUNCTION fn_soma () RETURNS INT
BEGIN
	
    declare Soma, Retorno int;
    
    SELECT COUNT(registro) as cadastros_dia , dtCadastro into Soma 
	from clientes;
    
	RETURN Soma;
    
END $$

delimiter ; 

select`loja`.`fn_soma`();