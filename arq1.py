idade1 = 39
idade2 = 30
idade3 = 27

print(idade1)
print(idade2)
print(idade3)

idades = [39,30,27,18]

print(idades)
print(len(idades))

idades.append(15)

print(idades)

idades.remove(30)
for idade in idades:
    print(idade)

print(28 in idades)
print(15 in idades)

idades.insert(0,20)
idades.extend([27, 19])
print(idades)

idade_qvem = []
for idade in idades:
    idade_qvem.append(idade+1)
print(idade_qvem)  

idade_qvem2 = [(idade+1) for idade in idades]
print(idade_qvem2)

idade_m21 = [(idade) for idade in idades if idade > 21]
print(idade_m21)

def proximo_ano(idade):
    return idade + 1

idade_qvem3 = [proximo_ano(idade) for idade in idades if idade > 21]  
print(idade_qvem3)  


