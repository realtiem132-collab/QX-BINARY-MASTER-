import os
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# সরাসরি টোকেন ও লিংক
TOKEN = "8824552633:AAGgIGBW896M8riJhDwN6FHd60yk7uozFxs"
IMAGE_URL = "https://raw.githubusercontent.com/realtiem132-collab/Bot-pic1/refs/heads/main/Gemini_Generated_Image_m6tstem6tstem6ts.png"
CHANNEL_LINK = "https://t.me/+gR00nolNZmA2MGQ1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    caption_text = (
        "18$ TO 183$ DAILY PUBLIC 🔥💸\n\n"
        "🧤+93% Accuracy\n"
        "🧤Loss Recovery\n"
        "🧤Non Mtg Signals\n"
        "🧤Daily 10 to 15 Sureshot Signals\n"
        "🧤5.5+ Years of Experience in Binary Trading\n"
        "🧤Daily Market Insights\n"
        "🧤Expert Trading Signals\n"
        "🧤Community Support\n"
        "🧤24/7 Assistance\n\n"
        "🚀Let's make profitable trades together!\n\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n"
        f"{CHANNEL_LINK}\n\n"
        "👇 Click on Below Button to Join TRADING KING 👇"
    )
    
    keyboard = [[InlineKeyboardButton("👑 JOIN TRADING KING 👑", url=CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=IMAGE_URL,
        caption=caption_text,
        reply_markup=reply_markup
    )

async def main() -> None:
    # অ্যাপ্লিকেশন তৈরি
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    # বোটের পোলিং শুরু এবং সেশন সচল রাখা
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    print("Bot is running perfectly...")
    
    # সার্ভারে বোটটিকে বন্ধ হওয়া থেকে আটকে রাখার লুপ
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    # Event Loop এর ত্রুটি দূর করার সঠিক পদ্ধতি
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped.")