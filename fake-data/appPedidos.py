import pymysql
from datetime import date, datetime

pedidos = [{
    "status": 1,
    "valor_total": 220.00,
    "prazo": 30,
    "descricao_classificacao": "Aprovado com sucesso",
    "class_usuario": 1,
    "usuario": 1,
    "cliente": 1,
    "produtos": [{
        "quantidade": 1,
        "produtoid": 1
    },
    {
        "quantidade": 1,
        "produtoid": 2
    }]
},
{
    "status": 1,
    "valor_total": 420.00,
    "prazo": 30,
    "descricao_classificacao": "Aprovado com sucesso",
    "class_usuario": 1,
    "usuario": 1,
    "cliente": 4,
    "produtos": [{
        "quantidade": 2,
        "produtoid": 1
    },
    {
        "quantidade": 1,
        "produtoid": 3
    }]
},
{
    "status": 1,
    "valor_total": 1335.00,
    "prazo": 30,
    "descricao_classificacao": "Aprovado com sucesso",
    "class_usuario": 1,
    "usuario": 1,
    "cliente": 7,
    "produtos": [{
        "quantidade": 3,
        "produtoid": 8
    },
    {
        "quantidade": 1,
        "produtoid": 13
    }]
}]

def connect():
    return pymysql.connect("198.199.73.180", "root", "aspartners2018", "credit_management")

def getNow():
    date = datetime.now().strftime('%d/%m/%Y')
    hours = datetime.now().strftime('%H:%M')
    date = date.split('/')
    hours = hours.split(':')

    return str(date[0]+date[1]+date[2]+hours[0]+hours[1])

def getDate():
    date = datetime.now().strftime('%Y/%m/%d')

    return date

def setProdutos(produtos, id_ped):
    con = connect()
    cursor = con.cursor()

    query = "INSERT INTO tbl_carrinho_produtos (quantidade,ped_id,prod_id) VALUES (%s,%s,%s)"

    try:
        cursor.execute(query, (produtos['quantidade'], id_ped, produtos['produtoid']))
        print(cursor)
        con.commit()
        print("produto add")
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        con.close()

def setPedidos(pedido, produtos):
    con = connect()
    cursor = con.cursor()

    query = "INSERT INTO tbl_pedidos(ped_status,ped_valor_total,ped_prazo,ped_datahora,classificacao_data,classificacao_descricao,classificacao_id,usu_id,clijxf_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    try:
        cursor.execute(query, (pedido['status'],pedido['valor_total'],pedido['prazo'],getNow(),getDate(),pedido['descricao_classificacao'],pedido['class_usuario'],pedido['usuario'],pedido['cliente']))
        id = cursor.lastrowid
        cursor.close() # smcjxsmc
        con.commit()
        print('pedido add')
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        con.close()
        return id

for j in pedidos:
    id = setPedidos(j, j['produtos'])
    for i in j['produtos']:
        setProdutos(i, id)