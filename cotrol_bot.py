from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apis_secretas import TOKEN


#fucnion que responde al comando /start del bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola soy tu Crypto Bro para ayudarte y informarte en las alzas y bajas de criptomonedas,valores de bolsas, etc y poder analizar el mercado con calculos ")

#funcion que responde al comnado /hola
async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hola!! , que activo queres consultar hoy?")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start)) 
    app.add_handler(CommandHandler("hola", hola))

    print("Estado del Bot-Encendido")
    app.run_polling()


