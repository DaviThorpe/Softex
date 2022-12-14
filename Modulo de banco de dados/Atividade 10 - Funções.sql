
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

insert into clientes
(nome, dtCadastro)
values
('Laura', '2022-12-14'),
('Leo', '2022-12-14'),
('Menó', '2022-12-14'),
('Valença', '2022-12-14'),
('Luciana', '2022-12-14');

select * from clientes;

/*A função não funciona de um modo realmente prático, precisa de algum ajuste para aceitar qualquer data
no momento ela irá esta somando todos os cadastros independete do dia*/

delimiter $$

CREATE FUNCTION fn_soma (registro int, dtCadastro date) RETURNS INT
BEGIN
	
declare Soma int;
if dtCadastro = curdate() then	
	SELECT count(registro) from clientes where dtCadastro = curdate()
    into Soma;
	RETURN Soma;
    
else
	set Soma = '1';    
    RETURN Soma;
end if;
        
END $$

delimiter ; 

select fn_soma(registro, dtCadastro) as clientes_cadastrados, dtCadastro from clientes
where dtCadastro = curdate(); 