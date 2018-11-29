import json, pymysql

def connect():
    return pymysql.connect("198.199.73.180", "root", "aspartners2018", "credit_management")

def formatDate(date):
    return date.split("/")

def setIdClient():
    con = connect()
    cursor = con.cursor()

    query = "INSERT INTO tbl_clientejxclientef(isQualified) VALUES (1)"

    try:
        cursor.execute(query)
        id = cursor.lastrowid
        cursor.close() # smcjxsmc
        con.commit()
    except Exception as e:
        con.rollback()
    finally:
        con.close()
        return id

def read(uf):
    con = connect()
    cursor = con.cursor()

    query = "SELECT smcj_uf FROM tb_salesmanClientJuristical WHERE smcj_uf LIKE %s"

    try:
        cursor.execute(query, uf)
        return cursor.fetchall()
    except:
        return -1
    finally:
        con.close()

def setRequest(value, id, sis):
    con = connect()
    cursor = con.cursor()

    query = "INSERT INTO tbl_cliente_juridico (clij_cnpj,clij_nome,clij_razao_social,clij_nome_fantasia,clifj_status_empresa,clij_data_fundacao,clij_email,clij_telefone,clij_cep,clij_cidade,clij_bairro,clij_endereco_numero,clij_endereco,clij_pais,clij_complemento,clij_uf,usu_id,clijxf_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    dt = formatDate(value['data_fundacao'])

    try:
        cursor.execute(query, (value['cnpj'], value['nome'], value['razao_social'], value['nome_fantasia'], sis, str(dt[2]+"/"+dt[1]+"/"+dt[0]), value['email'], value['telefone'], value['cep'], value['cidade'], value['bairro'], value['endereco_numero'], value['endereco'], value['pais'], value['complemento'], value['uf'], 1, id))
        con.commit()
        print("success")
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        con.close()



aux = [{'email': 'contabilidade@moveiscolorado.com.br', 'telefone': '(43) 3276-9638', 'cep': '86706180', 'cidade': 'Arapongas', 'nome_fantasia': 'Ind e Com de Moveis Colorado', 'bairro': 'Vila Industrial', 'endereco_numero': '70', 'endereco': 'R Rua Alcatraz', 'cnpj': '77250173000192', 'pais': 'Brasil', 'razao_social': 'Irmaos Tudino Ltda Em Recuperacao Judicial', 'nome': 'Ind e Com de Moveis Colorado - Irmaos Tudino Ltda Em Recuperacao Judicial', 'complemento': None, 'data_fundacao': '7/12/1976', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': '76300000', 'cidade': 'Ceres', 'nome_fantasia': None, 'bairro': 'Centro', 'endereco_numero': '885', 'endereco': 'R 41', 'cnpj': '00059620000104', 'pais': 'Brasil', 'razao_social': 'Moreira Turismo Ltda - ME', 'nome': 'Moreira Turismo Ltda - ME', 'complemento': 'Qd. 39 Lts 20 A 25', 'data_fundacao': '5/4/1994', 'uf': 'GO'}, {'email': None, 'telefone': None, 'cep': '86072250', 'cidade': 'Londrina', 'nome_fantasia': None, 'bairro': 'Pq Indl Cacique', 'endereco_numero': '350', 'endereco': 'R Walter Pereira', 'cnpj': '77769131000162', 'pais': 'Brasil', 'razao_social': 'Montasa Engenharia Industria e Comercio Ltda', 'nome': 'Montasa Engenharia Industria e Comercio Ltda', 'complemento': 'Caixa Postal 584', 'data_fundacao': '27/12/1983', 'uf': 'PR'}, {'email': None, 'telefone': '(42) 3273-3294', 'cep': '84268310', 'cidade': 'Telemaco Borba', 'nome_fantasia': 'Transpapel', 'bairro': 'Area 1', 'endereco_numero': None, 'endereco': 'Rod Papel Pr-160', 'cnpj': '79084117000150', 'pais': 'Brasil', 'razao_social': 'Transpapel Transportes Rodoviarios Ltda', 'nome': 'Transpapel - Transpapel Transportes Rodoviarios Ltda', 'complemento': 'Km 22,5 1 Andar', 'data_fundacao': '24/12/1985', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': '82315010', 'cidade': 'Curitiba', 'nome_fantasia': 'Neo Arquitetura', 'bairro': 'Sao Braz', 'endereco_numero': '1650', 'endereco': 'R Brasilio Cuman', 'cnpj': '00119549000108', 'pais': 'Brasil', 'razao_social': 'Neo Stands Ltda', 'nome': 'Neo Arquitetura - Neo Stands Ltda', 'complemento': None, 'data_fundacao': '21/7/1994', 'uf': 'PR'}, {'email': None, 'telefone': '(43) 3524-1957 / (43) 3524-2030', 'cep': '86300000', 'cidade': 'Cornelio Procopio', 'nome_fantasia': 'Raizes', 'bairro': 'Centro', 'endereco_numero': '204', 'endereco': 'R Carlos Gomes', 'cnpj': '85074037000117', 'pais': 'Brasil', 'razao_social': 'Catsumi Fushimi & Cia Ltda - ME', 'nome': 'Raizes - Catsumi Fushimi & Cia Ltda - ME', 'complemento': None, 'data_fundacao': '25/6/1992', 'uf': 'PR'}, {'email': 'crochedo@zaz.com.br', 'telefone': '(0062) 0241-8450', 'cep': '74810240', 'cidade': 'Goiania', 'nome_fantasia': 'Construtora Rochedo', 'bairro': 'Jardim Goias', 'endereco_numero': '843', 'endereco': 'R 56', 'cnpj': '00085696000104', 'pais': 'Brasil', 'razao_social': 'Construtora e Incorporadora Rochedo Ltda', 'nome': 'Construtora Rochedo - Construtora e Incorporadora Rochedo Ltda', 'complemento': None, 'data_fundacao': '8/6/1982', 'uf': 'GO'}, {'email': None, 'telefone': '(44) 3639-7300 / (44) 3639-7300', 'cep': '87503020', 'cidade': 'Umuarama', 'nome_fantasia': None, 'bairro': 'Zona Armazem', 'endereco_numero': '2280', 'endereco': 'Av Estacao', 'cnpj': '02232017000108', 'pais': 'Brasil', 'razao_social': 'Umed - Ind. e Com. de Produtos Hospitalares Ltda - ME', 'nome': 'Umed - Ind. e Com. de Produtos Hospitalares Ltda - ME', 'complemento': 'Centro', 'data_fundacao': '14/11/1997', 'uf': 'PR'}, {'email': None, 'telefone': '(41) 3264-5694', 'cep': '80410200', 'cidade': 'Curitiba', 'nome_fantasia': 'Vetorial', 'bairro': 'Centro', 'endereco_numero': '275', 'endereco': 'R Visconde De Nacar', 'cnpj': '04520826000132', 'pais': 'Brasil', 'razao_social': 'Vetorial Ltda', 'nome': 'Vetorial - Vetorial Ltda', 'complemento': None, 'data_fundacao': '1/6/2001', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': '30140040', 'cidade': 'Belo Horizonte', 'nome_fantasia': None, 'bairro': 'Santa Efigenia', 'endereco_numero': '455', 'endereco': 'R Padre Marinho', 'cnpj': '00057147000118', 'pais': 'Brasil', 'razao_social': 'Arthromig Arthroscopia e Ortopedia Ltda - ME', 'nome': 'Arthromig Arthroscopia e Ortopedia Ltda - ME', 'complemento': '14 Andar', 'data_fundacao': '2/5/1994', 'uf': 'MG'}, {'email': None, 'telefone': '(43) 3339-3949', 'cep': '86010490', 'cidade': 'Londrina', 'nome_fantasia': 'Talheres & Cia', 'bairro': 'Centro', 'endereco_numero': '459', 'endereco': 'Av Celso Garcia Cid', 'cnpj': '07176593000190', 'pais': 'Brasil', 'razao_social': 'Utilidom Comercio de Utilidades Domesticas Ltda - ME', 'nome': 'Talheres & Cia - Utilidom Comercio de Utilidades Domesticas Ltda - ME', 'complemento': 'Sala 10', 'data_fundacao': '13/1/2005', 'uf': 'PR'}, {'email': 'lfg.contabil@gmail.com', 'telefone': '(41) 3025-6620', 'cep': '82800050', 'cidade': 'Curitiba', 'nome_fantasia': None, 'bairro': 'Taruma', 'endereco_numero': '79', 'endereco': 'R Doutor Heitor Valente', 'cnpj': '79215448000182', 'pais': 'Brasil', 'razao_social': 'Retibens Distribuidora de Pecas Ltda', 'nome': 'Retibens Distribuidora de Pecas Ltda', 'complemento': None, 'data_fundacao': '23/5/1986', 'uf': 'PR'}, {'email': 'aurso@tmt-motoco.com.br', 'telefone': '(41) 9606-4087', 'cep': '81200200', 'cidade': 'Curitiba', 'nome_fantasia': None, 'bairro': 'Mossungue', 'endereco_numero': '113', 'endereco': 'R Gra Nicco', 'cnpj': '05203407000130', 'pais': 'Brasil', 'razao_social': 'Tmt do Brasil Ltda', 'nome': 'Tmt do Brasil Ltda', 'complemento': 'Bloco Iii Conj Comercial 101', 'data_fundacao': '2/8/2002', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': '86042150', 'cidade': 'Londrina', 'nome_fantasia': 'Mercado Zona Sul', 'bairro': 'Parque Ouro Branco', 'endereco_numero': '240', 'endereco': 'R Das Violetas', 'cnpj': '00702127000152', 'pais': 'Brasil', 'razao_social': 'Angela H Nakamura & Cia Ltda - Epp', 'nome': 'Mercado Zona Sul - Angela H Nakamura & Cia Ltda - Epp', 'complemento': None, 'data_fundacao': '17/7/1995', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': '87530000', 'cidade': 'Icaraima', 'nome_fantasia': 'Incolage', 'bairro': 'Zona Rural', 'endereco_numero': 'Sn', 'endereco': 'Rod Pr 082', 'cnpj': '02047232000120', 'pais': 'Brasil', 'razao_social': 'Incolage Ltda - Epp', 'nome': 'Incolage - Incolage Ltda - Epp', 'complemento': None, 'data_fundacao': '20/8/1997', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': None, 'cidade': None, 'nome_fantasia': None, 'bairro': None, 'endereco_numero': None, 'endereco': None, 'cnpj': '80794886000121', 'pais': None, 'razao_social': 'Transplamelo Transportes Ltda', 'nome': 'Transplamelo Transportes Ltda', 'complemento': None, 'data_fundacao': '5/7/1988', 'uf': None}, {'email': 'alzemir@embraer.com.br', 'telefone': '(12) 3927-3735 / (12) 3927-8563', 'cep': '12227901', 'cidade': 'Sao Jose Dos Campos', 'nome_fantasia': None, 'bairro': 'Putim', 'endereco_numero': '2170', 'endereco': 'Av Brigadeiro Faria Lima', 'cnpj': '07689002000189', 'pais': 'Brasil', 'razao_social': 'Embraer S.A.', 'nome': 'Embraer S.A.', 'complemento': None, 'data_fundacao': '8/9/2005', 'uf': 'SP'}, {'email': None, 'telefone': '(041) 2633-211', 'cep': None, 'cidade': None, 'nome_fantasia': 'Maha Matriz', 'bairro': None, 'endereco_numero': None, 'endereco': None, 'cnpj': '00494078000100', 'pais': None, 'razao_social': 'Maha Skates Wear-Comercio de Artigos Esportivos Ltda - ME', 'nome': 'Maha Matriz - Maha Skates Wear-Comercio de Artigos Esportivos Ltda - ME', 'complemento': None, 'data_fundacao': '2/1/1995', 'uf': None}, {'email': None, 'telefone': None, 'cep': '87113000', 'cidade': 'Sarandi', 'nome_fantasia': 'Norpecas', 'bairro': 'Jardim Nova Europa', 'endereco_numero': '1065', 'endereco': 'Av Ademar Bornia', 'cnpj': '80315120000117', 'pais': 'Brasil', 'razao_social': 'Vilela Distribuidora de Auto-Pecas Ltda. - ME', 'nome': 'Norpecas - Vilela Distribuidora de Auto-Pecas Ltda. - ME', 'complemento': None, 'data_fundacao': '9/10/1987', 'uf': 'PR'}, {'email': 'mecnunes@viareal.com.br', 'telefone': '(0031) 0742-1919', 'cep': '36420000', 'cidade': 'Ouro Branco', 'nome_fantasia': 'Mecanica Nunes Industria e Comercio', 'bairro': 'D.I. De Ouro Branco', 'endereco_numero': '391', 'endereco': 'R Antonio Joao Vieira', 'cnpj': '00085144000198', 'pais': 'Brasil', 'razao_social': 'Mecanica Industrial Nunes Eireli', 'nome': 'Mecanica Nunes Industria e Comercio - Mecanica Industrial Nunes Eireli', 'complemento': None, 'data_fundacao': '8/6/1994', 'uf': 'MG'}, {'email': None, 'telefone': '(85) 8785-4185', 'cep': '60332170', 'cidade': 'Fortaleza', 'nome_fantasia': 'Lonasa', 'bairro': 'Barra Do Ceara', 'endereco_numero': '563', 'endereco': 'R Senador Robert Kennedy', 'cnpj': '00104589000178', 'pais': 'Brasil', 'razao_social': 'Lonasa Comercial e Importadora de Eletrodomesticos Ltda - ME', 'nome': 'Lonasa - Lonasa Comercial e Importadora de Eletrodomesticos Ltda - ME', 'complemento': None, 'data_fundacao': '5/7/1994', 'uf': 'CE'}, {'email': None, 'telefone': None, 'cep': '81270330', 'cidade': 'Curitiba', 'nome_fantasia': None, 'bairro': 'Campo Comprido', 'endereco_numero': '84', 'endereco': 'R Joao Dembinski', 'cnpj': '78903143000109', 'pais': 'Brasil', 'razao_social': 'Binaar Comercio e Reparacao de Equip Pneumaticos Ltda - Epp', 'nome': 'Binaar Comercio e Reparacao de Equip Pneumaticos Ltda - Epp', 'complemento': None, 'data_fundacao': '6/8/1985', 'uf': 'PR'}, {'email': None, 'telefone': '(41) 3656-2065', 'cep': '83414170', 'cidade': 'Colombo', 'nome_fantasia': None, 'bairro': 'Centro', 'endereco_numero': '316', 'endereco': 'R Padre Francisco Bonato', 'cnpj': '05728170000100', 'pais': 'Brasil', 'razao_social': 'Usina Termoeletrica Winimport S.A.', 'nome': 'Usina Termoeletrica Winimport S.A.', 'complemento': None, 'data_fundacao': '6/2/2003', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': '95185000', 'cidade': 'Carlos Barbosa', 'nome_fantasia': None, 'bairro': 'Centro', 'endereco_numero': '308', 'endereco': 'R Garibaldi', 'cnpj': '93514180000100', 'pais': 'Brasil', 'razao_social': 'Tramontina Sul S/A', 'nome': 'Tramontina Sul S/A', 'complemento': None, 'data_fundacao': '24/7/1990', 'uf': 'RS'}, {'email': None, 'telefone': None, 'cep': None, 'cidade': None, 'nome_fantasia': 'Monaco Veiculos', 'bairro': None, 'endereco_numero': None, 'endereco': None, 'cnpj': '00561180000180', 'pais': None, 'razao_social': 'Estacionamento Monaco de Veiculos Ltda', 'nome': 'Monaco Veiculos - Estacionamento Monaco de Veiculos Ltda', 'complemento': None, 'data_fundacao': '20/4/1995', 'uf': None}, {'email': 'jchela@bol.com.br', 'telefone': '(11) 3262-5042', 'cep': '12244873', 'cidade': 'Sao Jose Dos Campos', 'nome_fantasia': None, 'bairro': 'Urbanova', 'endereco_numero': '50', 'endereco': 'Av Antonio Widmer', 'cnpj': '18186639000179', 'pais': 'Brasil', 'razao_social': 'Joao Luiz Chela - ME', 'nome': 'Joao Luiz Chela - ME', 'complemento': None, 'data_fundacao': '24/5/2013', 'uf': 'SP'}, {'email': 'wyny@wynybr.com.br', 'telefone': '(43) 3324-7353 / (43) 3324-8222', 'cep': '86020080', 'cidade': 'Londrina', 'nome_fantasia': 'Wyny do Brasil', 'bairro': 'Centro', 'endereco_numero': '210', 'endereco': 'Av Higienopolis', 'cnpj': '01111828000180', 'pais': 'Brasil', 'razao_social': 'Wyny do Brasil Industria e Comercio de Couros Ltda', 'nome': 'Wyny do Brasil - Wyny do Brasil Industria e Comercio de Couros Ltda', 'complemento': 'Andar 15 Sala 1.504', 'data_fundacao': '26/3/1996', 'uf': 'PR'}, {'email': 'celiopimentel@dglnet.com.br', 'telefone': '(12) 3103-1747 / (12) 3103-1717', 'cep': '12630000', 'cidade': 'Cachoeira Paulista', 'nome_fantasia': None, 'bairro': 'Jardim Europa I I', 'endereco_numero': '75', 'endereco': 'R Prof Cleston M Paiva', 'cnpj': '07979736000100', 'pais': 'Brasil', 'razao_social': 'Geraldo Luis da Silva Ribeiro Informatica - ME', 'nome': 'Geraldo Luis da Silva Ribeiro Informatica - ME', 'complemento': None, 'data_fundacao': '19/4/2006', 'uf': 'SP'}, {'email': None, 'telefone': None, 'cep': '84261020', 'cidade': 'Telemaco Borba', 'nome_fantasia': None, 'bairro': 'Dist.Industrial', 'endereco_numero': None, 'endereco': 'Rod Do Papel Km 15', 'cnpj': '00760665000101', 'pais': 'Brasil', 'razao_social': 'Paledson Industria e Comercio de Madeiras Ltda', 'nome': 'Paledson Industria e Comercio de Madeiras Ltda', 'complemento': None, 'data_fundacao': '9/8/1995', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': '87013000', 'cidade': 'Maringa', 'nome_fantasia': None, 'bairro': 'Zona 01', 'endereco_numero': '2843', 'endereco': 'Av Brasil', 'cnpj': '03525415000177', 'pais': 'Brasil', 'razao_social': 'Controle Construcoes Civis Ltda - ME', 'nome': 'Controle Construcoes Civis Ltda - ME', 'complemento': 'Sala 03 1. Andar', 'data_fundacao': '24/11/1999', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': None, 'cidade': None, 'nome_fantasia': None, 'bairro': None, 'endereco_numero': None, 'endereco': None, 'cnpj': '80222441000177', 'pais': None, 'razao_social': 'Vidracaria Cometa do Parana Ltda', 'nome': 'Vidracaria Cometa do Parana Ltda', 'complemento': None, 'data_fundacao': '20/8/1966', 'uf': None}, {'email': None, 'telefone': '(42) 3635-4341', 'cep': None, 'cidade': None, 'nome_fantasia': 'Andiju', 'bairro': None, 'endereco_numero': None, 'endereco': None, 'cnpj': '05761152000120', 'pais': None, 'razao_social': 'Andiju Alimentos Ltda.', 'nome': 'Andiju - Andiju Alimentos Ltda.', 'complemento': None, 'data_fundacao': '7/7/2003', 'uf': None}, {'email': 'celiopimentel@dglnet.com.br', 'telefone': '(12) 3103-2428', 'cep': '12630000', 'cidade': 'Cachoeira Paulista', 'nome_fantasia': 'Marcio Mendes Empreendimentos Imobiliarios', 'bairro': 'Centro', 'endereco_numero': '89', 'endereco': 'R Bernardino De Campos', 'cnpj': '17085532000171', 'pais': 'Brasil', 'razao_social': 'Marcio Mendes Empreendimentos Imobiliarios Eireli - ME', 'nome': 'Marcio Mendes Empreendimentos Imobiliarios - Marcio Mendes Empreendimentos Imobiliarios Eireli - ME', 'complemento': 'Sala 2', 'data_fundacao': '17/10/2012', 'uf': 'SP'}, {'email': None, 'telefone': '(44) 2286-876', 'cep': '87045360', 'cidade': 'Maringa', 'nome_fantasia': None, 'bairro': 'Jardim America', 'endereco_numero': '200', 'endereco': 'Av Das Industrias', 'cnpj': '01422442000199', 'pais': 'Brasil', 'razao_social': 'Corion Industria e Comercio de Vestuarios Ltda - ME', 'nome': 'Corion Industria e Comercio de Vestuarios Ltda - ME', 'complemento': 'Lote 11', 'data_fundacao': '5/9/1996', 'uf': 'PR'}, {'email': 'megleste@uol.com.br', 'telefone': '(0011) 0208-1966', 'cep': None, 'cidade': None, 'nome_fantasia': None, 'bairro': None, 'endereco_numero': None, 'endereco': None, 'cnpj': '00020324000191', 'pais': None, 'razao_social': 'Meg Leste Hospitalar Ltda', 'nome': 'Meg Leste Hospitalar Ltda', 'complemento': None, 'data_fundacao': '22/6/1994', 'uf': None}, {'email': 'maximum@wnet.com.br', 'telefone': '(044) 2621-670', 'cep': None, 'cidade': None, 'nome_fantasia': 'Nina Modas', 'bairro': None, 'endereco_numero': None, 'endereco': None, 'cnpj': '79777751000179', 'pais': None, 'razao_social': 'Industria e Comercio de Confeccoes Arzina Ltda.', 'nome': 'Nina Modas - Industria e Comercio de Confeccoes Arzina Ltda.', 'complemento': None, 'data_fundacao': '16/1/1987', 'uf': None}, {'email': 'contabilidade@fertimourao.com.br', 'telefone': '(44) 3518-1991 / (44) 3518-1971', 'cep': '87302140', 'cidade': 'Campo Mourao', 'nome_fantasia': None, 'bairro': 'Centro', 'endereco_numero': '855', 'endereco': 'R Mambore', 'cnpj': '03311884000193', 'pais': 'Brasil', 'razao_social': 'Campoceres Agricola Ltda - ME', 'nome': 'Campoceres Agricola Ltda - ME', 'complemento': None, 'data_fundacao': '12/7/1999', 'uf': 'PR'}, {'email': 'egc@contabilidadecipriani.com.br', 'telefone': '(41) 2576-987', 'cep': '80740050', 'cidade': 'Curitiba', 'nome_fantasia': None, 'bairro': 'Campina Do Siqueira', 'endereco_numero': '276', 'endereco': 'R Prof. Pedro Viriato Parigot De Souza', 'cnpj': '03641903000140', 'pais': 'Brasil', 'razao_social': 'Egc Construtora e Obras Ltda', 'nome': 'Egc Construtora e Obras Ltda', 'complemento': None, 'data_fundacao': '9/2/2000', 'uf': 'PR'}, {'email': 'revepaper@revepaper.com.br', 'telefone': '(41) 3544-0604 / (41) 3663-1001', 'cep': '83408280', 'cidade': 'Colombo', 'nome_fantasia': None, 'bairro': 'Jardim Palmital', 'endereco_numero': '2021-B', 'endereco': 'R Abel Scuissiato', 'cnpj': '02637265000120', 'pais': 'Brasil', 'razao_social': 'Revepaper do Brasil Importacao & Exportacao Ltda', 'nome': 'Revepaper do Brasil Importacao & Exportacao Ltda', 'complemento': None, 'data_fundacao': '26/6/1998', 'uf': 'PR'}, {'email': 'efraim@rotal.ind.br', 'telefone': '(62) 3091-9900 / (62) 3091-9950', 'cep': 'ecida De Goiania', 'cidade': '03 Ao 10', 'nome_fantasia': 'Rotal Hospitalar', 'bairro': 'Quadra29 Lote 01', 'endereco_numero': 'Sn', 'endereco': 'R Goias', 'cnpj': '00086231000160', 'pais': 'GO', 'razao_social': 'Rotal Hospitalar Ltda', 'nome': 'Rotal Hospitalar - Rotal Hospitalar Ltda', 'complemento': None, 'data_fundacao': '8/6/1982', 'uf': 'Vila Nossa Senhora De Lourdes'}, {'email': 'contabilidade@multifarma.com.br', 'telefone': '(41) 3313-3434', 'cep': '81315680', 'cidade': 'Curitiba', 'nome_fantasia': 'Multifarma', 'bairro': 'Cidade Industrial', 'endereco_numero': '156', 'endereco': 'R Lea Moreira De Souza Moura', 'cnpj': '07079300000157', 'pais': 'Brasil', 'razao_social': 'Zen Comercio de Medicamentos Ltda', 'nome': 'Multifarma - Zen Comercio de Medicamentos Ltda', 'complemento': None, 'data_fundacao': '8/11/2004', 'uf': 'PR'}, {'email': None, 'telefone': '(43) 9653-5212', 'cep': '86800720', 'cidade': 'Apucarana', 'nome_fantasia': None, 'bairro': 'Centro', 'endereco_numero': '1022', 'endereco': 'R Oswaldo Cruz', 'cnpj': '08582627000100', 'pais': 'Brasil', 'razao_social': 'Anaheim Comercio e Logistica de Alimentos S/A', 'nome': 'Anaheim Comercio e Logistica de Alimentos S/A', 'complemento': 'Sala 16 Andar 2 Edif Denadai', 'data_fundacao': '5/1/2007', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': None, 'cidade': None, 'nome_fantasia': 'White Coast', 'bairro': None, 'endereco_numero': None, 'endereco': None, 'cnpj': '00156164000102', 'pais': None, 'razao_social': 'Fabio Sanchez & Cia Ltda - ME', 'nome': 'White Coast - Fabio Sanchez & Cia Ltda - ME', 'complemento': None, 'data_fundacao': '22/8/1994', 'uf': None}, {'email': 'marcia@primartconsultoria.com.br', 'telefone': '(21) 2772-3767 / (21) 2240-6850', 'cep': '20031141', 'cidade': 'Rio De Janeiro', 'nome_fantasia': None, 'bairro': 'Centro', 'endereco_numero': '3', 'endereco': 'R Mexico', 'cnpj': '00063069000164', 'pais': 'Brasil', 'razao_social': 'Star Info Servicos de Informatica Ltda - ME', 'nome': 'Star Info Servicos de Informatica Ltda - ME', 'complemento': 'Sala 801 Parte', 'data_fundacao': '9/5/1994', 'uf': 'RJ'}, {'email': None, 'telefone': None, 'cep': '65020490', 'cidade': 'Sao Luis', 'nome_fantasia': 'Centro de Olhos de Sao Luis', 'bairro': 'Centro', 'endereco_numero': '80', 'endereco': 'R Rio Branco', 'cnpj': '00071178000123', 'pais': 'Brasil', 'razao_social': 'Centro de Olhos de Sao Luis Eireli', 'nome': 'Centro de Olhos de Sao Luis - Centro de Olhos de Sao Luis Eireli', 'complemento': None, 'data_fundacao': '18/5/1994', 'uf': 'MA'}, {'email': 'gerencia@crats.com.br', 'telefone': '(15) 2102-7824', 'cep': '18190000', 'cidade': 'Aracoiaba Da Serra', 'nome_fantasia': None, 'bairro': 'Centro', 'endereco_numero': '33', 'endereco': 'R Padua', 'cnpj': '00014676000134', 'pais': 'Brasil', 'razao_social': 'Crats Trabalho Temporario Ltda - ME', 'nome': 'Crats Trabalho Temporario Ltda - ME', 'complemento': None, 'data_fundacao': '8/6/1994', 'uf': 'SP'}, {'email': 'muralha@muralhacontabil.com.br', 'telefone': '(46) 3524-2625 / (46) 3524-2625', 'cep': '84178490', 'cidade': 'Castro', 'nome_fantasia': None, 'bairro': 'Cantagalo', 'endereco_numero': '37', 'endereco': 'R Licinio Pereira Bueno', 'cnpj': '04603868000137', 'pais': 'Brasil', 'razao_social': 'Evele Calcados Ltda - ME', 'nome': 'Evele Calcados Ltda - ME', 'complemento': None, 'data_fundacao': '14/8/2001', 'uf': 'PR'}, {'email': None, 'telefone': '(41) 3333-9774', 'cep': '80230150', 'cidade': 'Curitiba', 'nome_fantasia': 'Dystak Distribuidora', 'bairro': 'Reboucas', 'endereco_numero': '4314', 'endereco': 'R Joao Negrao', 'cnpj': '82211939000160', 'pais': 'Brasil', 'razao_social': 'Dystak Distribuidora de Medicamentos e Perfumaria Ltda - ME', 'nome': 'Dystak Distribuidora - Dystak Distribuidora de Medicamentos e Perfumaria Ltda - ME', 'complemento': None, 'data_fundacao': '27/6/1990', 'uf': 'PR'}, {'email': None, 'telefone': '(61) 3034-9950 / (61) 3034-9999', 'cep': '71250410', 'cidade': 'Brasilia', 'nome_fantasia': 'Wagner Empreendimentos Imobiliarios', 'bairro': 'Guara', 'endereco_numero': '01', 'endereco': 'Q Scia Quadra 12 Conjunto', 'cnpj': '00043513000180', 'pais': 'Brasil', 'razao_social': 'Wagner Imobiliaria Refrigeracao e Construcoes Industria e Comercio - Eireli', 'nome': 'Wagner Empreendimentos Imobiliarios - Wagner Imobiliaria Refrigeracao e Construcoes Industria e Comercio - Eireli', 'complemento': 'Lote 08', 'data_fundacao': '2/6/1967', 'uf': 'DF'}, {'email': 'fborazo@uol.com.br', 'telefone': '(42) 3035-7431', 'cep': '85070190', 'cidade': 'Guarapuava', 'nome_fantasia': None, 'bairro': 'Santana', 'endereco_numero': '450', 'endereco': 'R Pedro Siqueira', 'cnpj': '04163722000118', 'pais': 'Brasil', 'razao_social': 'Ecoenergia Geracao Termoeletrica Ltda', 'nome': 'Ecoenergia Geracao Termoeletrica Ltda', 'complemento': None, 'data_fundacao': '28/11/2000', 'uf': 'PR'}, {'email': None, 'telefone': '(47) 3035-5152 / (47) 3035-5153', 'cep': '89062101', 'cidade': 'Blumenau', 'nome_fantasia': None, 'bairro': 'Itoupava Central', 'endereco_numero': '3159', 'endereco': 'R Gustavo Zimmermann', 'cnpj': '00056633000111', 'pais': 'Brasil', 'razao_social': 'Tecnoblu S/A Industria e Comercio', 'nome': 'Tecnoblu S/A Industria e Comercio', 'complemento': None, 'data_fundacao': '2/5/1994', 'uf': 'SC'}, {'email': 'celiopimentel@dglnet.com.br', 'telefone': '(12) 3103-2428', 'cep': '12630000', 'cidade': 'Cachoeira Paulista', 'nome_fantasia': 'Taoker Tecnologia', 'bairro': 'Centro', 'endereco_numero': '113', 'endereco': 'R Ayrton Rodrigues Do Prado', 'cnpj': '20650181000109', 'pais': 'Brasil', 'razao_social': 'Taoker Tecnologia Ltda - ME', 'nome': 'Taoker Tecnologia - Taoker Tecnologia Ltda - ME', 'complemento': None, 'data_fundacao': '16/7/2014', 'uf': 'SP'}, {'email': None, 'telefone': '(43) 3428-1279', 'cep': '86825000', 'cidade': 'Marilandia Do Sul', 'nome_fantasia': 'Lunnisul Alimentos', 'bairro': 'Jardim Toquio', 'endereco_numero': None, 'endereco': 'Av Cerejeiras', 'cnpj': '08560499000101', 'pais': 'Brasil', 'razao_social': 'Lunnisul Industria, Comercio e Importacao de Alimentos Ltda. - ME', 'nome': 'Lunnisul Alimentos - Lunnisul Industria, Comercio e Importacao de Alimentos Ltda. - ME', 'complemento': 'Ibc Portao 13-16', 'data_fundacao': '20/12/2006', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': '80010070', 'cidade': 'Curitiba', 'nome_fantasia': 'Calcados Campeao', 'bairro': 'Centro', 'endereco_numero': '255', 'endereco': 'R Sen.Alencar Guimaraes', 'cnpj': '01073297000269', 'pais': 'Brasil', 'razao_social': 'Comercio de Calcados Campeao Ltda - ME', 'nome': 'Calcados Campeao - Comercio de Calcados Campeao Ltda - ME', 'complemento': 'Loja 1/3', 'data_fundacao': '1/2/1996', 'uf': 'PR'}, {'email': None, 'telefone': None, 'cep': '81650300', 'cidade': 'Curitiba', 'nome_fantasia': None, 'bairro': 'Vila Hauer', 'endereco_numero': '50', 'endereco': 'R Evaristo Da Veiga', 'cnpj': '73260606000130', 'pais': 'Brasil', 'razao_social': 'Allied Informatica Ltda - ME', 'nome': 'Allied Informatica Ltda - ME', 'complemento': None, 'data_fundacao': '24/8/1993', 'uf': 'PR'}]

i = 0
word = 'Em Recuperacao Judicial'
sis = ''
for j in aux:
    sis = 'ATIVO'

    pos = j['nome'].find(word)
    if (pos != -1):
        j['nome'] = j['nome'][0:pos-1]
        sis = 'RECUPERACAO JUDICIAL'
    id = setIdClient()
    setRequest(j, id, sis)