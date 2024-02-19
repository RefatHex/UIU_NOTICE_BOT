import time
from TOKEN import TOKEN
from scraper import get_notices
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global post_text
    await update.message.reply_text("Hello! Thanks for using our BOT.\nPlease use /get_updates command to get articles ")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("contact admin")


async def get_updates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_auto_update(update, context)


async def handle_auto_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    last_processed_news: str = ""
    await update.message.reply_text("From now on, you'll be receiving updates")

    async def job_callback(context):
        nonlocal last_processed_news
        post_text = get_notices()
        if post_text is not None and post_text != last_processed_news:
            await context.bot.send_message(update.effective_chat.id, text=post_text)
            print(post_text)
            last_processed_news = post_text
        print(post_text)

        time.sleep(60*60)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')

if __name__ == '__main__':
    print('Starting bot')
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('get_updates', get_updates))

    # error
    app.add_error_handler(error)

    # polling
    print("Polling")
    app.run_polling(poll_interval=3)
