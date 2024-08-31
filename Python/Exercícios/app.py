from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_pizza = Restaurante('pizza', 'italiana')

restaurante_praca.receber_avaliacao('nome',6)
restaurante_praca.receber_avaliacao('nome2',7)
restaurante_praca.receber_avaliacao('nome3',10)

# restaurante_pizza.receber_avaliacao('nome4',3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()