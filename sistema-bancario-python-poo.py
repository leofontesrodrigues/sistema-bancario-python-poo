class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class Conta:
    def __init__(self, agencia, numero_conta, cliente):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")

    def sacar(self, valor, limite_saque_diario):
        if valor > self.saldo:
            print("Saldo insuficiente. Operação de saque não realizada.")
        elif len(self.operacoes) >= limite_saque_diario:
            print("Limite de saques diários excedido.")
        else:
            self.saldo -= valor
            self.operacoes.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso.")

    def mostrar_extrato(self):
        print("Extrato:")
        for operacao in self.operacoes:
            print(operacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")


def obter_conta_por_numero(contas, numero_conta):
    for conta in contas:
        if conta.numero_conta == numero_conta:
            return conta
    return None


def obter_cliente_por_cpf(clientes, cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def main():
    clientes = []
    contas = []
    numero_conta = 1
    limite_saque_diario = 3

    while True:
        print("\nMenu:")
        print("[d] Depositar")
        print("[s] Sacar")
        print("[e] Extrato")
        print("[nc] Nova conta")
        print("[lu] Listar usuários")
        print("[lc] Listar contas")
        print("[nu] Novo usuário")
        print("[q] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "d":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do depósito: "))
            conta = obter_conta_por_numero(contas, numero_conta)
            if conta:
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")
        elif opcao == "s":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do saque: "))
            conta = obter_conta_por_numero(contas, numero_conta)
            if conta:
                conta.sacar(valor, limite_saque_diario)
            else:
                print("Conta não encontrada.")
        elif opcao == "e":
            numero_conta = int(input("Digite o número da conta: "))
            conta = obter_conta_por_numero(contas, numero_conta)
            if conta:
                conta.mostrar_extrato()
            else:
                print("Conta não encontrada.")
        elif opcao == "nc":
            cpf = input("Digite o CPF do cliente: ")
            cliente = obter_cliente_por_cpf(clientes, cpf)
            if cliente:
                contas.append(Conta("0001", numero_conta, cliente))
                print(f"Conta criada com sucesso para o cliente {cliente.nome}.")
                numero_conta += 1
            else:
                print("Cliente não encontrado.")
        elif opcao == "lu":
            print("Lista de usuários:")
            for cliente in clientes:
                print(f"Nome: {cliente.nome} - CPF: {cliente.cpf}")
        elif opcao == "lc":
            print("Lista de contas:")
            for conta in contas:
                print(f"Agência: {conta.agencia} - Número da conta: {conta.numero_conta} - CPF do cliente: {conta.cliente.cpf}")
        elif opcao == "nu":
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            data_nascimento = input("Digite a data de nascimento do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            clientes.append(Cliente(nome, cpf, data_nascimento, endereco))
            print("Cliente cadastrado com sucesso.")
        elif opcao == "q":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
