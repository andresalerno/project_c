import csv, pymysql.cursors, datetime

# Conexão com o db
con = pymysql.connect(host="198.199.73.180",
                             user='root',
                             password='aspartners2018',
                             db='credit_management')

# Especificando qual o bd utilizado
con.select_db("credit_management")

# Abrindo conexão
with con.cursor() as cursor:
    #Abrindo arquivo csv
    with open('arquivo_teste.csv') as csvfile:
        # Lendo arquivo
        readCSV = csv.reader(csvfile, delimiter=',')
        # Varrendo arquivo
        for row in readCSV:
            # Splitando a data para inserir no formato certo
            date = row[2].split("/")
            query = "INSERT INTO `pessoa` (`pes_nome`, `pes_data_nasc`, `pes_estado_civil`, `pes_grupo_economico`, `pes_cep`, `pes_celular`) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (str(row[1]), datetime.date(int(date[2]), int(date[1]), int(date[0])), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
            # Commitando alterações
            con.commit()
        # Fechando conexão
        con.close()
