def analisar_qualidade_ar(indice):
    if indice <= 25:
        return "A qualidade do ar está boa"
    
    elif 26 <= indice <= 50:
        return "A qualidade do ar está moderada"
    
    elif 51 <= indice <= 100:
        if indice > 80:
            return "A qualidade do ar está ruim, evite atividades ao ar livre | Acionar sistema de aspersão de água"
        return "A qualidade do ar está ruim, evite atividades ao ar livre"
    
    else: 
        return "A qualidade do ar está péssima, alerta de saúde | Acionar sistema de aspersão de água"
print(analisar_qualidade_ar(110))