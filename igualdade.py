class ContaCorrente():
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo = valor    

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):        
        return f'>>Código.: {self._codigo} Saldo.: {self._saldo}<<'

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

conta1 = ContaSalario(1)
conta1.deposita(500)

conta2 = ContaSalario(1)
conta2.deposita(500)

conta3 = ContaCorrente(1)
conta3.deposita(500)

print(f'Conta1 e igual a Conta2.: {conta1 == conta2}')
print(f'Conta1 e igual a Conta3.: {conta1 == conta3}')
