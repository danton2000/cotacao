from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def busca_cep():

    if request.method == 'POST':

        cep = request.form['cep']

        url = f"https://cep.awesomeapi.com.br/json/{cep}"

        resposta = requests.get(url)

        # print(resposta)

        resultado_api = resposta.json()

        print(resultado_api)

        cidade = resultado_api["city"]

        endereco = resultado_api["address"]

        estado = resultado_api["state"]

        return render_template('index.html', cep=cep, cidade=cidade, estado=estado, endereco=endereco)

    return render_template("index.html")
