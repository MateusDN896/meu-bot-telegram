import os
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

openai.api_key = os.getenv("OPENAI_API_KEY")

def start(update, context):
    update.message.reply_text("Oi! Aqui é a Renata da equipe FDZ. Pode me chamar no que precisar!")

def responder(update, context):
    pergunta = update.message.text
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pergunta}]
    )
    texto = resposta.choices[0].message.content
    update.message.reply_text(texto)

def main():
    updater = Updater(os.getenv("TELEGRAM_TOKEN"))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
