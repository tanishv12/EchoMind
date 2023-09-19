import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a bot that can answer questions about anything."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": "user_input"})
    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = messages)
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "EchoMind")

demo.launch(share=True)


