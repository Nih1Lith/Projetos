from exercicios_heranca import Banco
from exercicios_heranca import Veiculo

class Agencia(Banco):
    def __init__(self,nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, portas):
        super().__init__(marca, modelo)
        self._portas = portas
        self._cor = cor

    def __str__(self) -> str:
        status = 'ligado' if self._ligado else 'desligado'
        return f'{self._marca} | {self._modelo} | {self._portas} | {self._cor} | {status}'
    
    def ligar(self):
        print(f'O carro {self._modelo} está ligado')
    

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo, cor):
        super().__init__(marca, modelo)
        self._tipo = tipo
        self._cor = cor

    def __str__(self) -> str:
        return super().__str__(), f'{self._marca} | {self._modelo} | {self._tipo}'
    
    def ligar(self):
        print(f'A moto {self._modelo} está ligada')