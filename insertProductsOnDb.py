import csv, pymysql.cursors, datetime

# Conexão com o db
con = pymysql.connect(host="198.199.73.180",
                             user='root',
                             password='aspartners2018',
                             db='credit_management')

# Especificando qual o bd utilizado
con.select_db("credit_management")

# Dicionario para usar como estrutura de decisao
dic = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6
}

# Abrindo conexão
with con.cursor() as cursor:
    #Abrindo arquivo csv
    with open('arquivo_teste1.csv') as csvfile:
        # Lendo arquivo
        readCSV = csv.reader(csvfile, delimiter=',')
        # Varrendo arquivo
        for row in readCSV:
            query = "INSERT INTO `produto` (`cat_id`, `prod_nome`, `prod_cod`, `prod_desc`) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (int(dic[row[0]]), str(row[1]), str(row[2]), str(row[3])))
            # Commitando alterações
            con.commit()
        # Fechando conexão
        con.close()
