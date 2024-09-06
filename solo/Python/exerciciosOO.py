class Musica:
    def __init__(self, nome,artista, duracao):        
        self.nome = nome.title()
        self.artista = artista.title()
        self.duracao = duracao

musica1 = Musica(nome = '', artista = '', duracao = int)

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao

    def __str__(self) -> str:
        print(f'{'Nome:'.ljust(20)} | {'Idade:'.ljust(20)} | Profissão:')
        return f'{self.nome.ljust(20)} | {str(self.idade).ljust(20)} | {self.profissao}'
    
    def aniversario(self):
        self.idade+=1
    
    def saudacao(self):
        return f'Olá, sua profissão é {self.profissao}'
    
# pessoa = Pessoa(nome='nome',idade=20,profissao='tanto faz')
# print(pessoa)
# pessoa.aniversario()
# print(pessoa)
# print(pessoa.saudacao())

class ContaBancaria:
    contas = []
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self) -> str:
        return f'Titular: {self._titular} - Saldo: R${self._saldo}'
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
    def ativar_conta(self):
        self._ativo = True
        print('O titular está ativo')
    
    @classmethod
    def listar_titular(cls):
        print(f'{'Titular:'.ljust(20)} | {'Saldo:'.ljust(20)} | {'Status:'}')
        for titular in cls.contas:
            print(f'{titular._titular.ljust(20)} | R${str(titular._saldo).ljust(18)} | {titular._ativo}')
        print('')

class ClienteBanco:
    def __init__(self, nome, cpf, idade, endereco, tel):
        self._nome = nome.title()
        self._cpf = cpf
        self._idade = idade
        self._endereco = endereco
        self._tel = tel

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta


conta1 = ContaBancaria('nome', 5000)
print(conta1)
conta1.ativar_conta()

#ContaBancaria.listar_titular()

conta_cliente = ClienteBanco.criar_conta('nome2', 100)
print(conta_cliente)

#ContaBancaria.listar_titular()

class Livro:
    def __init__(self, titulo, autor, ano_publicado) -> None:
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True

    def __str__(self):
        #return f'{'Título:'.ljust(20)} | {'Autor:'.ljust(20)} | Ano de publicação:'
        return f'{self._titulo.ljust(20)} | {self._autor.ljust(20)} | {self._ano_publicado} | {'Disponível' if self._disponivel else 'Indisponível'}'
    
    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def  verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicado == ano and livro._disponivel]
        return livros_disponiveis
    
livro1 = Livro('titulo1', "autor1" , 1900)
livro2 = Livro('titulo2', 'autor2', 1940)
livro3 = Livro('titulo3', 'autor3', 1930)
    
Livro.livros = [livro1, livro2, livro3]