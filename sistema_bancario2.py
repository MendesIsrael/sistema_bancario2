import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [0] Sair
    Digite a opção desejada => """
    return input(textwrap.dedent(menu))

def depositar(saldo, deposito, extrato, numero_deposito, confirmacao_deposito, /):
  if confirmacao_deposito == "s" or "n":
    if deposito > 0:
      if confirmacao_deposito == "s":
        confirmacao_deposito = confirmacao_deposito
        numero_deposito += 1
        saldo += deposito
        extrato += f"Depósito:\tR$ {deposito:.2f}\n"
        print("\nDinheiro depositado!")
      elif confirmacao_deposito == "n":
        print("Dinheiro não depositado - Operação cancelada")
    else:
      print("\n# Operação falhou! O valor informado é inválido. #")
  else:
    print("Opção inválida, por favor selecione novamente a opção desejada")
  return saldo, extrato, numero_deposito

def sacar(*, saldo, saque, extrato, numero_saques, limite, confirmacao_saque, limite_saques):
    if confirmacao_saque == ("s" or "n") and (saque > 0):
        if (limite != 0 and saque < 501) and (limite_saques != 0 ):
            if saldo > saque:
                if confirmacao_saque == "s":
                    saldo -= saque
                    limite -= saque
                    numero_saques += 1
                    limite_saques -= 1
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    print("Dinheiro sacado")
                    print(f"Seu limite de saque diário é de: R$ {limite} e {limite_saques} saques.")
                elif confirmacao_saque == "n":
                    print("Dinheiro não sacado - Operação cancelada")
            else:
                print("Saldo insuficiente!")
        else:
            print(f"Limite de saque diário excedido! - limite de saque é de: R$ {limite} e/ou {limite_saques} saques.")
    else:    
        print("Opção inválida, por favor selecione novamente a opção desejada")

    return saldo, extrato, limite, numero_saques, limite_saques

def exibir_extrato(saldo, numero_deposito, numero_saques, /, *, extrato):
    print(f"""\n############# EXTRATO BANCÁRIO #############
              
    -Seu dinheiro total é de {saldo:.2f} reais na conta.

    -Você Realizou {numero_deposito} depósitos nesse período.
    -Você Realizou {numero_saques} saques nesse período\n""")
            
    print("-Não foram realizadas movimentações." if not extrato else extrato)

    print("############################################")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n# Já existe usuário com esse CPF! #")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n# Usuário não encontrado, fluxo de criação de conta encerrado! #")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_deposito = 0
    deposito = 0
    saque = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            deposito = float(input("Informe o valor do depósito: "))
            confirmacao_deposito = str(input(f"Confirma o valor de {deposito:.2f} R$ para depositar em sua conta? S ou N: "))

            saldo, extrato, numero_deposito = depositar(saldo, deposito, extrato, numero_deposito, confirmacao_deposito)

        elif opcao == "2":
            saque = float(input("Informe o valor do saque: "))
            confirmacao_saque = str(input(f"Confirma o valor de R$ {saque:.2f} para sacar em sua conta? S ou N: "))

            saldo, extrato, limite, numero_saques, LIMITE_SAQUE  = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE,
                confirmacao_saque=confirmacao_saque,
                1
            )

        elif opcao == "3":
            exibir_extrato(saldo, numero_deposito, numero_saques, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("# Operação inválida, por favor selecione novamente a operação desejada. #")

main()