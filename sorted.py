from audioop import reverse


idades = [15, 87, 65, 56, 32, 49, 37]

print(idades) #original

print(sorted(idades)) #ordenação menor para o maior

print(sorted(idades, reverse=True)) #ordenação maior para o menor

print(list(reversed(idades))) #inverte a ordem dos valores 

idades.sort()
print(f'Lista original alterada.: {idades}')
