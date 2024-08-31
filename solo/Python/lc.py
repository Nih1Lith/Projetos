import random

lista = []
counter = 0
while counter < 5:
    lista.append(random.randrange(1,100))
    for num in lista:
        if num == num in lista:
            num+=1
        elif num == num in lista:
            num+=2
    print(sorted(lista))
    counter+=1

print(sorted(lista))
print(range(len(lista)))
#'range(len(lista))' irá iterar sobre cada objeto dentro da lista (0,n-1)
for x in range(len(lista)):
    for y in range(x+1, len(lista)):
        num1 = lista[x]
        num2 = lista[y]        
    soma = num1 + num2
print(f'A soma de {num1} + {num2} é maior que 100' if soma > 100 else f'A soma de {num1} + {num2} não é maior que 100')
