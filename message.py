from database import read_users_from_db


async def send_message_to_user(bot, user_id, message):
    await bot.send_message(int(user_id), text=message)


async def send_message_to_all_users(bot, message):
    users = read_users_from_db()
    for user in users:
        await send_message_to_user(bot, user.user_id, message)
