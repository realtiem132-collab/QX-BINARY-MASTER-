import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("8824552633:AAHJYfeyKwOMaQYWU4i2nmc0zWcoGFzP75Q")

IMAGE_URL = "https://raw.githubusercontent.com/realtiem132-collab/Bot-pic1/refs/heads/main/Gemini_Generated_Image_m6tstem6tstem6ts.png"

18$ TO 183$ DAILY PUBLIC 🔥💸

🧤 +93% Accuracy
🧤 Loss Recovery
🧤 Non Mtg Signals
🧤 Daily 10 to 15 Sureshot Signals
🧤 5.5+ Years of Experience in Binary Trading
🧤 Daily Market Insights
🧤 Expert Trading Signals
🧤 Community Support
🧤 24/7 Assistance

🚀 *Let's make profitable trades together!*

https://t.me/+gR00nolNZmA2MGQ1
https://t.me/+gR00nolNZmA2MGQ1
https://t.me/+gR00nolNZmA2MGQ1

👇 *Click Below to Join TRADING KING* 👇"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 JOIN TRADING KING 👑", url="https://t.me/+gR00nolNZmA2MGQ1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=WELCOME_TEXT,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    logger.info("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()