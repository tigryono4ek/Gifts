import telebot
import random
from telebot import types

bot = telebot.TeleBot('8005835605:AAEopoivC4PlU-dhZZkKy98qC26b7DXYuSo')


gifts = [
    "5% скидка на процедуру мезотерапии",
    "5% скидка на процедуру ботулинотерапии",
    "5% скидка на контурную пластику губ",
    "5 % скидка на контурную пластику носогубных складок",
    "5% скидка на игольчатый RF лифтинг"   ,
    "5% скидка на SMAS" ,
    "Молочко для демакияжа",
    "Тоник",
    # ... добавляй сколько нужно
]

@bot.message_handler(commands=['start'])
def start_comand(message):
    gift = random.choice(gifts)
    bot.reply_to(message, gift)

bot.polling()

bot.polling(none_stop=True, interval=0)