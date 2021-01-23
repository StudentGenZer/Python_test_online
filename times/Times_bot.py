file = open("start.txt","r")
start_word = file.read()
file.close()
file = open("info.txt","r")
info = file.read()
file.close()
arr_info = info.split("\n")
import telebot
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row("1","2","3","4","5","6","7")
keyboard.row("8","9","10","11","12","13","14")
keyboard.row("15","16","17","18","19","20","21")
keyboard.row("22","23","24","25","26","27","28")
bot = telebot.TeleBot('955395141:AAGBLJSd1DIq7OKpxakFtS9E4oEXMt9Y010')
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.from_user.id,start_word,reply_markup = keyboard)
@bot.message_handler(content_types = ['text'])
def question(message):
    if message.text.isdigit():
        if int(message.text) >=1 and int(message.text)<=28:
            bot.send_message(message.from_user.id,arr_info[int(message.text)-1],reply_markup = keyboard)
        else:
            bot.send_message(message.from_user.id,"Error",reply_markup = keyboard)
    else:
        bot.send_message(message.from_user.id,"Error",reply_markup = keyboard)
bot.polling()
