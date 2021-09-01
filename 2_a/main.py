from conta_bancaria import ContaBancaria
from conta_bancaria import ContaPoupanca
from conta_bancaria import ContaCorrente

class main:
    def __init__(self):
        self.contas_poupanca = []
        self.contas_corrente = []
        self.contas = []

    def principal(self):
        menu = "0"
        while menu != "99":
            print("-----------menu--------------")
            print("Cadastrar Conta Poupança - 1 |")
            print("Cadastrar Conta Corrente - 2 |")
            print("Aumentar Limite - 3          |")
            print("Realizar Depósito - 4        |")
            print("Realizar Saque - 5           |")
            print("Listar Contas - 6            |")
            print("Sair do Menu - 99            |")
            print("------------------------------")
            menu = input("informe a opção desejada: ")

            if(menu == "1"):
                titular = input("Informe o Titular da conta: ")
                conta = input("Informe o numero da conta: ")
                nova_conta = ContaPoupanca()
                nova_conta.titular_bancaria = titular
                nova_conta.conta_bancaria = conta
                nova_conta.saldo = 0
                self.contas.append(nova_conta)
                print("Conta Poupança Cadastrada com sucesso")

            if(menu == "2"):
                titular = input("Informe o Titular da conta: ")
                conta = input("Informe o numero da conta: ")
                limite = input("Qual o limite permitido: ")
                nova_conta = ContaCorrente()
                nova_conta.titular_bancaria = titular
                nova_conta.conta_bancaria = conta
                nova_conta.saldo = 0
                nova_conta.limite_credito = limite
                self.contas.append(nova_conta)
                print("Conta Corrente Cadastrada com sucesso")

            if(menu == "3"):
                conta = input("Qual conta pretende alterar o limite? ")
                novo_limite = input("Qual o novo limite? ")
                contador = -1
                for i in self.contas:
                    contador += 1
                    if(i.conta_bancaria == conta):
                        #ContaCorrente.v_aumenta_limite(novo_limite)
                        x = ContaCorrente()
                        x.saldo = i.saldo
                        x.conta_bancaria = i.conta_bancaria
                        x.titular_bancaria = i.titular_bancaria
                        x.v_aumenta_limite(novo_limite)
                        self.contas[contador] = x

            if(menu == "4"):
                conta = input("Qual conta pretende depositar? ")
                novo_limite = input("Qual o valor do deposito? ")
                contador = -1
                for i in self.contas:
                    contador += 1
                    if(i.conta_bancaria == conta):
                        #ContaCorrente.v_aumenta_limite(novo_limite)

                        if(i.tipo == "p"):
                            x = ContaPoupanca()
                        else:
                            x = ContaCorrente()
                            x.limite_credito = i.limite_credito

                        x.saldo = i.saldo
                        x.conta_bancaria = i.conta_bancaria
                        x.titular_bancaria = i.titular_bancaria
                        x.v_deposito(int(novo_limite))
                        self.contas[contador] = x

            if(menu == "5"):
                conta = input("Qual conta pretende sacar? ")
                novo_limite = input("Qual o valor do saque? ")
                contador = -1
                for i in self.contas:
                    contador += 1
                    if(i.conta_bancaria == conta):
                        #ContaCorrente.v_aumenta_limite(novo_limite)

                        if(i.tipo == "p"):
                            x = ContaPoupanca()
                        else:
                            x = ContaCorrente()
                            x.limite_credito = i.limite_credito

                        x.saldo = i.saldo
                        x.conta_bancaria = i.conta_bancaria
                        x.titular_bancaria = i.titular_bancaria
                        if(i.tipo == "p"):
                            if(i.saldo >= int(novo_limite)):
                                x.v_saque(int(novo_limite))
                            else:
                                print("Saldo insuficiente para o Saque! ")
                        else:
                            if((int(i.saldo) + int(i.limite_credito)) >= int(novo_limite)):
                                x.v_saque(int(novo_limite))
                            else:
                                print("Saldo insuficiente para o Saque! ")
                        self.contas[contador] = x

            if(menu == "6"):
                for i in self.contas:
                    print("-----------")
                    print("conta: " + i.conta_bancaria)
                    if(i.tipo == "c"):
                        print("limite: " + i.limite_credito)
                    print("Conta: " + i.tipo)
                    print("Saldo: " + str(i.saldo))
                    print("-------------")


main().principal()
