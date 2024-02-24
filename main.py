from TOKEN import TOKEN
from scraper import get_notices
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from message import send_message_to_all_users, send_message_to_user
from database import User, add_user_to_db, is_user_in_db, add_notice_to_db, get_last_notice_from_db


async def handle_auto_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    last_processed_news: str = ""

    async def job_callback(context):
        nonlocal last_processed_news
        post_text = get_notices()
        print(post_text)
        if post_text is not None and post_text != last_processed_news:
            add_notice_to_db(post_text)
            await send_message_to_all_users(context.bot, post_text)
            print("Message sent to all users.")
            last_processed_news = post_text

    context.job_queue.run_repeating(job_callback, interval=60, first=0)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    username = update.effective_user.username
    first_name = getattr(update.effective_user, 'first_name', '')
    last_name = getattr(update.effective_user, 'last_name', '')
    name = first_name + ' ' + \
        last_name if first_name and last_name else first_name or last_name
    if not is_user_in_db(user_id):
        add_user_to_db(User(user_id, username, name))
        await update.message.reply_text("Welcome! To our bot Uiu notice bot")

        latest_notice_text = get_last_notice_from_db()
        if latest_notice_text:
            await send_message_to_user(context.bot, user_id, latest_notice_text)
    else:
        await update.message.reply_text("Welcome back!")

    await handle_auto_update(update, context)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Contact admin for help")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')

if __name__ == '__main__':
    print('Starting bot')
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # error
    app.add_error_handler(error)

    # polling
    print("Polling")
    app.run_polling(poll_interval=3)
