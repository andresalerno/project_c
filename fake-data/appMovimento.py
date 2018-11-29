import pymysql

movimento = [{
    "cod_transacao": "100059620000104100920181428",
    "ped_id": 1,
    "clijxf_id": 2,
    "usu_id": 1,
    "rpz_id": 0
}]

def connect():
    return pymysql.connect("198.199.73.180", "root", "aspartners2018", "credit_management")


def setMov(mov):
    con = connect()
    cursor = con.cursor()

    query = "INSERT INTO tbl_movimento (cod_transacao,ped_id,clijxf_id,usu_id,rpz_id) VALUES (%s,%s,%s,%s,%s)"

    try:
        cursor.execute(query, (mov['cod_transacao'],mov['ped_id'],mov['clijxf_id'],mov['usu_id'],mov['rpz_id']))
        print(cursor)
        con.commit()
        print("pedido pago")
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        con.close()

for j in movimento:
    setMov(j)