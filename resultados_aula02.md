LAB 01 - AULA 02 (MLCB): Classificador de Intenções

Output:
Mensagem: 'Quero consultar quanto dinheiro tenho' ==> Intenção Predita: [fazer_pix]
Mensagem: 'Pode me ajudar a fazer um pix?' ==> Intenção Predita: [fazer_pix]
Mensagem: 'Gostaria de cancelar meu cartão de crédito' ==> Intenção Predita: [cancelar_conta]

# 1 - Avaliem os resultados e verifiquem se os resultados foram corretos ou incorretos. Coloque a resposta no arquivo do relatório do laboratório
Incorreto, devido o primeiro resultado constar da seguinte forma 'Quero consultar quanto dinheiro tenho' ==> Intenção Predita: [fazer_pix]  e o correto seria 'Quero consultar quanto dinheiro tenho' ==> Intenção Predita: [Consultar saldo].

# 2 - Detectado algum erro, qual seria a maneira mais correta de melhorar o resultado do algoritmo?

Colocar a frase 'Quero consultar quanto dinheiro tenho' no dataset  e rotular ela da forma correta, obtendo mais chances de probabilidade de seguir corretamente no próximo resultado.

# 3 - Detalhe a função do LogisticRegression no algorítmo.

Essa função serve para verificar a probabilidade de uma entrada pertencer a uma classe ajustando uma função sigmoide/softmax. Exemplo: 'Gostaria de cancelar meu cartão de crédito', ele calcula as variáveis da frase e classificando o resultado entre 0 e 1 através dessa da função sigmoide

P ( y = 1 ) = 1 /1 + e − z

Se resultado for maior que 0,5, ele tem uma chance maior de ser uma classe X, e se for menor pertencer a uma outra classe.     
