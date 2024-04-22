
# Código para simular o processamento de pagamento conforme o diagrama UML fornecido.
# As variáveis e funções estão em português conforme solicitado.

# Dicionário simulando as informações da conta
dic = lambda : {
    '1': {'saldo': 1000, 'limite': 500},
    '2': {'saldo': 2000, 'limite': 1000}
}

informacoes_conta = dic()

# funcoes validadoras
monadContaExiste = lambda conta: conta if conta in informacoes_conta else (print("transacao encerrada"),exit()) if conta == '0' else (print("Conta não existe"), request_account_details())[1]
monadVerificarLimite = lambda conta, valor: False if informacoes_conta[conta]['limite'] < valor else True
monadVerificarSaldo = lambda conta, valor: False if informacoes_conta[conta]['saldo'] < valor else True

#funcoes de requisicoes do usuario
#Digite 0 para sair do loop de escolher a conta.
request_account_details = lambda: monadContaExiste(input("Digite o nome da conta: "))
request_account_details_To = lambda: monadContaExiste(input("Digite o nome da conta de deposito: "))
request_amount_details = lambda: input("Digite o valor da transacao: ")

#fluxo de pagamento de credito
create_transaction_credit = lambda : request_credit_payment_from_bank(request_account_details(), int(request_amount_details()))
request_credit_payment_from_bank = lambda conta, valor: atualizar_limite(conta, valor)
atualizar_limite = lambda conta, valor: (informacoes_conta[conta].update({'limite': informacoes_conta[conta]['limite'] - valor}),complete_transaction(f"transacao de credito no valor {valor} na conta {conta}")
) if monadVerificarLimite(conta, valor) else print("Limite insuficiente - transacao cancelada")

#fluxo de pagamento de debito
create_transaction_debit = lambda : request_transfer_payment_from_bank(request_account_details(), request_account_details_To(), int(request_amount_details()))
request_transfer_payment_from_bank = lambda contaOrigem, contaDestino,valor: atualizar_saldo(contaOrigem,contaDestino, valor)
atualizar_saldo = lambda contaOrigem, contaDestino, valor: ((informacoes_conta[contaOrigem].update({'saldo': informacoes_conta[contaOrigem]['saldo'] - valor})),((informacoes_conta[contaDestino].update({'saldo': informacoes_conta[contaDestino]['saldo'] + valor})),complete_transaction(f"transacao de debito no valor {valor} da conta {contaOrigem} para a {contaDestino}")) if monadVerificarSaldo(contaOrigem, valor) else print("Saldo insuficiente - transacao cancelada"))

#fluxo de pagamento em dinheiro
create_cash_payment = lambda : request_cash_payment(request_amount_details())
request_cash_payment = lambda valor: print_payment_receipt(valor)
print_payment_receipt = lambda valor: (print(f"Recibo do pagamento no valor de: R${valor}"),complete_transaction(f"transacao em dinheiro no valor de R${valor}"))


complete_transaction = lambda transacao: print(f"Complete Transaction - {transacao}")


#fluxo main
processar_pagamento = lambda tipo_pagamento: create_transaction_credit() if tipo_pagamento == 1 else create_transaction_debit() if tipo_pagamento == 2 else create_cash_payment() if tipo_pagamento == 3 else print("Tipo de pagamento inválido - transacao cancelada")
tipo = lambda : input("entre com o tipo do pagamento: 1 - credito, 2 - transferencia, 3 - dinheiro:")

def main():
    processar_pagamento(int(tipo()))

if __name__ == "__main__":
    main()