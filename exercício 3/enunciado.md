3. Sistema de monitoramento de qualidade do ar
Imagine que você está programando o software de um sensor para uma "Cidade Inteligente". Crie uma função chamada analisar_qualidade_ar que recebe o índice de micropartículas (µg/m³) no ar.

A função deve retornar uma string com a classificação:

Até 25: "Boa"
De 26 a 50: "Moderada"
De 51 a 100: "Ruim" (Exibir mensagem: "Evitar atividades ao ar livre")
Acima de 100: "Péssima" (Exibir mensagem: "Alerta de saúde!")

Adicione uma lógica extra: se o índice for maior que 80, a função deve sugerir automaticamente o acionamento de um sistema de aspersão de água.

Caso	Entrada (Índice)	Saída Esperada	Lógica Testada
01	20	"Boa"	Limite inferior.
02	55	"Ruim" + Mensagem de evitar atividades.	Faixa intermediária com alerta.
03	85	"Ruim" + Acionar aspersão.	Verificação do gatilho de auto