import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split


dados_agencia = {
    'mensagem': [
        'Quero comprar uma passagem para São Paulo',
        'Gostaria de reservar uma passagem de avião',
        'Preciso comprar uma passagem para o Rio de Janeiro',
        'Quero viajar para Salvador, como faço para comprar a passagem?',

        'Quero cancelar minha reserva',
        'Como faço para cancelar minha passagem?',
        'Preciso cancelar a viagem que reservei',
        'Quero desistir da minha reserva',

        'Quero falar com um atendente',
        'Preciso conversar com uma pessoa',
        'Gostaria de falar com o suporte',
        'Pode me encaminhar para um atendente?'
    ],
    'intencao': [
        'comprar_passagem','comprar_passagem','comprar_passagem','comprar_passagem',
        'cancelar_reserva','cancelar_reserva','cancelar_reserva','cancelar_reserva',
        'falar_atendente','falar_atendente','falar_atendente','falar_atendente'
    ]
}
df = pd.DataFrame(dados_agencia)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['mensagem'])
y = df['intencao']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = MultinomialNB()
modelo.fit(X_train, y_train)


mensagem_teste = ["Gostaria de cancelar minha reserva","Gostaria de saber sobre viagens internacionais","Como contato o suporte?"]
mensagem_teste_vetorizada = vectorizer.transform(mensagem_teste)
intencao_prevista = modelo.predict(mensagem_teste_vetorizada)
probabilidade = modelo.predict_proba(mensagem_teste_vetorizada)
classes = modelo.classes_

print("----RESULTADOS LAB 04----")
print(f"Mensagem de teste: {mensagem_teste[0]}")
print(f"Intenção predita: {intencao_prevista[0]}")

for classe,prob in zip(classes,probabilidade[0]):
    print(f"Probabilidade de ser {classe}: {prob * 100:.2f}%")
print("-------------------------------------------------")
print(f"Mensagem de teste: {mensagem_teste[1]}")
print(f"Intenção predita: {intencao_prevista[1]}")
print("-------------------------------------------------")
for classe,prob in zip(classes,probabilidade[1]):
    print(f"Probabilidade de ser {classe}: {prob * 100:.2f}%")
print("-------------------------------------------------")
print(f"Mensagem de teste: {mensagem_teste[2]}")
print(f"Intenção predita: {intencao_prevista[2]}")

for classe,prob in zip(classes,probabilidade[2]):
    print(f"Probabilidade de ser {classe}: {prob * 100:.2f}%")




