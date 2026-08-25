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
