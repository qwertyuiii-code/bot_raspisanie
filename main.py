import asyncio.exceptions
from telethon import TelegramClient, events
from loguru import logger
from datetime import datetime
import requests
import config as cfg

bot = TelegramClient("cock", api_id=cfg.API_ID, api_hash=cfg.API_HASH).start(bot_token=cfg.TOKEN)

@bot.on(events.NewMessage(pattern="/shit"))
async def main_command_handler(msg):
    logger.info("Получил запрос расписания")
    mymsg = await msg.reply("Напиши мне название группы")
    try:
        async with bot.conversation(msg.chat, timeout=60) as conv:
            reply = await conv.get_response(mymsg)
    except asyncio.exceptions.TimeoutError:
        logger.info("типо ждем")
        return

    name = reply.text
    response = requests.get('https://erp.nttek.ru/api/schedule/legacy/' + str(datetime.now().date()) + "/group/" + name)
    if response.status_code != 200:
        await reply.reply("Ошибка, проверьте правильность написания имени, либо на данный день недели нету расписания")
        return

    response_raw_json = response.json()
    schedule_textified = ""
    for lesson in response_raw_json["schedule"]:
        schedule_textified += "• " + lesson["name"] + " - " + lesson["teachers"][0] + " - " + lesson["rooms"][0] + "\n"
    await reply.reply(schedule_textified)

    logger.error("хуйня переделывай...")



logger.success("Ожидаю команды...")
bot.run_until_disconnected()
