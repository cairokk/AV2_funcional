# Definição das funções lambda
receber_pagamento = lambda valor: f"pagamento no valor de R${valor}"
imprimir_recibo = lambda recibo: f"Recibo: {recibo}"
encerrar_transacao = lambda recibo: f"Transacao encerrada.\n {recibo}"

# Definição da função fluxo_pagamento utilizando lambdas
fluxo_pagamento = lambda valor: encerrar_transacao(imprimir_recibo(receber_pagamento(valor)))

# Exemplo de uso do fluxo
valor = 100
resultado = fluxo_pagamento(valor)
print(resultado)
