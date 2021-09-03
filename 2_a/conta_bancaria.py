class ContaBancaria:
    def __init__(self):
        self.titular_bancaria = ""
        self.conta_bancaria = ""
        self.saldo = 0

    def v_deposito(self, valor):
        self.saldo += valor

    def v_saque(self, menos):
        self.saldo -= menos

class ContaPoupanca(ContaBancaria):
    def __init__(self):
        self.tipo = "p"


class ContaCorrente(ContaBancaria):
    def __init__(self):
        self.tipo = "c"
        self.limite_credito = 0

    def v_aumenta_limite(self, alteracao):
        self.limite_credito = alteracao
