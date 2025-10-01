from datetime import datetime as dt

class ClienteBancario:

    def __init__ (self):

        self.conta = 0
        self.limite = 500.0
        self.historico = []
        
        self.taxa = 0.01
        self.contrato = 25.00
        self.seguro = 100.00
        self.custoEfetivoTotal = 0.00
        self.financiamento = []

    def depositar(self, valor):

        self.conta += valor
        cliente.extrato(cliente.datas(), "Depósito", valor)

    def sacar(self, valor):

        if self.conta == 0 and valor <= self.limite:

            self.limite -= valor
            cliente.extrato(cliente.datas(), "Saque", valor)

        elif self.conta < valor:
            print("Erro! Saldo insuficiente.")

        else:
            self.conta -= valor
            cliente.extrato(cliente.datas(), "Saque", valor)

    def check(self, valor):

        if valor <= 0:
            raise ValueError()
        
    def extrato(self, data, descricao, valor):

        dicionario = {
            "Data" : data,
            "Desc." : descricao,
            "Valor" : valor,
            "Saldo" : self.conta,
            "ChequeEspecial": self.limite
            }
        
        self.historico.append(dicionario)

    def mostrar_extrato(self, maxDataInicial, maxDataFinal, dataInicial, dataFinal):

        if not self.historico:
            print("Erro! Não foram realizadas movimentações.")

        if dataInicial > dataFinal:
            print("Erro! Data inicial não pode ser maior que data final.")

        else:
            if all(maxDataInicial <= d <= maxDataFinal for d in (dataInicial, dataFinal)):

                for i in range(0, len(self.historico)):

                    print(self.historico[i])
            else:
                print("Erro! Datas fora de período.")
    
    def datas(self):
        
        now = dt.now()
        data_hoje = now.strftime("%d/%m/%Y")
        return data_hoje
    
    def simularFinanciamento(self, valor, nParcelas):

        dicionario = {
            "Nº" : 0,
            "Prestacao." : 0,
            "Juros" : 0.00,
            "Amortizacao" : 0.00,
            "SaldoDevedor" : valor
            }
        
        self.financiamento.append(dicionario)
        print(self.financiamento[0])
        
        taxa = self.taxa
        seguro = self.seguro

        prestacao = valor * (((1 + taxa) ** nParcelas) * taxa) / (((1 + taxa) ** nParcelas) - 1)

        for i in range(1, nParcelas + 1):

            juros = valor * taxa
            amortizacao = prestacao - juros
            valor -= amortizacao

            self.custoEfetivoTotal += prestacao + seguro

            dicionario.update({
            "Nº" : i,
            "Prestacao." : f"{prestacao:.2f}",
            "Juros" : f"{juros:.2f}",
            "Amortizacao" : f"{amortizacao:.2f}",
            "SaldoDevedor" : f"{valor:.2f}"
            })

            self.financiamento.append(dicionario)
            print(self.financiamento[i])

cliente = ClienteBancario()
maxDataInicial = cliente.datas()