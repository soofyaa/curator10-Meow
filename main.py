import telebot
import random

bot = telebot.TeleBot('6848604801:AAFKaDJtFj_x8MvgFaz429a6HK09xCpcrQk')
random_message = lambda: random.choice(predskazaniemas)
predskazaniemas = ['Сегодня нужно будет потрудиться', 'Завтра тебя ждет удачный день', ' Сегодня лучше отдохнуть',
                   'Встреча с друзьями принесет положительные эмоции']


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет,Я бот _Толик!_ /nТы можешь узнать что я умею нажав команду /help',
                     parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,
                     '*Вот что я могу:* \n/prediction - предсказание на день \n/link - ссылка на секретного бота который делает картинки',
                     parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'ЭТО [ССЫЛКА](https://t.me/kandinsky21_bot)', parse_mode='Markdown')


@bot.message_handler(commands=['prediction'])
def main(message):
    bot.send_message(message.chat.id, random_message(), parse_mode='Markdown')


bot.infinity_polling()