/* Selecionando o banco de dados */
USE credit_management;

/* Inserção dos dados fixos da tabela `tbl_prazo_level` */

INSERT INTO tbl_prazo_level (prl_id, acc_descricao)
VALUES (0, 'Minimo');
INSERT INTO tbl_prazo_level (prl_id, acc_descricao)
VALUES (1, 'Medio');
INSERT INTO tbl_prazo_level (prl_id, acc_descricao)
VALUES (3, 'Maximo');

/* CREATE TABLE tbl_acesso (
	acc_id int(1) primary key unique,
	acc_descricao varchar(100),
	acc_limite_desconto int,
	prl_id int(1),

	CONSTRAINT fkAccPrlId FOREIGN KEY (prl_id)
	REFERENCES tbl_prazo_level (prl_id)
); */

INSERT INTO tbl_acesso (acc_id, acc_descricao, acc_limite_desconto, prl_id) VALUES (0, 'Supreme root', 100, 3);

/* Inserção dos dados fixos da tabela `tbl_regra_prazos` */

INSERT INTO tbl_regra_prazos (rpz_id, rpz_status_desc)
VALUES (0, 'Paga até o vencimento');
INSERT INTO tbl_regra_prazos (rpz_id, rpz_status_desc)
VALUES (1, 'Paga entre 1 e 10 dias após o vencimento');
INSERT INTO tbl_regra_prazos (rpz_id, rpz_status_desc)
VALUES (2, 'Paga entre 11 e 20 dias após o vencimento');
INSERT INTO tbl_regra_prazos (rpz_id, rpz_status_desc)
VALUES (3, 'Paga entre 21 dias e 30 dias após o vencimento');
INSERT INTO tbl_regra_prazos (rpz_id, rpz_status_desc)
VALUES (4, 'Paga após 30 dias');

/* Inserção do supreme root */

INSERT INTO tbl_usuarios (usu_nome_completo, acc_id, usu_email, usu_senha) VALUES ('root', 0, 'admin', 'admin');

