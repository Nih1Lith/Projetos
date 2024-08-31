idades = [15,87,65,56,32,49,37]
print(range(len(idades)))

for i in range(len(idades)):
    print(i, idades[i])

for valor in enumerate(idades):
    print(valor)

for indice, idade in enumerate(idades):
    print(indice, "--", idade)

usuarios = [("Guilherme", 37, 1981), ("Daniela", 31, 1987), ("Paulo", 39, 1979)]
for nome, idade, nascimento in usuarios:
    print(nome)


print(sorted(idades))

print(sorted(idades, reverse=True))

nomes = ["Guilherme", "carlos", "Daniela", "Paulo"]
print(sorted(nomes))
