print(""" 
    Menu Bancário
    [d] - "Depositar"
    [s] - "Sacar"
    [e] - "Extrato"
    [q] - "Sair"
""")

saldo = 0
limite = 500
saque = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input("Escolha uma das Opções Abaixo: ")
    if opcao == "d":
        valor_deposito = float(input("Qual o valor do Depósito?: "))
        saldo += valor_deposito
        print(f"Depósito de R${valor_deposito:.2f} Realizado! Saldo atual:R${saldo:.2f}")
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Você já atingiu o limite de saques.")
            continue
        if saldo <= 0:
            print("Saldo insuficiente para saque.")
            continue
        valor_saque = float(input("Informe o valor do Saque: "))
        if valor_saque > limite:
            print(f"Limite de saque por transação é de R${limite:.2f}.")
            continue
        if (saldo - valor_saque) < 0:
            print("Saldo insuficiente para saque.")
            continue
        if (sum(saque) + valor_saque) > 1500:
            print("Limite de saque diário atingido.")
            continue
        saldo -= valor_saque
        saque.append(valor_saque)
        numero_saques += 1
        print(f"Saque de R${valor_saque:.2f} Realizado com Sucesso! Saldo atual: R${saldo:.2f}")
    elif opcao == "e":
        extrato = saldo
        print(f"O seu saldo atual é de: R${extrato:.2f}")
    elif opcao == "q":
        print("Sair")
        break
    else:
        print("Opção inválida.")
