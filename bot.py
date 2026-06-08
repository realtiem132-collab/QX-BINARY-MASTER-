import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# টোকেন এবং লিংকের ভেরিয়েবল
TOKEN = os.getenv("8824552633:AAGgIGBW896M8riJhDwN6FHD6Oyk7uozFxs")
IMAGE_URL = "https://raw.githubusercontent.com/realtiem132-collab/Bot-pic1/refs/heads/main/Gemini_Generated_Image_m6tstem6tstem6ts.png"
CHANNEL_LINK = "https://t.me/+gR00nolNZmA2MGQ1"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # আপনার দেওয়া সম্পূর্ণ টেক্সট মেসেজ
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
    
    # নিচের ইনলাইন বাটন (Inline Button)
    keyboard = [[InlineKeyboardButton("👑 JOIN TRADING KING 👑", url=CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # ছবিসহ মেসেজ ও বাটন পাঠানো
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=IMAGE_URL,
        caption=caption_text,
        reply_markup=reply_markup
    )

def main() -> None:
    if not TOKEN:
        print("Error: BOT_TOKEN variable missing!")
        return
        
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()