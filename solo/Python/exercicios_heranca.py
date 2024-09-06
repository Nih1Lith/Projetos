class Banco:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def __str__(self) -> str:
        return f'{self._nome} | {self._endereco}'
    

class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self) -> str:
        status = 'ligado' if self._ligado else 'desligado'
        return f'{self._marca.ljust(20)} | {self._modelo.ljust(20)} | {status}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self) -> str:
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'{self._marca} | {self._modelo} | {self._portas} | {status}'
    

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self) -> str:
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'{self._marca} | {self._modelo} | {self._tipo} | {status}'