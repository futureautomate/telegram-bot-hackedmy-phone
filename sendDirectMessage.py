import tokenKey
import telegram

bot = telegram.Bot(token=tokenKey.BOT_TOKEN)

bot.send_message(chat_id = tokenKey.CHAT_ID,text = 'Hi Wass up?')
