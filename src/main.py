from aiogram import Bot, Dispatcher, executor, types, filters

from bsod import crash_pc, freeze_disk
from config import TG_ADMIN_USER_ID, TGBOT_TOKEN


bot = Bot(token=TGBOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(filters.IDFilter(TG_ADMIN_USER_ID),
                    filters.Command(['bsod', 'killswitch']))
async def killswitch_handler(msg: types.Message):
    freeze_disk()
    await msg.reply('turning off..')
    crash_pc()


@dp.message_handler(filters.IDFilter(TG_ADMIN_USER_ID))
async def unknown_command_handler(msg: types.Message):
    await msg.reply('Hello, Confi!\n\nType /bsod or /killswitch')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
