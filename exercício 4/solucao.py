def simular_rendimento(capital_inicial, tempo_meses, tipo_investimento ):
    if tipo_investimento == "POUPANCA":
        juros = capital_inicial * 0.005 * tempo_meses
        valor_total = capital_inicial + juros
        return valor_total
    elif tipo_investimento == "CDB":
        juros = capital_inicial * 0.01 * tempo_meses
        juros = juros - (0.15 * juros)
        valor_total = capital_inicial + juros
        return valor_total
    elif tipo_investimento == "TESOURO":
         juros = capital_inicial * 0.008 * tempo_meses
         juros = juros - (0.15 * juros)
         valor_total = capital_inicial + juros
         return valor_total
    
print(simular_rendimento(1000, 12, "POUPANCA"))
print(simular_rendimento(1000, 12, "TESOURO"))
print(simular_rendimento(1000, 12, "CDB"))
