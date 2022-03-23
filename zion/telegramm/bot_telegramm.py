import telebot
import zion.mqtt.mqtt as mqtt

bot = telebot.TeleBot('955425525:AAEENrexVMjdX44VHH7xfQ4FFMeByOb9lsQ');


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, kirill ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    message.text = message.text.lower()
    print(message.text)

    if message.text == 'hi':
        print('HELLO')

    mqtt.publish('/telegramm',message.text)


def start():
    print('start_telega')
    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    keyboard1.row('Привет', 'Пока')
    bot.polling()
