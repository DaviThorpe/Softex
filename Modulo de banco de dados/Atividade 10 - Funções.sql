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

select * from clientes;

insert into clientes
(nome, dtCadastro)
values
('Pedro', '2022-09-19'),
('Ana', '2022-09-19'),
('Julio', '2022-09-19'),
('Paula', '2022-09-19'),
('Lucas', '2022-09-20');

insert into clientes
(nome, dtCadastro)
values
('Laura', '2022-12-21'),
('Leo', '2022-12-21'),
('Menó', '2022-12-21'),
('Valença', '2022-12-21'),
('Luciana', '2022-12-21');

select * from clientes;

/*A função não funciona de um modo realmente prático, precisa de algum ajuste
no momento ela irá somar todos os cadastros independete do dia*/

delimiter $$

CREATE FUNCTION fn_soma (registro int, dtCadastro date) RETURNS INT
BEGIN
	
declare Soma int;	
	SELECT count(registro) from clientes where day(dtCadastro)=day('2022-12-21')
    into Soma;
	RETURN Soma;
        
END $$

delimiter ; 

select fn_soma(registro, dtCadastro) as clientes_cad, day(dtCadastro) as dia_cad from clientes; 