4 . Comparador de Renda fixa
Crie uma função chamada simular_rendimento que receba o capital_inicial, o tempo_meses e o tipo_investimento (uma string).

As taxas de juros (simples, para facilitar nesta fase) são:

"POUPANCA": 0,5% ao mês.

"CDB": 1,0% ao mês.

"TESOURO": 0,8% ao mês.

A função deve calcular o lucro (Juros = Capital × Taxa × Tempo).

Regra de Imposto de Renda: Se o investimento for "CDB" ou "TESOURO", a função deve descontar 15% de imposto sobre o lucro antes de retornar o valor final. Se for "POUPANCA", é isento.

A função deve retornar o valor total (Capital + Lucro Líquido) que o aluno receberia ao final do período.

Caso	Entrada (Cap, Meses, Tipo)	Saída Esperada	Lógica Testada
01	1000, 12, "POUPANCA"	R$ 1060.00	Isento de IR. Lucro de R$ 60,00.
02	1000, 12, "CDB"	R$ 1102.00	Lucro bruto R$ 120. IR de 15% (R$ 18). Líquido R$ 102.
03	1000, 12, "TESOURO"	R$ 1081.60	Lucro bruto R$ 96. IR de 15% (R$ 14.40). Líquido R$ 81,60.
