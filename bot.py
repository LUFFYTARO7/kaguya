from abc import update_abstractmethods
from asyncio.log import logger
from turtle import update
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

def start(update, context):
    update.message.reply_text('Hi! i am Kaguya-sama bot')

def help(update, context):
    update.message.reply_text('Help!')

def echo(update, context):
    update.message.reply_text()

def afk(update, context):
    first_name = update.message.from_user.first_name
    update.message.reply_text(f'you are gone now, {first_name}!')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)





bot = telegram.Bot("5751139494:AAHPpkQoF6noI9F90Wy7DHEv5lfjKQSx7ms")

def ban(update, context):
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    bot.kick_chat_member(chat_id=chat_id, user_id=user_id)







# Create the Updater and pass it your bot's token.
# Make sure to set use_context=True to use the new context based callbacks
# Post version 12 this will no longer be necessary
updater = Updater("5751139494:AAHPpkQoF6noI9F90Wy7DHEv5lfjKQSx7ms", use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('afk', afk))
updater.dispatcher.add_handler(CommandHandler('ban', ban))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()

