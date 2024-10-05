import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
            
        dados_restaurante[nome_restaurante].append({'item': item['Item'],
                                                        'price': item['price'],
                                                        'descricao': item['description']})
else:
    print(f'O erro foi {response.status_code}')

# print(dados_restaurante["McDonald’s"])

#O método "items()" retorna um objeto view. O objeto view contém os pares chave-valor do dicionário, como tuplas em uma lista.
for nome_restaurante, dados in dados_restaurante.items():
    #Json é uma sintaxe para armazenar e trocar dados.
    #Json é texto escrito com notação de objeto JavaScript
    nome_arquivo = f'{nome_restaurante}.json'
    #A função "open" é utilizada para abrir arquivos em Python, podendo especificar o modo de abertura read - 'r', write - 'w' ou append - 'a'. O retorno de open é um objeto de arquivo que pode ser manipulado para ler e gravar dados. É necessário fechar o arquivo no fim com "close().
    #O "with" é uma maneira de simplificar o uso de recursos que precisam ser inicializados e finalizados(ex., arquvios, conexões de rede, etc.). Quando usa-se o "with", não é necessário se preocupar em fechar o arquivo manualmente.
    #O uso de "with" com "open" é a maneira mais comum e recomendada de manipular arquivos em Python. Ao usar "with", você garante que o arquivo será aberto e, ao final da operação, será fechado automaticamente, mesmo se ocorrerem erros.
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        #O "json.dump" é utilizado para gravar dados no formato JSON diretamente em um arquivo. Ele recebe dois parâmetros principais: os dados(normalmente um dicionário ou lista) e o objeto de arquivo no qual os dados serão gravados.
        #Enquanto "json.dump" grava diretamente em um arquivo, "json.dumps" converte os dados em uma string JSON, que pode ser manipulada diretamente no código.
        json.dump(dados, arquivo_restaurante, indent=4)