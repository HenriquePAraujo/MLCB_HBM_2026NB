# ATIVIDADE 1: CRIAÇÃO DOS DATAFRAMES


## Output:


Ambiente preparado com sucesso.
Frase original:
Gostaria de saber se vocês estão DEVOLVENDO os valores das mesas compradas!!!

Frase processada:
gostar saber devolver valor meso comprada
Texto original:
MEU sofá!!! chegou quebrado e quero DEVOLVER!!!

Texto normalizado:
sofá chegar quebrar querer devolver

Quantidade de caracteres: 47
Quantidade de tokens antes: 13
Quantidade de tokens depois: 5
Tokens removidos: ['meu', 'chegou', 'quebrado', 'e', 'quero']
Tokens finais: ['sofá', 'chegar', 'quebrar', 'querer', 'devolver']

# ATIVIDADE 2: Finalized Mean Pooling


## Output:

X_vetores: (80, 50)
y: (80,)

Tudo certo!
Treinamento: (64, 50)
Teste: (16, 50)
Dimensão dos vetores: 50

# ATIVIDADE 3: Regressão Logistica + FallBack 


## Output: 


Carregando modelo de Embeddings...
Modelo carregado com sucesso!

Colunas do dataset:

- mensagem
- intencao

Coluna utilizada como target: intencao

Distribuição das intenções:
intencao
logistica_entregas 20
trocas_devolucoes 20
vendas_orcamento 20
suporte_tecnico 20
Name: count, dtype: int64

Formato da matriz X:
(80, 50)

Modelo de Regressão Logística treinado com sucesso!

Classes identificadas:
['logistica_entregas' 'suporte_tecnico' 'trocas_devolucoes'
'vendas_orcamento']

Frase: Quero saber o valor do frete do sofá
Resultado: FALLBACK_HUMANO
Confiança: 42.56%

Frase: Gostaria de ver receitas de bolo de cenoura
Resultado: vendas_orcamento
Confiança: 71.59%

# ATIVIDADE 4: Regressão Logistica + KNN


## Output: 

         Modelo Accuracy Precision Recall     F1
Regressão Logística   75.00%    79.17% 75.00% 75.36%
                KNN   56.25%    52.50% 56.25% 52.14

#Perguntas 

Questão 1 - Qual modelo apresentou melhor desempenho?
A Regressão Logística apresentou o melhor desempenho.

Questão 2 - Por que os resultados podem ser diferentes mesmo utilizando os mesmos embeddings?
Porque embedding é apenas a representação dos textos. Cada algoritmo utiliza essa representação de uma maneira diferente.

Questão 3 - O KNN utiliza distância. Por que a qualidade dos embeddings é particularmente importante para esse algoritmo?
Porque o KNN depende diretamente da distância entre os pontos.

Questão 4 - Se o sistema tivesse 100 mil mensagens e centenas de intenções, você escolheria KNN? Justifique.
Não. No KNN, para classificar uma nova mensagem, precisamos procurar mensagens próximas dentro do conjunto de dados.

Questão 5 - Qual modelo você escolheria para colocar em produção neste cenário?
Regressão Logística.



                
