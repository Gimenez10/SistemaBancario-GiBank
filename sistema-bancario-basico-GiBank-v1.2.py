from datetime import datetime

class GiBank:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        nome = input("Digite o nome do usu�rio: ")
        data_nascimento = input("Digite a data de nascimento (formato dd/mm/aaaa): ")
        cpf = input("Digite o CPF do usu�rio: ")
        endereco = input("Digite o endere�o do usu�rio: ")
        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        print("Usu�rio criado com sucesso.")
        return usuario

    def criar_conta_corrente(self, usuario):
        conta = ContaCorrente(usuario)
        self.contas.append(conta)
        print("Conta corrente criada com sucesso.")
        return conta

    def depositar(self, conta, valor):
        conta.saldo, conta.depositos = self._realizar_deposito(conta.saldo, valor, conta.depositos)
        print(f"Dep�sito de R$ {valor:.2f} realizado com sucesso.")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")

    def sacar(self, conta, valor):
        conta.saldo, conta.saques, conta.saques_diarios = self._realizar_saque(
            conta.saldo, valor, conta.saques, conta.saques_diarios)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")

    def extrato(self, conta):
        print("\nExtrato:")
        for operacao in conta.depositos + conta.saques:
            print(operacao)
        print(f"Saldo atual: R$ {conta.saldo:.2f}")

    def _realizar_deposito(self, saldo, valor, extrato):
        if valor > 0:
            saldo += valor
            extrato.append(f"Dep�sito de R$ {valor:.2f}")
            return saldo, extrato
        else:
            print("N�o foi poss�vel realizar o dep�sito, o valor deve ser positivo.")
            return saldo, extrato

    def _realizar_saque(self, saldo, valor, extrato, limite_saques):
        if 0 < valor <= 500 and saldo >= valor and limite_saques < 3:
            saldo -= valor
            extrato.append(f"Saque de R$ {valor:.2f}")
            limite_saques += 1
            self._atualizar_data_saque()
            return saldo, extrato, limite_saques
        elif valor <= 0:
            print("N�o foi poss�vel realizar o saque, o valor deve ser positivo e maior que zero.")
            return saldo, extrato, limite_saques
        elif valor > 500:
            print("O valor m�ximo de saque � de R$ 500.00.")
            return saldo, extrato, limite_saques
        elif limite_saques >= 3:
            print("Limite de saques di�rios excedido. Tente novamente amanh�.")
            return saldo, extrato, limite_saques
        else:
            print("Saldo insuficiente para realizar o saque.")
            return saldo, extrato, limite_saques

    def _atualizar_data_saque(self):
        hoje = datetime.now().date()
        if self.data_ultimo_saque != hoje:
            self.saques_diarios = 0
        self.data_ultimo_saque = hoje

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    numero_conta = 1

    def __init__(self, usuario):
        self.agencia = "0001"
        self.numero = ContaCorrente.numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0
        self.data_ultimo_saque = None
        ContaCorrente.numero_conta += 1

if __name__ == "__main__":
    sistema = GiBank()

    while True:
        print("\nOp��es:")
        print("1 - Criar Usu�rio")
        print("2 - Criar Conta Corrente")
        print("3 - Dep�sito")
        print("4 - Saque")
        print("5 - Extrato")
        print("6 - Sair")

        opcao = int(input("Digite o n�mero da op��o desejada: "))

        if opcao == 1:
            sistema.criar_usuario()
        elif opcao == 2:
            if sistema.usuarios:
                usuario_index = int(input("Digite o n�mero do usu�rio: "))
                if 0 <= usuario_index < len(sistema.usuarios):
                    sistema.criar_conta_corrente(sistema.usuarios[usuario_index])
                else:
                    print("Usu�rio inv�lido.")
            else:
                print("Crie um usu�rio antes de criar uma conta.")
        elif opcao == 3:
            if sistema.contas:
                conta_index = int(input("Digite o n�mero da conta: "))
                if 0 <= conta_index < len(sistema.contas):
                    valor_deposito = float(input("Digite o valor do dep�sito: "))
                    sistema.depositar(sistema.contas[conta_index], valor_deposito)
                else:
                    print("Conta inv�lida.")
            else:
                print("Crie uma conta antes de realizar um dep�sito.")
        elif opcao == 4:
            if sistema.contas:
                conta_index = int(input("Digite o n�mero da conta: "))
                if 0 <= conta_index < len(sistema.contas):
                    valor_saque = float(input("Digite o valor do saque: "))
                    sistema.sacar(sistema.contas[conta_index], valor_saque)
                else:
                    print("Conta inv�lida.")
            else:
                print("Crie uma conta antes de realizar um saque.")
        elif opcao == 5:
            if sistema.contas:
                conta_index = int(input("Digite o n�mero da conta: "))
                if 0 <= conta_index < len(sistema.contas):
                    sistema.extrato(sistema.contas[conta_index])
                else:
                    print("Conta inv�lida.")
            else:
                print("Crie uma conta antes de visualizar o extrato.")
        elif opcao == 6:
            print("Saindo do sistema.")
            break
        else:
            print("Op��o inv�lida. Digite um n�mero v�lido.")