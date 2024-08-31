import os

restaurantes = [{'nome':'Sushi', 'categoria':'Japonesa', 'ativo':True},
                {'nome':'Pizza', 'categoria':'Italiana', 'ativo': False},
]

def titulo_app():
    #fsymbols abaixo.
    '''Usa estilização para mostrar o título do app'''
    print('s̝̙a͇͚̠b̫͚͜o͇̘̠r̟̻ e̙̫͚x͚̙̙p̻̺̫r͉̼̟e̻̝s͓̫s͔̼\n')

def exibir_subtitulo(texto):
    '''Limpa a tela e mostra o subtítulo da opção escolhida'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    os.system('cls')
    print('opção inválida.')
    voltar_ao_menu_principal()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar Restaurante.')
    nome_restaurante = input('Digite o nome do restaurante:\n')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso.')
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    exibir_subtitulo('Alterando Estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar: ')
    #status_restaurante = False
    for restaurante in restaurantes:
        if(nome_restaurante == restaurante['nome']):
            #status_restaurante = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
        if (nome_restaurante != restaurante['nome']):
            print(f'Restaurante {nome_restaurante} não encontrado.')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes.')
    print(f'{'Nome do Restaurante'.ljust(22)} {'Categoria'.ljust(20)} {'Status'.ljust(20)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        #Usando match ao invés de if, elif e else.
        match opcao:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    titulo_app()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()