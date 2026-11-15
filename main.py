import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to AI Quotex OTC Bot!\n\n"
        "Your bot is online!\n"
        "Use /help for commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start the bot\n"
        "/help - Show help"
    )

def main():
    token = os.environ["BOT_TOKEN"]
    render_url = os.environ["RENDER_EXTERNAL_URL"].rstrip("/")
    port = int(os.environ.get("PORT", "10000"))

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path="telegram-webhook",
        webhook_url=f"{render_url}/telegram-webhook",
    )

if __name__ == "__main__":
    main()
