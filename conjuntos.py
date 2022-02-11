from posixpath import split
from collections import defaultdict, Counter


usua_data_science = [15, 23, 43, 56]
usua_machine_learning = [13, 23, 56, 42]

assistiram = usua_data_science.copy()
assistiram.extend(usua_machine_learning)

print(assistiram)
print(len(assistiram))

print(set(assistiram))

for usuario in set(assistiram):
    print(usuario)

conjunto1 = {15, 23, 43, 56} 
conjunto2 = {13, 23, 56, 42}  

#O Pipe faz a função do extend da lista.. 
# ele junta os 2 conjuntos e exclui os duplicados
print(conjunto1 | conjunto2)

#O &(and) retornar os numeros que estão nos dois conjuntos..
#e exclui outros
print(conjunto1 & conjunto2)

#O menos retorna somente os numeros do conjunto1 que não estão no conjunto2
print(conjunto1 - conjunto2)

fez_ds_nfez_ml = conjunto1 - conjunto2

for usuario in fez_ds_nfez_ml:
    print(usuario)

#Por padrão os conjuntos no python são mutaveis 
# é possivel adicionar, alterar e excluir elementos dentro do conjunto
usuarios = {1, 2, 3, 4, 5, 99}
usuarios.add(78)
for usuario in usuarios:
    print(usuario)    

#usuarios = frozenset(usuarios)    
#usuarios.add(451)

texto = "Leandro Reis Bento teste de split Bento Leandro"

print(set(texto.split()))

valor = {
    "Leandro": 1,
    "Reis": 1,
    "Bento": 2
}

print(type(valor))
print(valor["Leandro"])
print(valor.get("xxx",0)) #quando não sabemos se a chave existe, podemos 
                          #utilizar o get para passar um valor Default

#criando dicionarios
valor2 = dict(Leandro = 2, Bento = 3, Teste = "Texto padrão")
print(valor2)      

#adiciona novos elementos no dicionario
valor2["Total"] = 10.58
print(valor2)

#alterando um valor de uma chave
valor2["Total"] = 12.96
print(valor2)

#deletando uma chave
del valor2["Total"]
print(valor2)

#verificando se a chave existe no dicionario
print("Leandro" in valor2)

#interar com todos as chaves do elemento no dicionario
for chave in valor2.keys():
    print(chave)

#interar com todos os valores do elemento no dicionario
for valor in valor2.values():
    print(valor)    

#intera com a chave e o valor do dicionario
for chave, valor in valor2.items():
    print(chave, "=", valor)    

#compressao de lista com dicionario
lista = [f'Palavra.: {chave}' for chave in valor2.keys()]
print(lista)

meu_texto = "Bem vindo meu nome e Leandro eu gosto muito de nome e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

print(meu_texto.split())

aparicoes = {}
qtde = 0
for palavra in meu_texto.split():
    qtde = aparicoes.get(palavra, 0)
    aparicoes[palavra] = qtde + 1 

print(aparicoes)    

aparicoes = defaultdict(int)
qtde = 0
for palavra in meu_texto.split():
    qtde = aparicoes[palavra]
    aparicoes[palavra] = qtde + 1

for palavra in aparicoes.items():
    print(palavra)


aparicoes = defaultdict(int)
for palavra in meu_texto.split():   
    aparicoes[palavra] += 1

for palavra in aparicoes.items():
    print(palavra)


class Conta:
    def __init__(self):
        print("Criando uma Conta")

contas = defaultdict(Conta)

contas[15]
print(contas)

#o contador já faz a validação da chave e verifica a 
#quantidade de vezes que a chave aparece no texto
meu_texto = "Bem vindo meu nome e Leandro eu gosto muito de nome e tenho o meu cachorro e gosto muito de cachorro"
aparicoes = Counter(meu_texto.split())
print(aparicoes)    

