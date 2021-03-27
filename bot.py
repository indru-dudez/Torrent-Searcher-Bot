#Licenced under MIT License
#charset = "utf-8"
#Language = "Python3"
#Bot Framework = "python-telegram-bot"
#The Code is without Proxy, Actual code contains Proxy
#Proxy should be used is of the type SOCKS5
#Special thanks to cyberboySumanjay
#The bot will work till you press ctrl+c in the terminal or command line.,

#import the required files
import requests
import logging
import config
from telegram import *
from telegram.ext import *

#enable logger (optional)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = "1630656372:AAHQvQzF_08wXXxCFYS_lDdI56QiS3ogva8"

#CommandHandler for message "Start"
def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat.id
    keyboard = [[
        InlineKeyboardButton('Support Chat',
                             url=config.supportChatUrl)
    ],
        [
            InlineKeyboardButton('🕵️MASTER🤖',
                                 url=config.appUrl)
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("<b>Hi, I Can Search Torrent Database For Your Query.</b>\n\n"
                             "Supports Inline Mode \n-/help For More Info\n",
                    parse_mode='HTML',
                    reply_markup=reply_markup)


#CommandHandler to get torrents for the query
def torr_serch(update: Update, context: CallbackContext) -> None:
    torr_serch = ' '.join(context.args) 
    try:
        update.message.reply_text("Searching results for {}".format(update.message.text.split(' ',1)[1]))
        url = "https://api.sumanjay.cf/torrent/?query={}".format(update.message.text.split(' ',1)[1])
        results = requests.get(url).json()
        print(results)
        for item in results:
            age = item.get('age')
            leech = item.get('leecher')
            mag = item.get('magnet')
            name = item.get('name')
            seed = item.get('seeder')
            size = item.get('size')
            typ= item.get('type')
            update.message.reply_text(f"""*Name:* {name}
_Uploaded {age} ago_
*Seeders:* `{seed}`
*Leechers:* `{leech}`
*Size:* `{size}`
*Type:* {typ}
*Magnet Link:* `{mag}`""", parse_mode=ParseMode.MARKDOWN)
        update.message.reply_text("End of the search results...")
    except:
        update.message.reply_text("""Search results completed...
If you've not seen any results, try researching...!""")

#CommandHnadler for message "info"
def info(update: Update, context: CallbackContext) -> None:
    #Never Mind :-)
    update.message.reply_text("""*Made with 🍄.*

*Language:* [Python3](https://www.python.org/)

*Bot Framework:* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)

*Server:* [Heroku](www.heroku.com)

*Source Code:* `MAY BE NEXT TIME`

If you 👍 this bot, Support the developer by just sharing the bot to Your friends...""", parse_mode=ParseMode.MARKDOWN)

#CommandHandler for message "Help"
def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""Hey, this is not most complicated bot. Just use /search command and enter the query you want to search and i will do the rest!

This bot is in the *BETA* stage. So, if any error occurs, feel free to pm my master""", parse_mode=ParseMode.MARKDOWN)

#Add all handlers to the main function.
def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("search", torr_serch, pass_args=True))
    updater.start_polling() #set bot to polling, if you use webhooks, replace this statement with the url of webhook.,
    updater.idle()

#Call the main function
if __name__ == '__main__':
    main()
