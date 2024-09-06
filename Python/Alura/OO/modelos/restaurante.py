# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'cardapio')))


from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        #".title()" deixa a primeira letra em maiúculo
        self._nome = nome.title()
        #".upper()" deixa todas letras maiúsculas
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        ##Todo restaurante criado vai para a lista restaurantes[], o append(self) irá adicionar
        # o próprio restaurante usando o self que está referenciando o próprio objeto
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self._nome} | {self._categoria}'
    
    #coolsymbols
    @property
    def ativo(self):
        return '☑ Ativo' if self._ativo else '☐ Desativado'

    #O @classmethod é um decorador que transforma um método em um método de classe, ou seja, ele recebe a classe como primeiro argumento, em vez de receber a instância da classe como acontece nos métodos normais. Isso permite que o método acesse e modifique atributos da classe em vez de trabalhar apenas com atributos da instância.
    # Principais Características:
    # O primeiro parâmetro de um método de classe é a classe, geralmente chamado de cls.
    # É útil para manipular ou acessar dados compartilhados por todas as instâncias da classe.
    # Não depende de uma instância da classe para ser chamado, pode ser invocado diretamente pela classe.
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome:'.ljust(25)} | {'Categoria:'.ljust(25)} | {'Avaliação:'.ljust(25)} | Status:')
        for restaurante in cls.restaurantes:
           print(f'{ restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante._ativo}')

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    def alternar_estado(self):
        self._ativo = not self._ativo

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_avaliacao = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media_avalicao = round(soma_avaliacao / len(self._avaliacao), 1)
        # if media_avalicao > 5:
        #     media_avalicao = 5
        return media_avalicao
    
    # def adicionar_bebida_cardapio(self, bebida):
    #     self._cardapio.append(bebida)

    # def adicionar_prato_cardapio(self, prato):
    #     self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        #A função isinstance() é usada para verificar se um objeto é de um determinado tipo ou classe. Ele retorna True se o objeto for uma instância do tipo/classe especificada, ou de uma subclasse dela.
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    #O decorador @property é utilizado para transformar um método de uma classe em uma propriedade que pode ser acessada como um atributo, sem a necessidade de parênteses.
    #Permite definir getters e setters (facilita o controle de acesso a atributos privados).
    #Com ele, você pode acessar um método como se fosse um atributo de instância, permitindo encapsular a lógica sem alterar a interface da classe.
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante: {self._nome}\n')
        for i,item in enumerate(self._cardapio, start=1):
            #A função hasattr() é usada para verificar se um objeto possui um determinado atributo. Ela retorna True se o objeto tiver o atributo e False caso contrário.
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)



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
