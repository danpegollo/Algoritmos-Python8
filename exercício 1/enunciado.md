1. Simulador de Consumo de Energia
Crie uma função chamada calcular_conta_luz que recebe a leitura atual e a leitura anterior do medidor (em kWh), além da bandeira tarifária atual ("VERDE", "AMARELA" ou "VERMELHA"). A função deve retornar o valor a ser pago

O consumo é a diferença entre as leituras.
Valor do kWh base: R$ 0,50.
Acréscimos da bandeira: Amarela (+ R$ 0,02 por kWh), Vermelha (+ R$ 0,05 por kWh).
Se o consumo for superior a 300 kWh, aplica-se uma taxa extra de 10% sobre o valor total por "alto consumo".

Caso	Entrada (Leituras e Bandeira)	Saída Esperada (Valor Total)	Lógica Testada
01	1100, 1000, "VERDE"	R$ 50.00	Consumo base (100 kWh) sem adicionais.
02	1100, 1000, "AMARELA"	R$ 52.00	Adicional de R$ 0,02/kWh.
03	1500, 1000, "VERMELHA"	R$ 302.50	Alto consumo (>300) + Bandeira Vermelha + 10% taxa.
