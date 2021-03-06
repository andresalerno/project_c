import pymysql

products = [{
    "id": 1,
    "nome": "Produto A",
    "valor": 160.00,
    "prazo": 30
},{
    "id": 2,
    "nome": "Produto B",
    "valor": 60.00,
    "prazo": 20
},{
    "id": 3,
    "nome": "Produto C",
    "valor": 300.00,
    "prazo": 30
},{
    "id": 4,
    "nome": "Produto D",
    "valor": 35.00,
    "prazo": 30
},{
    "id": 5,
    "nome": "Produto E",
    "valor": 11.20,
    "prazo": 50
},{
    "id": 6,
    "nome": "Produto F",
    "valor": 76.25,
    "prazo": 90
},{
    "id": 7,
    "nome": "Produto G",
    "valor": 106.12,
    "prazo": 160
},{
    "id": 8,
    "nome": "Produto H",
    "valor": 32.14,
    "prazo": 30
},{
    "id": 9,
    "nome": "Produto I",
    "valor": 13.17,
    "prazo": 30
},{
    "id": 10,
    "nome": "Produto J",
    "valor": 99.14,
    "prazo": 30
},{
    "id": 11,
    "nome": "Produto K",
    "valor": 746,
    "prazo": 30
},{
    "id": 12,
    "nome": "Produto L",
    "valor": 17564,
    "prazo": 30
},{
    "id": 13,
    "nome": "Produto M",
    "valor": 1245,
    "prazo": 30
},{
    "id": 14,
    "nome": "Produto N",
    "valor": 945.10,
    "prazo": 30
},{
    "id": 15,
    "nome": "Produto O",
    "valor": 75.47,
    "prazo": 30
}]

def connect():
    return pymysql.connect("198.199.73.180", "root", "aspartners2018", "credit_management")

def push(product):
    con = connect()
    cursor = con.cursor()

    query = "INSERT INTO tbl_produtos(prod_nome,prod_valor_unitario,prod_prazo) VALUES (%s,%s,%s)"

    try:
        cursor.execute(query, (product['nome'],product['valor'],product['prazo']))
        con.commit()
        print("sucess")
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        con.close()

for j in products:
    print(j['id'])
    push(j)