2. Validador de Triângulos Moderno
Escreva uma função analisar_triangulo(a, b, c) que receba três lados.

Primeiro, a função deve verificar se os lados formam um triângulo (a soma de dois lados deve ser sempre maior que o terceiro).
Se for válido, retorne uma string com o tipo: "Equilátero", "Isósceles" ou "Escaleno".
Se for inválido, retorne "Não é um triângulo".

Caso	Entrada (Lados)	Saída Esperada	Lógica Testada
01	3, 4, 5	"Escaleno"	Triângulo válido com todos lados diferentes.
02	5, 5, 5	"Equilátero"	Todos os lados iguais.
03	10, 10, 15	"Isósceles"	Dois lados iguais.
04	1, 1, 20	"Não é um triângulo"	Condição de existência (1+1 não é > 20).
