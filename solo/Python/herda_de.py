from exercicios_heranca import Banco
from exercicios_heranca import Veiculo
from exercicios_heranca import Carro
from exercicios_heranca import Moto


class Agencia(Banco):
    def __init__(self,nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero


    
conta_1 = Banco('nome', 'endereco')
carro_1 = Carro('marca1', 'modelo1', 4)
moto_1 = Moto('marca_moto', 'modelo_moto', 'Esportiva')

def main():
    print(conta_1)
    print('')
    print(carro_1)
    print('')
    print(moto_1)

if __name__ == '__main__':
    main()


# class Carro(Veiculo):
#     def __init__(self, marca, modelo, portas):
#         super().__init__(marca, modelo)
#         self._portas = portas

#     def __str__(self) -> str:
#         status = 'ligado' if self._ligado else 'desligado'
#         return f'{self._marca} | {self._modelo} | {self._portas} | {status}'
    

# class Moto(Veiculo):
#     def __init__(self, marca, modelo, tipo):
#         super().__init__(marca, modelo)
#         self._tipo = tipo

#     def __str__(self) -> str:
#         return super().__str__(), f'{self._marca} | {self._modelo} | {self._tipo}'