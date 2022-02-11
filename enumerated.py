import enum


idades = [15, 87, 65, 56, 32, 49, 37]

for idade in idades:
    print(idade)

for i in range(len(idades)):
    print(i, idades[i])

print(list(range(len(idades))))

print(list(enumerate(idades)))

for pos, valor in enumerate(idades):
    print(pos, valor)

for valor in enumerate(idades):
    print(valor)   

usuarios = [
    ("Bento", 31, 1990),
    ("Maria", 27, 1994),
    ("JesT", 28, 1993)
]     

for nome, idade, nasc in usuarios: # já desempacotando
    print(nome, idade, nasc)

for _, idade, _ in usuarios: # desempacotando somente as informações necessarias
    print(idade)

