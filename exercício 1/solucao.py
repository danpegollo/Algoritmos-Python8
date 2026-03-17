leitura_atual = int(input("Qual foi a leitura atual do medidor em kWh: "))
leitura_anterior = int(input("Qual foi a leitura anterior do medidor em kWh: "))
bandeira = str(input("Coloque a cor da bandeira da tarifa em minúsculo, deve ser: verde, amarelo ou vermelho: "))

def calcularContaLuz(leitura_anterior, leitura_atual, bandeira):
    consumo = leitura_atual - leitura_anterior

    if bandeira == "amarelo":
        preco_kwh = 0.52
        valor_Conta = consumo * preco_kwh
    elif bandeira == "vermelho":
        preco_kwh = 0.55
        valor_Conta = consumo * preco_kwh
    else:
        preco_kwh = 0.50
        valor_Conta = consumo * preco_kwh

    if consumo > preco_kwh == 300:
        valor_Conta*= 1.1
    return valor_Conta

print(f"{calcularContaLuz(leitura_anterior, leitura_atual, bandeira):.2f}")
