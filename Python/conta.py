from operator import attrgetter
from functools import total_ordering


class Conta:
    def __init__(self, conta):
        self._conta = conta
        self._saldo = 0

    def deposita(self, valor):
        self._saldo = valor

    def __str__(self):
        return f"[>>Conta{self._conta} - Saldo{self._saldo}<<]"


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

@total_ordering
class ContaSalario(Conta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return  False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>Código: {self._codigo} -- Saldo: {self._saldo}]"

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

conta_do_guilherme = ContaSalario(20)
conta_do_guilherme.deposita(500)
conta_da_daniela = ContaSalario(19)
conta_da_daniela.deposita(1000)
conta_do_paulo = ContaSalario(18)
conta_do_paulo.deposita(510)
contas_salario = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in contas:
    conta.passa_o_mes()
    print(conta)

for conta in sorted(contas_salario, key=attrgetter("_codigo")): #Quebrando encapsulamento do objeto privado
    print(conta)

for conta in sorted(contas_salario): # Sem quebrar usando o __lt__(less than)
    print(conta)

for conta in sorted(contas_salario, reverse=True):
    print(conta)