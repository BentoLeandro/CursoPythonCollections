from audioop import reverse
from operator import attrgetter
from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'>>Código.: {self._codigo} Salario.: {self._saldo}<<'

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo        

conta1 = ContaSalario(100)
conta1.deposita(510)

conta2 = ContaSalario(2)
conta2.deposita(1000)

conta3 = ContaSalario(33)
conta3.deposita(510)

contas = [conta1, conta2, conta3]

#for conta in contas:
#    print(conta)

def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas):
    print(conta)

print(conta1 > conta1)

