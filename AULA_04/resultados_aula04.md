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
Intenção prevista é: vendas
A probabilidade é: 66.67%

[Teste 2/10]
Intenção prevista é: vendas
A probabilidade é: 100.00%

[Teste 3/10]
Intenção prevista é: suporte
A probabilidade é: 100.00%

[Teste 4/10]
Intenção prevista é: suporte
A probabilidade é: 100.00%

[Teste 5/10]
Intenção prevista é: trocas_devolucoes
A probabilidade é: 66.67%

[Teste 6/10]
Intenção prevista é: trocas_devolucoes
A probabilidade é: 100.00%

[Teste 7/10]
Intenção prevista é: reclamacoes
A probabilidade é: 100.00%

[Teste 8/10]
Intenção prevista é: reclamacoes
A probabilidade é: 100.00%

[Teste 9/10]
Intenção prevista é: logistica_entregas
A probabilidade é: 100.00%

[Teste 10/10]
Intenção prevista é: logistica_entregas
A probabilidade é: 100.00%

Acurácia (no conjunto de teste inicial): 1.0
F1-Score Weighted (no conjunto de teste inicial): 1.0
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

# Atividade 3: Relatório Comparativo de Modelos


## 1.Tabela Comparativa de Métricas (Dados de Teste)

| Modelo | Acurácia Geral | F1-Score (Weighted) | Principais Erros na Matriz |
| :--- | :--- | :--- | :--- |
| KNN (K=3) | 100% | 100% | Nenhuma classe se confundiu |
| Decision Tree | 77% | 75% | Reclamações foi a que mais se confundiu,2 acertos e 3 erros,1 em logistica e 3 em trocas e devoluções |


## 2. Análise dos Testes de Entrada (`input()`)
- Comportamento do KNN (10 testes): Um comportamento e precisão quase perfeitos e sem erros
- Comportamento da Decision Tree (8 testes): Confusa e insegura


## 3. Veredito Final
- Melhor modelo para este projeto: KNN
- Justificativa técnica: O KNN foi escolhido como o melhor modelo para este projeto porque apresentou 100% de acurácia e 100% de F1-Score Weighted nos
dados de teste. Além disso, não apresentou erros na matriz de confusão, demonstrando que todas as classes foram classificadas corretamente durante a
avaliação. Nos testes realizados, o modelo também apresentou um bom comportamento na identificação das intenções dos clientes.









