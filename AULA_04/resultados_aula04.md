# ATIVIDADE 1: CHATBOT VERSÃO 1 (KNN)

## Output:
precision    recall  f1-score   support

logistica_entregas       1.00      1.00      1.00         6
       reclamacoes       1.00      1.00      1.00         6
           suporte       1.00      1.00      1.00         6
 trocas_devolucoes       1.00      1.00      1.00         6
            vendas       1.00      1.00      1.00         6

          accuracy                           1.00        30
         macro avg       1.00      1.00      1.00        30
      weighted avg       1.00      1.00      1.00        30

[[6 0 0 0 0]
 [0 6 0 0 0]
 [0 0 6 0 0]
 [0 0 0 6 0]
 [0 0 0 0 6]]

=== INICIANDO BATERIA DE TESTES (10 INPUTS OBRIGATÓRIOS) ===

[Teste 1/10]

[Teste 2/10]

[Teste 3/10]

[Teste 4/10]

[Teste 5/10]

[Teste 6/10]

[Teste 7/10]

[Teste 8/10]

[Teste 9/10]

[Teste 10/10]
Digite a frase do cliente: Quero comprar uma tv
Intenção prevista é:  {'vendas'}
A probabilidade é: 100.00%  
### ou:
Digite a frase do cliente: não sei dirigir
Encaminhando para atendimento humano.

# Atividade 2: Construção do Zero (Versão 2 — Decision Tree e 8 Testes Digitados)

## Output:
                precision    recall  f1-score   support

logistica_entregas       0.80      0.67      0.73         6
       reclamacoes       0.57      0.67      0.62         6
           suporte       0.57      0.67      0.62         6
 trocas_devolucoes       1.00      0.67      0.80         6
            vendas       0.71      0.83      0.77         6

          accuracy                           0.70        30
         macro avg       0.73      0.70      0.71        30
      weighted avg       0.73      0.70      0.71        30

[[4 0 0 0 2]
 [1 4 1 0 0]
 [0 2 4 0 0]
 [0 0 2 4 0]
 [0 1 0 0 5]]
Intenção prevista é:  {'vendas'}
A probabilidade é: 100.00%                precision    recall  f1-score   support

logistica_entregas       0.80      0.67      0.73         6
       reclamacoes       0.57      0.67      0.62         6
           suporte       0.57      0.67      0.62         6
 trocas_devolucoes       1.00      0.67      0.80         6
            vendas       0.71      0.83      0.77         6

          accuracy                           0.70        30
         macro avg       0.73      0.70      0.71        30
      weighted avg       0.73      0.70      0.71        30

[[4 0 0 0 2]
 [1 4 1 0 0]
 [0 2 4 0 0]
 [0 0 2 4 0]
 [0 1 0 0 5]]
Intenção prevista é:  {'vendas'}
A probabilidade é: 100.00%








