import os
from flask import Flask
import threading
import telebot
from telebot import types

TOKEN = '8824552633:AAG6HLfCGxt8ONpAdbPA-efFO4W4vYTZ-k0'
bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running perfectly!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton('Market Analysis')
    btn2 = types.KeyboardButton('🧠 Trading Logic')
    btn3 = types.KeyboardButton('⚠️ Risk Management')
    markup.add(btn1, btn2, btn3)

    photo_url = 'https://raw.githubusercontent.com/realtiem132-collab/Bot-pic1/refs/heads/main/Gemini_Generated_Image_m6tstem6tstem6ts.png'

    caption = (
        "18$ TO 183$ DAILY PUBLIC 🔥💸\n"
        "Bangladesh 🇧🇩\n\n"
        "🧤+93% Accuracy 🇧🇩\n"
        "🧤Loss Recovery 🇧🇩\n"
        "🧤Non Mtg Signals 🇧🇩\n"
        "🧤Daily 10 to 15 Sureshot Signals\n"
        "🧤5.5+ Years of Experience in Binary Trading 🇧🇩\n"
        "🧤Daily Market Insights 🇧🇩\n"
        "🧤Expert Trading Signals 🇧🇩\n"
        "🧤Community Support 🇧🇩\n"
        "🧤24/7 Assistance 🇧🇩\n\n"
        "🚀Let's make profitable trades together!\n\n"
        "https://t.me/+swR7BhguPPQxZDc1\n"
        "https://t.me/+swR7BhguPPQxZDc1\n"
        "https://t.me/+swR7BhguPPQxZDc1\n\n\n"
        "👇 Click on Below Button to Join TRADING KING 👇🇧🇩"
    )

    bot.send_photo(message.chat.id, photo_url, caption=caption, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == 'Market Analysis':
        reply = ("**📊 Market Analysis**\n\nWelcome to our Market Analysis section! We monitor major asset pairs and OTC markets.\n\n* **Style:** 1-minute candlestick charts for fast setups.\n* **Indicators:** Our tools leverage Bollinger Bands, Stochastic, and Keltner Channels.")
        bot.send_message(message.chat.id, reply, parse_mode='Markdown')
    elif message.text == '🧠 Trading Logic':
        reply = ("**🧠 Trading Logic**\n\nTrading is 10% strategy and 90% discipline.\n\n* **Rules:** Always wait for a clear confirmation candle.\n* **Accuracy:** Our premium setups maintain 70-80% accuracy to avoid market noise.")
        bot.send_message(message.chat.id, reply, parse_mode='Markdown')
    elif message.text == '⚠️ Risk Management':
        reply = ("**⚠️ Risk Management Rules**\n\nProtecting your capital is your number one job.\n\n* **Max Risk:** Never risk more than 1% to 2% per trade.\n* **Overtrading:** Set a daily profit and loss limit. Once hit, close the platform.")
        bot.send_message(message.chat.id, reply, parse_mode='Markdown')

if __name__ == "__main__":
    t = threading.Thread(target=run_flask)
    t.start()
    bot.polling(none_stop=True)