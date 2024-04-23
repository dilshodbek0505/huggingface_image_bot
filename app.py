import logging, os, image_generate
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


load_dotenv()

API_TOKEN = str(os.getenv("BOT_TOKEN"))

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    await msg.answer(f"Salom! {msg.from_user.full_name}\nMen bilan ishlashni davom ettirish uchun rasim yuboring!")

@dp.message_handler(content_types='photo')
async def save_photo(message: types.Message):
    await message.photo[-1].download(destination='img.jpg')
    data = image_generate.query("img.jpg")
    try:
        text = data[0]['generated_text']
        await message.answer_photo(
            photo=message.photo[-1].file_id,
            caption=text
        )
    except:
        await message.answer("Nimadir xatolik bo'ldi! Iltmos qayta urining")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)