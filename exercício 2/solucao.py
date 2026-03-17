def analisar_triangulo(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        if a == b == c:
           return "Equilátero"
        elif a!=b and b!=c and a!=c:
            return "Escaleno"
        else:
            return "Isosceles"
    else:
       return "Não é um triângulo"
print(analisar_triangulo(1, 1, 20))