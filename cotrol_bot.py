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

async def cotizacion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        #busca la api de dolarapi(api gratis que te meustra el valor en tiempo real del dolar)
        valor = requests.get("https://api.bluelytics.com.ar/v2/latest",timeout=10) #el timeout de 10 seg para q no quede esperando 
        datos = valor.json()

        print("DATOS RECIBIDOS DE LA API:", datos)

        #llamo a los valores de dolar blue y oficial 
        
        # precio de venta -> si vos le queres comprar al banco o entidad financiera 
        # precio de compra -> si vos queres vender
        dolar_blue = datos["blue"]["value_sell"]
        dolar_oficial = datos["oficial"]["value_sell"]
        euro_oficial = datos["oficial_euro"]["value_sell"]
        euro_blue = datos["blue_euro"]["value_sell"]

        # tambien se puede agregar el dolar cripto, tarjeta, mayorista, bolsa, etc :)

        mensaje = (
            f"Cotizaciones Dolar y Euro Actualizadas \n"
            f"Dolar Oficial: ${dolar_oficial}\n"
            f"Dolar Blue: ${dolar_blue}\n"
            f"Euro Oficial: {euro_oficial} €\n"
            f"Euro Blue: {euro_blue} €\n"
            f"Datos obtenidos de Bluelytics" 
        )

        await update.message.reply_text(mensaje, parse_mode= "Markdown") #print del msj

    except requests.exceptions.ConnectionError:
        await update.message.reply_text("no tenes internet bro, revisa la conexion del servidor o la tuya crack")
        
    except Exception as Nombre_Del_error:
        print(f"error: {Nombre_Del_error}")
        await update.message.reply_text("Ocurrio un error reintenta en un par de minutos :(")

    

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start)) 
    app.add_handler(CommandHandler("hola", hola))
    app.add_handler(CommandHandler("cotizacion", cotizacion))


    print("Estado del Bot-Encendido")
    app.run_polling()

