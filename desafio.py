# Desafio DIO - Sistema Bancario
# Autor: João Ciola
# Saque, Depósito, Extrato

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3

menu = """
=================
|     Menu      |
| 1 - Depositar |
| 2 - Sacar     |
| 3 - Extrato   |
| 4 - Sair      |
|               |
=================

=> """

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES_DIARIO:
            valor = float(input("Digite o valor do saque: "))
            if valor <= saldo and valor <= limite_saque:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Saldo insuficiente ou valor acima do limite de saque diário.")
        else:
            print("Limite de saques diário atingido.")

    elif opcao == "3":
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")