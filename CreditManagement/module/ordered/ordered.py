from flask import session
from datetime import datetime

from ..connection import Connection

con = Connection()

def getClientsName(companyName):
    companies = con.getClientForName(companyName)

    return companies

def getClientCnpj(cnpj):
    companies = con.getClientForCnpj(cnpj)

    return companies

def getPessoaFisicaName(name):
    companies = con.getPessoaFisicaForName(name)

    return companies

def getPessoaFisicaCpf(cpf):
    companies = con.getPessoaFisicaForCpf(cpf)

    return companies

def getClientsInfo():
    id = session['id']

    clients = con.getClients(id)
    return clients

def getProductsInfo():
    products = con.getProducts()
    return products

def getClient(id):
    client = con.getClient(id)
    return client

def getProductsCampaignInfo(sales):
    detailOrdered = {
        'idSalesman': session['id'],
        'idClient': sales[0],
        'products': []
    }

    productsCampaign = con.getProductsInCampaign()

    for k in range(1, len(sales)):
        for i in range(0, len(productsCampaign)):
            if(int(sales[k]) == int(productsCampaign[i][0])): # Colocando os produtos no dict com nome e desconto caso tenha
                detailOrdered['products'].append({
                    'productId': sales[k],
                    'discount': productsCampaign[i][2]
                })
                break;
            else:
                if(i == len(productsCampaign)-1):
                    detailOrdered['products'].append({
                        'productId': sales[k],
                        'discount': 0
                    })

    return detailOrdered

def getAllProducts(sales):
    del sales[0]

    products = con.getProductsForId(sales)

    return products

def addRequest(data):
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d')
    info = {
      'idClient': data['idClient'],
      'idSalesman': data['idSalesman'],
      'dateApproveDesapprove': formatted_date,
      'isApprove': data['isApprove'],
      'idWhoApprove': data['idWhoApprove'],
      'idReasons': data['idReasons'],
    }

    for k in data['products']:
        con.setRequest(info, k)
