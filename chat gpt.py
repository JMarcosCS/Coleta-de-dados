import openai

openai.api_key = "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"

messages = [
    {"role": "system", "content": "você é um assistente prestativo."}
]

input_message = input("digite sua mensagem: ")
messages.append({"role": "user", "content": input_message})

while input_message != "fim":
    response = openai.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=200
    )

    awnser = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": awnser})

    print("resposta", awnser)
    input_message = input("digite sua mensagem: ")
    messages.append({"role": "user", "content": input_message})

'''
def enviar_mensagem(mensagem):
    resp = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": mensagem},
            {"role": "assistant", "content": mensagem},
            {"role": "user", "content": mensagem},
            {"role": "system", "content": mensagem},
            {"role": "user", "content": mensagem},
        ]
    )

    return resp["choices"][0]["message"]



while True:
    texto = input("Digite sua dúvida: ")

    if texto == "sair":
        break
    else:
        resp = enviar_mensagem(texto)
        print("Chatbot:", resp["content"])'''
