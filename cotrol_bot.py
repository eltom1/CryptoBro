from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apis_secretas import TOKEN
import requests


#============== COMANDOS DEL BOT ============================

# /start -> devuelve msj de bienvenida
# /hola  -> devuele msj de bienvenida
# /cotizacion -> te devuelve la cotizacion en tiempo real del dolar 

#fucnion que responde al comando /start del bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola soy tu Crypto Bro para ayudarte y informarte en las alzas y bajas de criptomonedas,valores de bolsas, etc y poder analizar el mercado con calculos ")

#funcion que responde al comnado /hola
async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hola!! , que activo queres consultar hoy?")

async def cotizacion(update: Update, tcontext: ContextTypes.DEFAULT_TYPE):
    try:
        #busca la api de dolarapi(api gratis que te meustra el valor en tiempo real del dolar)
        valor = requests.get("https://dolarapi.com/v1/dolares")
        datos = valor.json()

        #llamo a los valores de dolar blue y oficial 
        
        blue = next(item["venta"]
                    for item in datos if item["nombre"] == "Dolar Blue")
        
        oficial = next(item["venta"] 
                    for item in datos if item["nombre"] == "Dolar Oficial")

        # tambien se puede agregar el dolar cripto, tarjeta, mayorista, bolsa, etc :)

        mensaje = (
            f"cotizacion del dolar en pesos Arg\n"
            f"Dolar Oficial: ${oficial}\n"
            f"Dolar Blue: ${blue}\n"
            f"Datos obtenidos de https://dolarapi.com/v1/dolares"
        )

        await update.message.reply_text(mensaje, parse_mode= "Markdown")

    except Exception as Nombre_Del_error:
        print(f"error: {Nombre_del_error}")
        await update.message.reply_text("Ocurrio un error reintenta en un par de minutos :(")


if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start)) 
    app.add_handler(CommandHandler("hola", hola))
    app.add_handler(CommandHandler("cotizacion", cotizacion))


    print("Estado del Bot-Encendido")
    app.run_polling()


