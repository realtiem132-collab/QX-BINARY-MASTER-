import os
from flask import Flask
import threading
import telebot
from telebot import types

TOKEN = '8824552633:AAHPfTf1ZnHnW_i3gsHJnJdFIe4j3nL9XSY'
bot = telebot.TeleBot(TOKEN)
app = Flask('')

# ✅ আপনার Telegram User ID এখানে বসান
ADMIN_ID = 7867534011  # 👈 আপনার আসল ID দিন

@app.route('/')
def home():
    return "Bot is running perfectly!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# ✅ সকল user ID store করার জন্য
user_ids = set()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_ids.add(message.chat.id)  # user ID save করা

    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton('Market Analysis')
    btn2 = types.KeyboardButton('🧠 Trading Logic')
    btn3 = types.KeyboardButton('⚠️ Risk Management')
    markup.add(btn1, btn2, btn3)

    photo_url = 'https://raw.githubusercontent.com/realtiem132-collab/Bot-pic1/refs/heads/main/Gemini_Generated_Image_m6tstem6tstem6ts.png'

    caption = (
        "18$ TO 183$ DAILY PUBLIC 🔥💸\n"
        "আপনি কি 𝐐𝐔𝐎𝐓𝐄𝐗 এ লস করেছেন ?\n\n"
        "এবার জয় করার পালা 𝐐𝐔𝐎𝐓𝐄𝐗 𝐀𝐈\n"
        "𝐒𝐈𝐆𝐍𝐀𝐋 𝐁𝐎𝐓  দিয়ে ধাপে ধাপে লস\n"
        "রিকোভারি করুন। টার্গেট 100% Live\n"
        "সিগন্যাল পেতে চ্যানেলে জয়েন করুন।\n"
        "👇\n\n"
        "𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐋𝐈𝐍𝐊\n"

        "https://t.me/+swR7BhguPPQxZDc1\n"
        "https://t.me/+swR7BhguPPQxZDc1\n"
        "https://t.me/+swR7BhguPPQxZDc1\n\n\n"
        "👇 Click on Below Button to Join TRADING KING 👇🇧🇩"
    )

    bot.send_photo(message.chat.id, photo_url, caption=caption, reply_markup=markup)

# ✅ Broadcast command
@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    if message.chat.id != ADMIN_ID:
        bot.send_message(message.chat.id, "❌ You are not authorized to use this command.")
        return

    # /broadcast এর পরের text নেওয়া
    text = message.text[len('/broadcast'):].strip()

    if not text:
        bot.send_message(message.chat.id, "⚠️ Please write a message after /broadcast\nExample: /broadcast Hello everyone!")
        return

    success = 0
    failed = 0
    for uid in user_ids:
        try:
            bot.send_message(uid, text)
            success += 1
        except Exception:
            failed += 1

    bot.send_message(message.chat.id, f"✅ Broadcast done!\n📤 Sent: {success}\n❌ Failed: {failed}")

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    user_ids.add(message.chat.id)  # যেকোনো message এ user ID save

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