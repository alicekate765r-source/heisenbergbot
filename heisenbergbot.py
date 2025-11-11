from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "TON_NOUVEAU_TOKEN_ICI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_url = "https://i.ibb.co/7RCZRLg/heisenberg-poster.jpg"
    keyboard = [
        ["📢 Canal", "🥔 Potato"],
        ["🧭 Menu Mini-App"],
        ["🛒 Commander", "ℹ️ Informations"],
        ["📞 Tous les contacts"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_photo(
        photo=photo_url,
        caption="👋 *Bienvenue sur HeisenbergBOT !*\n\nChoisissez une option ci-dessous pour continuer ⬇️",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🤖 HeisenbergBOT est en ligne...")
app.run_polling()
