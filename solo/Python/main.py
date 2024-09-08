from exercicios_heranca import Banco
from herda_de import Carro
from herda_de import Moto


conta_1 = Banco('nome', 'endereco')
carro_1 = Carro(marca = 'marca1', modelo = 'modelo1', cor = 'preto', portas = 4)
print(f'{carro_1._marca} | {carro_1._modelo} | {carro_1._cor} | {carro_1._portas}')
moto_1 = Moto('marca_moto', 'modelo_moto', 'Esportiva', 'azul')