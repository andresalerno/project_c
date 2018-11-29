/*
	Regras para padronização:
		* Foreign keys => fk + <nome_tabela_atual> + <nome_tabela_referencia> + <tipo_coluna (id por exemplo)>
			Obs: Caso mesmo assim repita o nome, a coluna de nome diferente da tabela referenciada precisa ter seu nome previamente citado na construção do nome da chave.
		* Primary key => pk + <nome_primeira_chave> + <nome_segunda_chave> + <tipo_coluna (id por exemplo)>
			Obs: Caso tenha mais chaves acrescentá-las uma após a outra e no final colocar tipo da coluna (id por exemplo)
*/

DROP DATABASE credit_management;

/* Criação e utilização do banco de dados */
CREATE DATABASE credit_management;
USE credit_management;

CREATE TABLE tbl_prazo_level (
	prl_id int(1) primary key unique,
	acc_descricao varchar(100)
);

/* Tabela de controle de niveis de acesso/responsabilidades */
CREATE TABLE tbl_acesso (
	acc_id int(1) primary key unique,
	acc_descricao varchar(100),
	acc_limite_desconto int,
	prl_id int(1),

	CONSTRAINT fkAccPrlId FOREIGN KEY (prl_id)
	REFERENCES tbl_prazo_level (prl_id)
);

/* Tabela do cadastro de usuarios */
CREATE TABLE tbl_usuarios (
	usu_id int primary key auto_increment unique,
	usu_nome_completo varchar(150),
	
	acc_id int(1), /* Chave estrangeira para a tabela tbl_acesso que dita o nivel de acesso de cada usuario */
	usu_email varchar(100),
	usu_senha varchar(100),

	CONSTRAINT fkUsuAccId FOREIGN KEY (acc_id)
	REFERENCES tbl_acesso(acc_id)
);

/* Tabela intermediaria que une os dois clientes: Pessoa juridica e pessoa fisica */
CREATE TABLE tbl_clientejxclientef (
	clijxf_id int primary key auto_increment,
	isQualified int(1) /* 0- Não qualificada | 1- Qualificada */
);

/* Tabela de clientes (PESSOA FISICA) */
CREATE TABLE tbl_cliente_fisico (
	clif_cpf varchar(11) primary key unique,
	clif_nome_completo varchar(150),
	clif_data_nascimento date,
	clif_estado_civil varchar(30),
	clif_cep varchar(8),
	clif_telefone varchar(11),
	clif_grupo_economico varchar(1),
	clif_email varchar(100),

	usu_id int, /* ID do vendedor desse cliente */
	clijxf_id int,

	CONSTRAINT fkClifUsuId FOREIGN KEY (usu_id)
	REFERENCES tbl_usuarios(usu_id),
	CONSTRAINT fkClifClijxfId FOREIGN KEY (clijxf_id)
	REFERENCES tbl_clientejxclientef (clijxf_id)
);

/* Tabela de clientes (PESSOA JURIDICA) */
CREATE TABLE tbl_cliente_juridico (
	clij_cnpj varchar(14) primary key unique,
	clij_nome varchar(250),
	clij_razao_social varchar(250),
	clij_nome_fantasia varchar(250),
	clifj_status_empresa varchar(50),
	clij_data_fundacao date,
	clij_email varchar(150),
	clij_telefone varchar(150),
	clij_cep varchar(100),
	clij_cidade varchar(150),
	clij_bairro varchar(100),
	clij_endereco_numero varchar(10),
	clij_endereco varchar(100),
	clij_pais varchar(100),
	clij_complemento varchar(100),
	clij_uf varchar(100),

  	usu_id int, /* ID do vendedor desse cliente */
	clijxf_id int,

	CONSTRAINT fkClijUsuId FOREIGN KEY (usu_id)
	REFERENCES tbl_usuarios(usu_id),
	CONSTRAINT fkClijClijxfId FOREIGN KEY (clijxf_id)
	REFERENCES tbl_clientejxclientef (clijxf_id)
);

/* Tabela de produtos */
CREATE TABLE tbl_produtos (
	prod_id int primary key auto_increment,
	prod_nome varchar(256),
	prod_valor_unitario double(8,2),
	prod_prazo int
);

ALTER TABLE tbl_produtos
ADD COLUMN prod_imagem varchar(256);

/* Tabela de campanha */
CREATE TABLE tbl_campanhas (
	camp_id int primary key auto_increment,
	camp_nome varchar(200),
	camp_desconto int,
	camp_data_incio date,
	camp_data_termino date
);

/* Tabela intermediaria que une a campanha e os produtos atrelados a ela */
CREATE TABLE tbl_produtos_campanha (
	prca_id int primary key auto_increment,
	
	prod_id int, /* ID do produto na campanha */
	camp_id int, /* ID da campanha */
	
	CONSTRAINT fkPrcaProdId FOREIGN KEY (prod_id)
	REFERENCES tbl_produtos (prod_id),
	CONSTRAINT fkPrcaCampId FOREIGN KEY (camp_id)
	REFERENCES tbl_campanhas (camp_id)
);

/* Tabela de pedidos */
CREATE TABLE tbl_pedidos (
	ped_id int auto_increment primary key,
	ped_status int, /* Flag de status: 0- Rejeitado | 1- Aprovado | 2- Aguardando aprovação */
	ped_valor_total double(8,2), /* Valor total do pedido */
	ped_prazo int, /* Prazo maximo do pedido */
	ped_datahora varchar(30),

	classificacao_data date, /* Data da aprovação ou rejeição do pedido */
	classificacao_descricao varchar(300), /* Descricao da aprovação ou rejeição do pedido */
	classificacao_id int, /* Id de quem aprovou ou rejeitou o pedido */
	
	usu_id int, /* Id de quem fez o pedido */
	clijxf_id int, /* Id do cliente */

	CONSTRAINT fkPedUsuIdClass FOREIGN KEY (classificacao_id)
	REFERENCES tbl_usuarios(usu_id),
	CONSTRAINT fkPedUsuId FOREIGN KEY (usu_id)
	REFERENCES tbl_usuarios(usu_id),
	CONSTRAINT fkPedClijxfId FOREIGN KEY (clijxf_id)
	REFERENCES tbl_clientejxclientef(clijxf_id)
);
/* Tabela de carrinho de produtos nos pedidos */
CREATE TABLE tbl_carrinho_produtos (	
	quantidade int, /* Quantidade do produto requerido */

	ped_id int, /* ID do pedido feito */
	prod_id int, /* ID do produto requerido */
	
	CONSTRAINT fkCarprodPedId FOREIGN KEY (ped_id)
	REFERENCES tbl_pedidos(ped_id),
    CONSTRAINT fkCarprodProdId FOREIGN KEY (prod_id)
    REFERENCES tbl_produtos(prod_id),

	CONSTRAINT pkPedProdId PRIMARY KEY (ped_id, prod_id)
);

/* Tabela de status do pagamento do pedido */
CREATE TABLE tbl_regra_prazos (
	rpz_id int(1) primary key unique,
	rpz_status_desc varchar(100)
);

/* Tabela onde contem as informações dos pedidos já pagos e finalizados */
CREATE TABLE tbl_movimento (
	mov_id int primary key auto_increment,

	cod_trasacao varchar(256), /* ped_id + cnpj/cpf + ped_datahora */
	ped_id int, /* Id do pedido */
	clijxf_id int, /* Id do cliente */
	usu_id int, /* Id do vendedor que fez o pedido */
	rpz_id int, /* Id do status do pagamento */

	CONSTRAINT fkMovPedId FOREIGN KEY (ped_id)
	REFERENCES tbl_pedidos(ped_id),
	CONSTRAINT fkMovClijxfId FOREIGN KEY (clijxf_id)
	REFERENCES tbl_clientejxclientef(clijxf_id),
	CONSTRAINT fkMovUsuId FOREIGN KEY (usu_id)
	REFERENCES tbl_usuarios(usu_id),
	CONSTRAINT fkMovRpzId FOREIGN KEY (rpz_id)
	REFERENCES tbl_regra_prazos(rpz_id)
);
