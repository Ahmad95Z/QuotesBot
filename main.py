import requests
import random
import telebot
from bs4 import BeautifulSoup as b


URL = 'https://finewords.ru/cit/citaty-iz-knig'

API_KEY = '5596452229:AAHFCDSdgMEL64JEu2UfCQJlK6Yghd7ZW9c'

def parser(url):
    r = requests.get(url)
    soup = b(r.text,'html.parser')
    quotes = soup.find_all('div',class_ = 'cit')
    return  [i.text for i in quotes] 

list_job = parser(URL)
random.shuffle(list_job)  

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id,'Привет! Выбери любую цифру:')

@bot.message_handler(content_types=['text'])

def quot(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id,list_job[0])
        del list_job[0]
    else:
        bot.send_message(message.chat.id,'Введите  цифру!')

bot.polling()
