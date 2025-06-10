import telebot

TOKEN = "8199006545:AAHHmZD2Tj2TOTNj7Ig2flD9agm_5rMuqBk"
bot = telebot.TeleBot(TOKEN)

referral_url = "https://otieu.com/4/9431817"

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id
    args = message.text.split()
    if len(args) > 1:
        bot.send_message(user_id, f"👋 Welcome! You were referred by ID: {args[1]}")
    else:
        bot.send_message(user_id, "👋 Welcome to Crypto Dogs Bot!")

    msg = (
        f"\n🎯 Earn tokens here:\n👉 {referral_url}\n\n"
        f"🔗 Share your referral link:\n"
        f"https://t.me/CryptoDogsEarningBot?start={user_id}"
    )
    bot.send_message(user_id, msg)

bot.polling()
