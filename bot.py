from telegram.ext import Updater, CommandHandler

import bot_config

def hello_world(bot, update):
    print(update)

def main():
    my_bot = Updater(bot_config.TOKEN)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', hello_world))

    my_bot.start_polling()
    my_bot.idle()

if __name__ == '__main__':
    main()