import random

num = int(input("Digite um número: "))
lista_numeros = []
qtd_numeros = 0
while(qtd_numeros < num):
    num_aleatorio = random.randrange(1,100)
    lista_numeros.append(num_aleatorio)
    qtd_numeros += 1
print(len(lista_numeros))
print(sorted(lista_numeros))


#random.randint, escolhe um número aleatório dentro de uma sequência entre (x,y)
print(random.randint(1,10))

#random.choice, escolhe um item aleatório dentro de uma sequência
print (f"o número {random.choice(lista_numeros)} x {num} é igual a {random.choice(lista_numeros)*num}")


def lista():
    lista_nums = []
    num = int(input("Digite um número entre 0 e 100: "))
    qtd_numeros = 0
    while (qtd_numeros < num):
        num_aleatorio = random.randrange(1,100)
        lista_nums.append(num_aleatorio)
        qtd_numeros += 1
    print(sorted(lista_nums))

    for i in lista_nums ():
        #Escolher o maior ou menor dentro da lista
        #num_aleatorio = random.choice(lista_nums)
        pass


def lista2():
    num = int(input(f"Lista2 - Digite um número entre 0 e 100: "))
    while(num > 100 or num < 0):
        num = int(input(f"Lista2 - O número digitado foi {num}, digite um número válido: "))
    print(f"O número digitado multiplicado por 2 é {num*2}")
lista2()
