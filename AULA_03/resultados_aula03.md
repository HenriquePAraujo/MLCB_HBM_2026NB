# LAB 01 - AULA 03 (MLCB): Pré-processamento e Stopwords

# Output:

--- RESULTADOS DO LAB 01 (AULA 03) ---
Mensagem: 'Preciso urgente da segunda via da fatura'
Intenção Predita: [segunda_via]
Vocabulário Filtrado (sem stopwords): ['2a', '2a via', 'aberto', 'acordo', 'acordo pagar', 'alterar', 'alterar endereço', 'app', 'atrasada', 'atualizo', 'atualizo dados', 'boleto', 'cadastramento', 'dados', 'dados residenciais', 'débito', 'débito aberto', 'dívida', 'emitir', 'emitir segunda', 'endereço', 'endereço cadastramento', 'fatura', 'fatura atrasada', 'fazer', 'fazer um', 'gostaria', 'gostaria alterar', 'negociar', 'negociar pagamento', 'no', 'no app', 'onde', 'onde atualizo', 'pagamento', 'pagamento dívida', 'pagar', 'pagar débito', 'posso', 'posso emitir', 'residenciais', 'residenciais no', 'segunda', 'segunda via', 'um', 'um acordo', 'via', 'via boleto', 'via fatura']

# 1 - Qual o impacto da remoção de stopwords no tamanho do vocabulário do modelo?
O impacto é positivo, pois deixa o algoritmo mais otimizado. 
# 2 - O que significa a configuração ngram_range=(1, 2) no TfidfVectorizer?
Dar contesto nas palavras, para ter o melhor resultado 
Ex: "Segunda", "Via" com o TfidfVectorizer ficaria da seguinte forma: Segunda via 
# 3 - Como a remoção de palavras genéricas ajuda a evitar classificações incorretas?
Por que tem menos palavras para o algoritmo avaliar, deixando as palavras mais diretas para classificação.


# LAB 02 - AULA 03 (MLCB): Matriz de Confusão e Métricas

# Output:
--- Relatório de Classificação ---
                     precision    recall  f1-score   support

horario_atendimento       0.50      1.00      0.67         1
        localizacao       0.00      0.00      0.00         1
    troca_devolucao       0.00      0.00      0.00         1

           accuracy                           0.33         3
          macro avg       0.17      0.33      0.22         3
       weighted avg       0.17      0.33      0.22         3

--- Matriz de Confusão ---
[[1 0 0]
 [1 0 0]
 [0 1 0]]

# 1 - O que representam as métricas Precision, Recall e F1-Score no relatório?
#### Precision 
Entre as mensagens que o modelo classificou em uma determinada classe,mostrara quantas estarão corretas. Ex:
O modelo classificou 5 mensagens como localizacao, mas apenas 4 realmente eram de localização,logo Precision = 4 / 5 = 0,80 = 80%
#### Recall
Entre todas as mensagens que realmente pertencem a uma determinada classe, quantas o modelo conseguiu identificar? Ex:
Há 6 mensagens realmente relacionadas a localizacao, mas o modelo conseguiu identificar corretamente apenas 4,logo Recall = 4 / 6 = 0,67 = 67%
#### F1-Score
O F1-Score combina Precision e Recall em uma única métrica,a sua fórmula é:
F1 = 2 × (Precision × Recall) / (Precision + Recall)
# 2 - Como interpretar a diagonal principal da Matriz de Confusão?
A diagonal principal da Matriz de Confusão representa os acertos do modelo,cada posição da diagonal representa a quantidade de mensagens que foram classificadas 
corretamente em cada uma dessas classes,já os valores que aparecem fora da diagonal representam erros, pois indicam que o modelo confundiu uma classe com outra.
# 3 - Por que a acurácia isolada pode ser enganosa quando temos classes desbalanceadas?
Porque ela acaba ignorando outras classes. Ex:
100 mensagens:
90 são localizacao
5 são horario_atendimento
5 são troca_devolucao
Agora imagine que um modelo simplesmente classifique todas as mensagens como localizacao.
Ele acertaria as 90 mensagens de localização,logo Acurácia = 90 / 100 = 90%
Por isso, uma acurácia de 90% pode dar a impressão de que o modelo é muito bom, quando na verdade ele está ignorando algumas classes.


# LAB 03 - AULA 03 (MLCB): Scikit-Learn Pipeline (Modo TODO)

# Output:
Acuracia via Pipeline: 0.00%

# 1 - Cole o código corrigido e a acurácia obtida.
Só foi aumentado o número de mensagens para treino e teste do modelo para ele conseguir ter conteúdo suficiente para trabalhar.
Acuracia via Pipeline: 100.00%
# 2 - Qual é a grande vantagem de utilizar o objeto Pipeline no Scikit-Learn?
O Pipeline permite colocar várias etapas do Machine Learning em sequência
# 3 - Por que o Pipeline evita que erros de pré-processamento ocorram entre treino e teste?
O Pipeline evita erros de pré-processamento porque encapsula as etapas de transformação e classificação, garantindo que o mesmo 
processo de pré-processamento usado no treinamento seja aplicado aos dados de teste. Ex:
#### Com Pipeline
pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])
#### Sem Pipeline
vectorizer.fit_transform(X_train)
vectorizer.transform(X_test)

modelo.fit(X_train_vec, y_train)
modelo.predict(X_test_vec)






