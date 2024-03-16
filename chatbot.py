import random
import tensorflow as tf
from transformers import BertTokenizer, TFBertForQuestionAnswering

# Importe a biblioteca de processamento de linguagem natural
import nltk
from nltk.chat.util import Chat, reflections

# Define os padrões de entrada e saída para o chatbot
pares = [
    # Padrões de saudação
    ["meu nome é (.*)", ["Olá %1, como posso ajudá-lo?"]],
    ["(Oi|Olá|E aí)", ["Olá, como posso ajudá-lo?"]],
    ["(tudo bem|como vai você)", ["Estou bem, obrigado por perguntar!"]],
    # Respostas divertidas
    ["(brincar|jogar)", ["Claro! Vamos jogar algum jogo."]],
    ["(comida|pizza|sushi)", ["Eu adoraria uma %2 agora!"]],
    # Informações básicas
    ["(.*) clima (.*)", ["O clima está ótimo!"]],
    ["(idade|anos)", ["Sou apenas um programa, não tenho idade."]],
    # Despedidas
    ["(adeus|tchau)", ["Até logo!"]],
    ["(obrigado|agradecido)", ["Você é bem-vindo!"]],
    # Caso não entenda
    ["(.*)", ["Desculpe, não entendi. Pode reformular a pergunta?"]],
]

# Respostas aleatórias de saudação
respostas_saudacao = [
    "Olá! Sou o Brusabot. Pode falar comigo!",
    "Oi! Estou aqui para ajudar. O que você gostaria de fazer?",
    "E aí! Como posso ser útil hoje?",
]

# Inicialize o chatbot
chatbot = Chat(pares, reflections)

# Inicie o loop de conversação
print(random.choice(respostas_saudacao))
while True:
    mensagem = input("Você: ")
    if mensagem.lower() == "adeus":
        print("Chatbot: Até logo!")
        break
    resposta = chatbot.respond(mensagem)
    print("Chatbot:", resposta)
