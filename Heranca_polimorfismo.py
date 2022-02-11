from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_mes(self):
        pass    

    def __str__(self):
        return f'Codigo.: {self._codigo} Saldo.: {self._saldo}'

class ContaCorrente(Conta):
    def passa_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass


conta1 = ContaCorrente(1)
conta1.deposita(1000)
#conta1.passa_mes()
print(conta1)    

conta2 = ContaPoupanca(2)
conta2.deposita(1000)
#conta2.passa_mes()
print(conta2)

conta3 = ContaInvestimento(3)
print(conta3)

contas = [conta1, conta2]

for conta in contas:
    conta.passa_mes()
    print(conta)




