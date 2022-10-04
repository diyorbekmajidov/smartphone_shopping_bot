from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup,InputMediaPhoto
import telegram
import db 
db = db.DB('db.json')

TOKEN='5675498896:AAEvbgMA01S0Jy_jiqhg1RtE63_cvrM67dU'
updater=Updater(TOKEN)

def start(update:Update, context:CallbackContext):
    button1 = InlineKeyboardButton('Vivo',callback_data='📱Vivo')
    button2 = InlineKeyboardButton('Redmi', callback_data="📱Redmi")
    button3 = InlineKeyboardButton("Samsung", callback_data="📱Samsung")
    button4 = InlineKeyboardButton("Apple", callback_data="📱Apple")
    button5 = InlineKeyboardButton("Nokia",callback_data="📱Nokia")
    button6 = InlineKeyboardButton("Oppo", callback_data="📱Oppo")
    button7 = InlineKeyboardButton("Huawei", callback_data="📱Huawei")
    reply_markup = InlineKeyboardMarkup([[button1,button2,button3],[button5,button6,button7],[button4]])
    update.message.reply_text(text=" Phone\n MI,Apell,Vivo,Samsung",reply_markup=reply_markup)

def mobile_button(update:Update, context:CallbackContext):
    query=update.callback_query
    company_quere = query.data[1:]
    company_data = db.company_name(company_quere)
    keyboard1 = []
    keyboard2 = []
    keyboard3 = InlineKeyboardButton("➡️", callback_data = "➡️Next")
    keyboard4 = InlineKeyboardButton("❌", callback_data = "❌cancel")
    keyboard5 = InlineKeyboardButton("⬅️", callback_data = "⬅️arrowleft")
    str_button = 'Mobilni tanlang\n\n' 
    n = 1
    for i in company_data:
        if n <= 10:
            if len(keyboard1)<5:
                str_button += str(n)+". "+i + '\n'
                keyboard1.append(InlineKeyboardButton(str(n),callback_data=f'📲{i}'))
            else:
                str_button += str(n)+". "+i + '\n'
                keyboard2.append(InlineKeyboardButton(str(n),callback_data=f'📲{i}'))
        n += 1
    reply_markup=InlineKeyboardMarkup([keyboard1,keyboard2,[keyboard5,keyboard4,keyboard3]])
    query.edit_message_text(str_button, reply_markup=reply_markup)

def cancel(update:Update, context:CallbackContext):
    data = db.company_name()
    if query.data == "➡️Next" :


def onclick(update:Update, context:CallbackContext):
    # query = Query()
    bot=context.bot 
    query=update.callback_query
    chat_id = query.message.chat.id 
    data = db.company_mobil_imeg(query.data[1:])
    img_url = data[0]["img_url"]
    name=data[0]["name"]
    company=data[0]["company"]
    color = data[0]["color"]
    memory=data[0]["memory"]
    price = data[0]["price"]
    Ram = data[0]["RAM"]
    caption = f'Mobil company:{company}\n\nMobil name:{name}\nMobil color:{color}\nMobil RAM:{Ram}\nMobil memory:{memory}\nMobil price:{price}'
    bot.sendPhoto(chat_id,img_url,caption)




updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CallbackQueryHandler(mobile_button, pattern='📱'))
updater.dispatcher.add_handler(CallbackQueryHandler(onclick, pattern='📲'))


updater.start_polling()
updater.idle()

