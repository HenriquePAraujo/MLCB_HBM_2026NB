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


LAB 02 - AULA 02 (MLCB): Naive Bayes e Probabilidades

Output:

Mensagem de Teste: 'Gostaria de devolver o produto que comprei'
Intenção Predita: troca_devolucao

--- Distribuição de Probabilidades por Classe ---
Classe [duvida_frete]: 27.99%
Classe [rastrear_pedido]: 24.54%
Classe [troca_devolucao]: 47.46%


# 1 - Avaliem os resultados e verifiquem se os resultados foram corretos ou incorretos. Coloque a resposta no arquivo do relatório do laboratório
O resultados estão corretos.
# 2 - Detectado algum erro, qual seria a maneira mais correta de melhorar o resultado do algoritmo?
Cadastrando a frase que causou o erro no código junto com sua classe
# 3 - Detalhe a função do Naive Bayes no algorítmo.
Ele calcula a probabilidade de um dado pertencer a uma categoria,a que for maior será o resultado final



LAB 03 - AULA 02 (MLCB): Preencha os blocos TODO

Output:
Acurácia do Modelo: 33.33%

# 1 - Qual foi a acurácia obtida pelo modelo no conjunto de teste e por que, em um dataset tão pequeno (9 exemplos), essa métrica pode ser enganosa?
33.33%. Pode ser enganosa pois a baixa quantidade de dados tanto para teste e para treino não podem ser suficientes para treinar um algoritmo
# 2 - Como o modelo de Árvore de Decisão (DecisionTreeClassifier) toma a decisão de separar as intenções do usuário?
A Árvore de Decisão analisa as características presentes nos dados e cria regras para separar as diferentes classes.Exemplo:
As palavras 'senha','redefinir' e 'acesso' ajudam a identificar o 'reset_senha'.
# 3 - Qual é o risco de utilizar uma Árvore de Decisão sem limite de profundidade (max_depth) em datasets de texto maiores?
Overfitting(sobreajuste),sem limitar a profundidade, a árvore pode ficar muito complexa e aprender detalhes específicos dos dados de treinamento, inclusive padrões que não são realmente importantes

