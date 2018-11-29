/*
TABLES:

tbl_acesso
tbl_campanhas
tbl_carrinho_produtos
tbl_cliente_fisico
tbl_cliente_juridico
tbl_clientejxclientef
tbl_movimento
tbl_pedidos
tbl_prazo_level
tbl_produtos
tbl_produtos_campanha
tbl_regra_prazos
tbl_usuarios
*/
show tables;

use credit_management;

select * from tbl_cliente_juridico;

/* Query que retorna os pedidos em aberto */
SELECT * FROM tbl_pedidos p
JOIN tbl_carrinho_produtos cp
ON p.ped_id = cp.ped_id
WHERE p.ped_id NOT IN (
	SELECT ped_id FROM tbl_movimento
);

/* Query que retorna os pedidos já pagos */
SELECT * FROM tbl_pedidos p
JOIN tbl_carrinho_produtos cp
ON p.ped_id = cp.ped_id
WHERE p.ped_id IN (
	SELECT ped_id FROM tbl_movimento
);

