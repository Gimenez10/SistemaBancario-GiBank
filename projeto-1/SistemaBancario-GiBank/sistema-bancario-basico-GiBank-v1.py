from datetime import datetime

class GiBank:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0
        self.data_ultimo_saque = None

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            print(f"Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Não foi possível realizar o depósito, o valor deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= 500 and self.saldo >= valor and self.saques_diarios < 3:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            self.atualizar_data_saque()
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            print(f"Saldo atual: R$ {self.saldo:.2f}")
        elif valor <= 0:
            print("Não foi possível realizar o saque, o valor deve ser positivo e maior que zero.")
        elif valor > 500:
            print("O valor máximo de saque é de R$ 500.00.")
        elif self.saques_diarios >= 3:
            print("Limite de saques diários excedido. Tente novamente amanhã.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def extrato(self):
        print("\nExtrato:")
        for deposito in self.depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in self.saques:
            print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def atualizar_data_saque(self):
        hoje = datetime.now().date()
        if self.data_ultimo_saque != hoje:
            self.saques_diarios = 0
        self.data_ultimo_saque = hoje


if __name__ == "__main__":
    sistema = GiBank()

    while True:
        print("\nOpções:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            valor_deposito = float(input("Digite o valor do depósito: "))
            sistema.depositar(valor_deposito)
        elif opcao == 2:
            valor_saque = float(input("Digite o valor do saque: "))
            sistema.sacar(valor_saque)
        elif opcao == 3:
            sistema.extrato()
        elif opcao == 4:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Digite um número válido.")
