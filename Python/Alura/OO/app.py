import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'cardapio')))

from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.restaurante import Restaurante


restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_pizza = Restaurante('pizza', 'italiana')

restaurante_praca.receber_avaliacao('nome',6)
restaurante_praca.receber_avaliacao('nome2',7)
restaurante_praca.receber_avaliacao('nome3',10)

restaurante_pizza.receber_avaliacao('nome4',3)

suco_1 = Bebida('Suco de Melancia', 5.0, 'Grande')
prato_1 = Prato('Pão', 2.0, 'O melhor pão da cidade')

#print(f'{suco_1._nome} | {suco_1._preco} | {suco_1._tamanho}')
restaurante_praca.adicionar_no_cardapio(suco_1)
restaurante_praca.adicionar_no_cardapio(prato_1)
suco_1.aplicar_desconto()
prato_1.aplicar_desconto()

#print(restaurante_praca.exibir_cardapio())
def main():
    #Restaurante.listar_restaurantes()
    # print('')
    # print(suco_1)
    # print(prato_1)
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()