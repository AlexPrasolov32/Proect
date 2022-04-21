import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def help(update, context):
    update.message.reply_text(
        "Я бот музыкант, могу подобрать музыку по жанрам.")


def Grange(update, context):
    update.message.reply_text(
        "Three Days Grace - i hate everything about you    "
        "Breaking Benjamin - The Diary of Jane    "
        "Poets of the Fall - Carnival of Rust    "
        "Nirvana - Smells Like Teen Spirit    ")


def Punk(update, context):
    update.message.reply_text(
        "The Offspring - You're Gonna Go Far Kid    "
        "Sum 41 - Still Waiting    "
        "Sex Pistols - Anarchy In The UK    "
        "Rise Against - Give It All    ")


def Hard(update, context):
    update.message.reply_text(
        "Led Zeppelin - Black Dog    "
        "Guns N' Roses - November Rain    "
        "Bon Jovi - It's My Life    "
        "Scorpions - Rock You Like A Hurricane    ")


def Trash(update, context):
    update.message.reply_text(
        "Metallica - Master Of Puppets    "
        "Slayer - Raining Blood    "
        "Megadeth - Peace Sells    "
        "Annihilator - Phoenix Rising    ")


def Metalcore(update, context):
    update.message.reply_text(
        "Ice Nine Kills - Welcome To Horrorwood    "
        "Memphis May Fire - Left For Dead    "
        "Motionless In White - Another Life    "
        "Killswitch Engage - The End of Heartache    ")


def alternative(update, context):
    update.message.reply_text(
        "Papa Roach - Last Resort    "
        "Linkin Park - What I've Done    "
        "Bring Me The Horizon - Throne    "
        "Fight The Fade - Second Horizon    ")



def Rapcore(update, context):
    update.message.reply_text(
        "Limp Bizkit - My Generation    "
        "Hollywood Undead - No. 5    "
        "Falling In Reverse - Drugs    "
        "From Ashes to New - Enough    ")


def Old(update, context):
    update.message.reply_text(
        "Eminem - Not Afraid    "
        "50 Cent - Just A Lil Bit    "
        "2Pac - Old School    "
        "Wu-Tang Clan - C.R.E.A.M.    ")


def rok(update, context):
    reply_keyboard = [['/Grange', '/Punk'],
                      ['/Hard', '/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        "Я бот-музыкант, какой поджанр предпочитаете?",
        reply_markup=markup
    )


def met(update, context):
    reply_keyboard = [['/Trash', '/Metalcore'],
                      ['/alternative', '/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        "Я бот-музыкант, какой поджанр предпочитаете?",
        reply_markup=markup
    )


def rap(update, context):
    reply_keyboard = [['/Rapcore', '/Old'],
                      ['/back']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        "Я бот-музыкант, какой поджанр предпочитаете?",
        reply_markup=markup
    )


def start(update, context):
    reply_keyboard = [['/Rock', '/Metal'],
                      ['/Rap', '/Help']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        "Я бот-музыкант, какой жанр предпочитаете?",
        reply_markup=markup
    )


def main():
    updater = Updater('5108607488:AAGLSHhDf0TYrDR8rzlxMfClGuK8TLwX-5Y')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("Rock", rok))
    dp.add_handler(CommandHandler("Metal", met))
    dp.add_handler(CommandHandler("Rap", rap))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("back", start))
    dp.add_handler(CommandHandler("Grange", Grange))
    dp.add_handler(CommandHandler("Punk", Punk))
    dp.add_handler(CommandHandler("Hard", Hard))
    dp.add_handler(CommandHandler("Trash", Trash))
    dp.add_handler(CommandHandler("Metalcore", Metalcore))
    dp.add_handler(CommandHandler("alternative", alternative))
    dp.add_handler(CommandHandler("Rapcore", Rapcore))
    dp.add_handler(CommandHandler("Old", Old))
    updater.start_polling()


if __name__ == '__main__':
    main()
