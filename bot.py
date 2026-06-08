from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8824552633:AAHTo6LiHHSgMOfHnJdhjNYbt3gMWnSK9gQ"

IMAGE_URL = "https://raw.githubusercontent.com/realtiem132-collab/Bot-pic1/refs/heads/main/Gemini_Generated_Image_m6tstem6tstem6ts.png"

CHANNEL_LINK = "https://t.me/+gR00nolNZmA2MGQ1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "18$ TO 183$ DAILY PUBLIC 🔥💸\n\n"
        "💠+93% Accuracy\n"
        "💠Loss Recovery\n"
        "💠Non Mtg Signals\n"
        "💠Daily 10 to 15 Sureshot Signals\n"
        "💠5.5+ Years of Experience in Binary Trading\n"
        "💠Daily Market Insights\n"
        "💠Expert Trading Signals\n"
        "💠Community Support\n"
        "💠24/7 Assistance\n\n"
        "🚀Let's make profitable trades together!\n\n"
        "https://t.me/+gR00nolNZmA2MGQ1\n"
        "https://t.me/+gR00nolNZmA2MGQ1\n"
        "https://t.me/+gR00nolNZmA2MGQ1"
    )

    keyboard = [[InlineKeyboardButton("👇 Click on Below Button to Join TRADING KING 👇", url=CHANNEL_LINK)]]

    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
