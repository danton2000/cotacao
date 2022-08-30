import requests

# url da api
url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

# variavel que recebe as resposta da api
resposta = requests.get(url)
print(resposta)

# pegar os dados da respota [json]
dados_resposta = resposta.json()
print(dados_resposta['USDBRL'])

print('Cotação:', dados_resposta['USDBRL']['bid'])