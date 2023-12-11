import random
import string
import telebot

# Создание экземпляра бота с помощью токена
bot = telebot.TeleBot('6671933355:AAHDjP8ZIHh2e4sA7geU0tN4XUsEO-dLR_o')

# Словарь для хранения паролей игроков
passwords = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Генерация случайного пароля
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Сохранение пароля для пользователя
    passwords[message.chat.id] = password

    # Отправка пароля пользователю
    bot.send_message(message.chat.id, f"Ваш пароль для входа в игру: {password}")

# Обработчик ввода пароля
@bot.message_handler(func=lambda message: True)
def check_password(message):
    # Проверка введенного пароля
    if message.text == passwords.get(message.chat.id):
        bot.send_message(message.chat.id, "Вы успешно вошли в игру!")
    else:
        bot.send_message(message.chat.id, "Неверный пароль!")

# Запуск бота
bot.polling()
