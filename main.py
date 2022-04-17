import io
import logging

from PIL import Image, ImageDraw
from aiogram import Bot, Dispatcher, executor, types

from modules import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.settings.telegram_token)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    new_image = Image.new("RGBA", (1000, 1000))
    draw = ImageDraw.Draw(new_image)

    draw.rounded_rectangle((50, 50, 950, 950), 250, fill="black")

    bytes_img = io.BytesIO()
    new_image.save(bytes_img, "PNG")

    await message.answer_sticker(bytes_img.getvalue())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
