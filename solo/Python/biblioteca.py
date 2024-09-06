from exerciciosOO import Livro

livro_main = Livro('livroMain1', 'autorMain', 2000)


print(livro_main)
livro_main.emprestar()
print(livro_main)


ano_especifico = 1940

livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)


def main():
    print('Biblioteca')
    print(f'Livros disponíveis - {livros_disponiveis_ano}')

if __name__ == '__main__':
    main()