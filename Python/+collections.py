from collections import defaultdict
from collections import Counter

usuarios_data_science = [15, 43, 23, 56]
usuarios_machine_learning = [12, 23, 56, 42]
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)
print(sorted(assistiram))
print(sorted(set(assistiram)))
usuarios = (usuarios_machine_learning, usuarios_data_science)
print(usuarios)
usuarios = [1, 5, 13, 17, 34, 52, 76]
print(len(usuarios))
print(usuarios)
usuarios.append(765)
print(len(usuarios))
print(usuarios)

usuarios = frozenset(usuarios)
type(usuarios)

num = [3, 2, 6, 5, 9]
num2 = [1, 4, 3, 7, 5, 8]

print(sorted(set(num).intersection(num2)))

aparicoes = {"guilherme": 1, "cachorro": 2, "nome": 2, "vindo": 1}
type(aparicoes)
print(aparicoes["guilherme"])
aparicoes2 = dict(Guilherme=2, cachorro=1)
print(aparicoes2)
aparicoes["carlos"] = 1
print(aparicoes)
del aparicoes["carlos"]
print(aparicoes)

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento, aparicoes[elemento])

for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, "=", valor)

for elemento in aparicoes.items():
    print(elemento)

print([f"palavra {chave}" for chave in aparicoes.keys()])

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
print(meu_texto.lower())

aparicoes_palavra = {}
for palavra in meu_texto.split():
    ate_agora = aparicoes_palavra.get(palavra, 0)
    aparicoes_palavra[palavra] = ate_agora + 1
print(aparicoes_palavra)

aparicoes_palavra = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes_palavra[palavra] += 1
print(aparicoes_palavra)


aparicoes_palavra = Counter(meu_texto.split())
print(aparicoes_palavra)

print(Counter(meu_texto).most_common(10))
print(aparicoes_palavra.most_common(10))
