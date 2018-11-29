import pymysql

class Connection:
    def connect(self):
        return pymysql.connect("198.199.73.180", "root", "aspartners2018", "credit_management")

    def read(self):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM produto")
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    # Retorna dados para comparacao de login/senha do vendedor
    def getUserData(self):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT sm_email, sm_password, sm_id, acc_id FROM tb_salesman")
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def getClient(self, id):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT smc_name FROM tb_salesmanClient WHERE smc_id = %s", id)
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def getClientForName(self, companyName):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM tb_salesmanClientJuristical WHERE smcj_name LIKE %s", '%'+companyName+'%')
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def getPessoaFisicaForName(self, name):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM tb_salesmanClient WHERE smc_name LIKE %s", '%'+name+'%')
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def getPessoaFisicaForCpf(self, cpf):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM tb_salesmanClient WHERE smc_cpf LIKE %s", cpf)
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def getClientForCnpj(self, cnpj):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM tb_salesmanClientJuristical WHERE smcj_cnpj LIKE %s", cnpj)
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    # Retorna os dados de clientes pelo id do vendedor
    def getClients(self, salesmanId):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM tb_salesmanClient WHERE sm_id = %s", salesmanId)
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def getProducts(self):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM tb_products")
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def getProductsForId(self, productsId):
        con = Connection.connect(self)
        cursor = con.cursor()
        format_strings = ','.join(['%s'] * len(productsId))

        try:
            cursor.execute("SELECT pd_id, pd_name, pd_unit_value FROM tb_products WHERE pd_id IN (%s)" % format_strings, tuple(productsId))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def getProductsInCampaign(self):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            # Refatorar a query e acrescentar o WHERE que filtre as campanhas. Campanha.DateBegin <= Date.now <= Campanha.DateEnd
            cursor.execute("SELECT pd_id, cp_name, cp_desconto FROM tb_productsInCampaign p JOIN tb_campaign c ON p.cp_id = c.cp_id;")
            # WHERE Date.now >= c.cp_dataInicio
            # AND Date.now <= c.cp_dataTermino;
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def setRequest(self, info, products):
        con = Connection.connect(self)
        cursor = con.cursor()

        print(info)
        print(products)

        query = "INSERT INTO tb_requestDecided (smc_id,sm_id,rd_dateApproveReject,fl_id,rd_ApproveRejectId,ra_id,pd_id,rd_amount,rd_total_value,rd_prazo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";

        print(query)

        try:
            cursor.execute(query, (info['idClient'], info['idSalesman'], info['dateApproveDesapprove'], info['isApprove'], info['idWhoApprove'], info['idReasons'], products['idProduct'], products['amount'], products['liquidValue'], products['time']))
            con.commit()
            print("success")
        except Error as e:
            con.rollback()
            print(e)
        finally:
            con.close()

    def add(self, data):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("")
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("")
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Connection.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("")
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
