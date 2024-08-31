lista_nums = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = ['nome1','nome2','nome3','nome4']
lista_anos= [1996,2024]

cadastro = {'nome':'nomePessoa', 'idade':28, 'cidade':'Belford Roxo'}
print(cadastro)
print(cadastro['nome'])
cadastro['nome'] = 'Gabriel'
print(cadastro['nome'])
cadastro['profissão'] = 'profissão1'
print(cadastro)
del cadastro['cidade']
print(cadastro)

num_quadrado = {x: x**2 for x in range(1,6)}
print(num_quadrado)

print('sim, possui idade no dicionário') if 'idade' in cadastro else print('não possui idade no dicionário')

print(len(cadastro['a'.count]))

frase = 'Python tornou-se uma das linguagens de programação mais populares nos últimos anos'
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra]
print(contagem_palavras)


print('Array completo')
for i in lista_nums:
    print(i)
print()

soma = 0

for i in lista_nums:
    if(i%2 != 0):
        soma = i+soma
    i+=1
print(f'Soma dos números ímpares: {soma}')

#start = len(lista_nums) - 1
#end = -1
#step = -1
for i in range(len(lista_nums),-1,-1):
    #Opção a se fazer usando for i in range(len(lista_nums) -1,-1,-1):
    #print(lista_nums[i])
    #ou usando for i in range(len(lista_nums),-1,-1):
    print(i)

num = int(input('Digite um número: '))
for i in lista_nums:
    print(f'{num}x{i} = {num*i}')

try:
    for i in lista_nums:
        soma = 0
        soma+=i
    print(f'Soma dos elementos: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

try:
    for i in lista_nums:
        soma_valores = 0
        soma_valores += i
    media = soma_valores/len(lista_nums)
    print(f'Média dos valores: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
    