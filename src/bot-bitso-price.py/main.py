from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bitso import Api
from bitso.errors import ApiError
import logging
import os
import random
import sys

ff = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=ff)
logger = logging.getLogger()

mode = os.getenv('MODE')
TOKEN = os.getenv('TOKEN')
PORTT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME')
api = Api()
attrs = ('ask', 'bid', 'last', 'high', 'low', 'vwap', 'volume')
books = '\n'.join(api.available_books().books).replace('_', ' ')

if mode == 'dev':
    def run(updater):
        updater.start_polling()
elif mode == 'prod':
    def run(updater):
        url = f'https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}'
        updater.start_webhook(
            listen='0.0.0.0',
            port=PORTT,
            url_path=TOKEN,
            webhook_url=url
        )
else:
    logger.error('No MODE specified!')
    sys.exit(1)

def price_handler(update: Update, context: CallbackContext):
    try:
        coin0 = context.args[0]
        coin1 = context.args[1]
        ticker = api.ticker(f'{coin0}_{coin1}')
        msg = '\n'.join((f'{atr}: ${getattr(ticker, atr)}' for atr in attrs))
    except IndexError:
        msg = 'creo que se te ha olvidado un parámetro wacho. Ej: /p btc ars'
    except ApiError:
        msg = f'no existe libro de orden de {coin0} a {coin1}, pruebe al revés'
    update.message.reply_text(msg)

def help_handler(update: Update, context: CallbackContext):
    msg = f'los siguientes libros están habilitados:\n{books}\nEj: /p btc ars'
    update.message.reply_text(msg)

if __name__ == '__main__':
    logger.info('Starting bot')
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler('price', price_handler))
    updater.dispatcher.add_handler(CommandHandler('p', price_handler))
    updater.dispatcher.add_handler(CommandHandler('help', help_handler))
    run(updater)

