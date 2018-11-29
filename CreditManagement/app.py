from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, redirect, url_for
from module.connection import Connection
from module.auth import *
from module.ordered.ordered import *
import os
import json
from generateBoleto import *
from datetime import datetime

app = Flask(__name__)
db = Connection()

@app.route('/', methods=["GET","POST"])
def goLogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email != None and password != None:
            res = isLoginValid(email, password)
            if res['response']:
                session['logged_in'] = True
                session['id'] = res['id']
                session['access'] = res['access']
                return redirect(url_for('goDashboard'))
            else:
                return '<h1>Deu n o login bixo</h1>'
        else:
            flash('Password or email is null')
    return render_template('login.html')

# Searchs
@app.route("/searchClient", methods=["GET","POST"])
def goSearchClient():
    end = ""
    res = session['access']
    res = int(res)

    if not session.get('logged_in'):
        return redirect(url_for("goLogin"))
    else:
        end = "pessoaJuridica"
        return render_template('searchClient.html', end=end)

@app.route("/searchClientJ/<string:data>", methods=["GET","POST"])
def goSearchClientJ(data):
    end = ""
    res = session['access']
    res = int(res)

    print(data)

    if not session.get('logged_in'):
        return redirect(url_for("goLogin"))
    else:
        end = "pessoaJuridica"
        return render_template('searchClient.html', end=end, companies=getClientsName(data))

@app.route("/searchClientF/<string:data>", methods=["GET","POST"])
def goSearchClientF(data):
    end = ""
    res = session['access']
    res = int(res)

    print(data)

    if not session.get('logged_in'):
        return redirect(url_for("goLogin"))
    else:
        end = "pessoaJuridica"
        return render_template('searchClient.html', end=end, companies=getClientCnpj(data))

@app.route("/pessoaFisica", methods=["GET", "POST"])
def goSearchClientFisica():
    end = ""
    res = session['access']
    res = int(res)

    if not session.get('logged_in'):
        return redirect(url_for("goLogin"))
    else:
        end = "pessoaFisica"
        return render_template('searchClient.html', end=end)

@app.route("/pessoaFisicaName/<string:data>", methods=["GET", "POST"])
def goSearchClientFisicaName(data):
    end = ""
    res = session['access']
    res = int(res)

    if not session.get('logged_in'):
        return redirect(url_for("goLogin"))
    else:
        end = "pessoaFisica"
        return render_template('searchClient.html', end=end, companies=getPessoaFisicaName(data))

@app.route("/pessoaFisicaCpf/<string:data>", methods=["GET", "POST"])
def goSearchClientFisicaCpf(data):
    end = ""
    res = session['access']
    res = int(res)

    if not session.get('logged_in'):
        return redirect(url_for("goLogin"))
    else:
        end = "pessoaFisica"
        return render_template('searchClient.html', end=end, companies=getPessoaFisicaCpf(data))

# Requests clients
@app.route('/dashboard', methods=["GET", "POST"])
def goDashboard():
    end = " "
    res = session['access']
    res = int(res)

    if not session.get('logged_in'):
        return redirect(url_for("goLogin"))
    else:
        if res == 1:
            end = 'body-gestorCredito'
        elif res == 5:
            end = 'body-vendedor1'
        return render_template('dashboard.html', end=end)

@app.route('/request/client', methods=["GET", "POST"])
def goRequestClient():
    end = " "
    res = session['access']
    res = int(res)

    if not session.get('logged_in'):
        return redirect(url_for("goLogin"))
    else:
        end = 'requestClient'
        return render_template('dashboard.html', end=end, listClients=getClientsInfo())

@app.route('/product/<int:id>', methods=["GET", "POST"])
def goRequestProduct(id):
    if not session.get('logged_in'):
        return redirect(url_for("goLogin"))
    else:
        end = 'requestProduct'
        return render_template('dashboard.html', end=end, listProducts=getProductsInfo())

@app.route('/detail/<string:data>', methods=["GET", "POST"])
def goRequestDetail(data):

    data = convertToJson(data)

    if not session.get('logged_in'):
        return redirect(url_for("goLogin"))
    else:
        end = 'requestDetail'
        productsCampaign=getProductsCampaignInfo(data)
        return render_template('dashboard.html', end=end, data=data, productsCampaign=productsCampaign, allProducts=getAllProducts(data))

def convertToJson(data):
    data = data[0:len(data)-1].split('+')
    return data

@app.route("/finish", methods=["POST"])
def goFinishRequest():
    data = request.get_json(force=True)
    addRequest(data)

    now = datetime.now()
    formatted_date = now.strftime('%d/%m/%Y')

    aux = conversor(data['products'])

    print(getClient(data['idClient'])[0][0])

    print_bb(aux[1], aux[0], getClient(data['idClient'])[0][0])
    end='finishRequest'
    return render_template('dashboard.html', end=end)

def conversor(data):
    total = 0;
    prazo = 99999999;

    for k in data:
        total = total + int(k['liquidValue'])
        if(prazo > int(k['time'])):
            prazo = int(k['time'])
    return [total, prazo]

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for("goLogin"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.secret_key = 'g93rjgibrtnj98ruj9aw'
    app.run('0.0.0.0', port=port)
    app.run(debug=True)
