from avaliacao import Avaliacao
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        #".title()" deixa a primeira letra em maiúculo
        self._nome = nome.title()
        #".upper()" deixa todas letras maiúsculas
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        ##Todo restaurante criado vai para a lista restaurantes[], o append(self) irá adicionar
        # o próprio restaurante usando o self que está referenciando o próprio objeto
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self._nome} | {self._categoria}'
    
    #coolsymbols
    @property
    def ativo(self):
        return '☑ Ativo' if self._ativo else '☐ Desativado'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome:'.ljust(25)} | {'Categoria:'.ljust(25)} | {'Avaliação:'.ljust(25)} | Status:')
        for restaurante in cls.restaurantes:
           print(f'{ restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante._ativo}')

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_avaliacao = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media_avalicao = round(soma_avaliacao / len(self._avaliacao), 1)
        # if media_avalicao > 5:
        #     media_avalicao = 5
        return media_avalicao


#Desafios
#restaurante_praca.nome = 'Praça'
#restaurante_praca.categoria = 'Italiana'

#restaurantes = [restaurante_pizza, restaurante_praca]

#print(f'Categoria: {restaurante_praca.categoria}')
#print(f'O restaurante {restaurante_praca.nome} está ativo') if restaurante_praca.ativo else print(f'O restaurante {restaurante_praca.nome} está desativado')

#categoria = Restaurante.categoria
#restaurante_praca.nome = 'Bistrô'

#restaurante_pizza.nome = 'Pizza Place'
#restaurante_pizza.categoria = 'Fast Food'

#print(f'Categoria: {restaurante_pizza.categoria}')
#restaurante_pizza.ativo = True
#print(f'Nome: {restaurante_praca.nome} - Categoria: {restaurante_praca.categoria}')
