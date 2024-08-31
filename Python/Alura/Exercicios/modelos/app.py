import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'cardapio')))

from cardapio.bebida import Bebida
from cardapio.prato import Prato
from restaurante import Restaurante


restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_pizza = Restaurante('pizza', 'italiana')

restaurante_praca.receber_avaliacao('nome',6)
restaurante_praca.receber_avaliacao('nome2',7)
restaurante_praca.receber_avaliacao('nome3',10)

restaurante_pizza.receber_avaliacao('nome4',3)

suco_1 = Bebida('Suco de Melancia', 5.0, 'Grande')
prato_1 = Prato('Pão', 2.0, 'O melhor pão da cidade')


def main():
    Restaurante.listar_restaurantes()
    print('')
    print(suco_1)
    print(prato_1)

if __name__ == '__main__':
    main()