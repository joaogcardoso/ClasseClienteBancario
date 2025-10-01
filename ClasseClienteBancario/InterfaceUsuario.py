from ClasseClienteBancario import cliente, maxDataInicial
import ClasseClienteBancario

nome = str(input("Digite seu nome completo: "))
cpf = str(input("Digite seu CPF(000.000.000-00): "))
endereco = str(input("Digite seu endereço (Rua, número, bairro, CEP(00000-000), cidade-UF): "))

while True:
    try:
        print("Escolha uma opção:")
        print("Opção 1: Depositar")
        print("Opção 2: Sacar")
        print("Opção 3: Extrato")
        print("Opção 4: Financiamento")
        print("Opcão 5: Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:

            valor = float(input("Qual valor deseja depositar? "))
            cliente.check(valor)
            cliente.depositar(valor)

        if opcao == 2:

            valor = float(input("Qual valor deseja sacar? "))
            cliente.check(valor)
            cliente.sacar(valor)

        if opcao == 3:

            maxDataFinal = cliente.datas()
            dataInicial = str(input("Digite a data inicial do período(DD/MM/AAAA): "))
            dataFinal = str(input("Digite a data final do período(DD/MM/AAAA): "))

            if not dataInicial:
                dataInicial = cliente.datas()

            if not dataFinal:
                dataFinal = cliente.datas()

            print("========== Extrato Bancário ==========")
            print(f"Período: {dataInicial} - {dataFinal}")
            print(f"Nome: {nome}")
            print(f"CPF: {cpf}")
            print(f"Endereço: {endereco}")

            cliente.mostrar_extrato(maxDataInicial, maxDataFinal, dataInicial, dataFinal)

        if opcao == 4:

            valor = float(input("Qual valor deseja financiar? "))
            nParcelas = int(input("Quantas parcelas deseja financiar? "))
            cliente.check(valor)
            cliente.check(nParcelas)

            print("========== Simulação de Financiamento ==========")
            
            cliente.simularFinanciamento(valor, nParcelas)

            contrato = ClasseClienteBancario.cliente.contrato
            seguro = ClasseClienteBancario.cliente.seguro
            custoEfetivoTotal = ClasseClienteBancario.cliente.custoEfetivoTotal

            print(f"Taxa de confecção de contrato: R${contrato}")
            print(f"Taxa de seguro: R${seguro}")
            print(f"Custo efetivo total: R${(custoEfetivoTotal + contrato):.2f}")
            break

        if opcao == 5:
            print("Fim da sessão.")
            break

    except ValueError:
        print("Erro! Entrada inválida.")
        break