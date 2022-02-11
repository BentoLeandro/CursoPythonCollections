class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor  

    def __str__(self):
        return f'[>>Codigo.:{self.codigo} Saldo.:{self.saldo}<<]' 

conta_bento = ContaCorrente(12)
print(conta_bento)    
conta_bento.deposita(300)
print(conta_bento)

conta_mari = ContaCorrente(10)
conta_mari.deposita(500)
print(conta_mari)

conta_bento.deposita(100)

contas = [conta_bento, conta_mari, conta_bento]
print(contas)
for conta in contas:
    print(conta)

def deposita_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_bento, conta_mari]
print(contas[0], contas[1])
deposita_todas(contas)
print(contas[0], contas[1]) 

contas.insert(0, 47)
print(contas[0], contas[1], contas[2])

bento = ('Bento', 31, 1990)
mari  = ('Mari', 27, 1993)

def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

usuarios = [bento, mari]   
usuarios.append(('Paulo', 44, 1970))
print(usuarios) 

#usuarios[0][0] = 'Bento Teste'

print(usuarios[0][1])

contas_t = (conta_bento, conta_mari)
contas_t[0].deposita(1000)

for conta in contas_t:
    print(conta)


