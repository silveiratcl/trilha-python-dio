menu = """

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

==> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        deposito = float(input("Informe o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Deposito realizado com sucesso!")

        else:
            print("Valor informado é inválido.")

    elif opcao == "s":

        saque = float(input("Informe o valor do saque: "))

        if saque < 0:
            print("Opção inválida")

        elif saque > 500:
                    print("Seu limite e de R$ 500.00 por saque")

        elif numero_saque > 3:
            print("Excedido número máximo diário (3) de saques")

        elif saque > saldo:
            print("Saldo insuficiente")

        else:
            saldo -= saque
            numero_saque += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
            print("\n Saque realizado com sucesso!\n Aguarde e retire seu dinheiro")

    elif opcao == "e":

        print(f"##### Extrato Bancário #####\n\n{extrato}\n\nR$ {saldo:.2f}")

    elif opcao == "q":
        break

else:
        print("Operação inválida, favor selecionar opção válida")