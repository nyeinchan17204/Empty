from pyrogram import Client,filters
import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

app_id = "7693500"
app_hash = "8d82e2ae3917b001afb9a3e2c1ba2ce6"
bot_token = "5481750969:AAGusiUIOdwebDrianaUzk7w-64uUBzupak"
app = Client("Test",api_id=app_id,api_hash=app_hash,bot_token=bot_token)
LOGGER.info("starting bot")

@app.on_message(filters.command('start'))
async def start(_,message):
  await message.reply('It is me Moe Nya')

app.start()