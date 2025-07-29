
import telebot

TOKEN = "8244661641:AAEp7eT--fFz_KQZs81BYqfu608qfU02s1uE"
CHAT_ID = "8123321927"
bot = telebot.TeleBot(TOKEN)

# Глобальні змінні для статистики
stats = {
    "visits": 0,
    "form_input": 0,
    "form_submit": 0
}

# Обробка команд з меню
@bot.message_handler(commands=["start", "menu"])
def send_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📊 Переходи", "✍️ Введення", "✅ Надіслано")
    bot.send_message(message.chat.id, "Меню статистики:", reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "📊 Переходи")
def show_visits(message):
    bot.send_message(message.chat.id, f"📊 Кількість переходів: {stats['visits']}")

@bot.message_handler(func=lambda msg: msg.text == "✍️ Введення")
def show_inputs(message):
    bot.send_message(message.chat.id, f"✍️ Кількість введень у формі: {stats['form_input']}")

@bot.message_handler(func=lambda msg: msg.text == "✅ Надіслано")
def show_submits(message):
    bot.send_message(message.chat.id, f"✅ Кількість відправлених форм: {stats['form_submit']}")

# Обробка повідомлень з сайту
@bot.message_handler(func=lambda message: True)
def receive_data(message):
    text = message.text

    if "перейшов на сайт" in text:
        stats["visits"] += 1
    elif "вводити дані" in text:
        stats["form_input"] += 1
    elif "успішно надіслав форму" in text:
        stats["form_submit"] += 1

    # Вивід повідомлення в бот
    bot.send_message(CHAT_ID, text)

bot.polling()
