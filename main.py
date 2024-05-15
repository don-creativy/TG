import asyncio
from aiogram import Bot, Dispatcher
from handlers import include_routers

bot = Bot(token="7091036049:AAGGLZHLyEUIcKqB6vCviPdxwZktAWL85Kk")
dp = Dispatcher()

async def get_time_notify():
    now = datetime.now()
    return (User.filter(User.time > now).order_by(User.time.asc()).first()).time

async def send_admin():
    send_time = await get_time_notify()
    send_time = time(send_time.hour, send_time.minute)
    await bot.send_message(320720102, "Бот запущен!")
    while True:
        print(datetime.now().time(), send_time)
        now_time = datetime.now().time()
        now_time = time(now_time.hour, now_time.minute)
        if send_time == now_time:
            # рассылка уведомлений всем пользователям
            for user in User.filter(time=send_time):
                await bot.send_message(user.tg_user, 'ping')

            send_time = await get_time_notify()
            print(send_time)

               
        now_time = (datetime.now() + timedelta(minutes=1))
        now_time = datetime(now_time.year, now_time.month, now_time.day, 
                            now_time.hour, now_time.minute)
        seconds = (now_time - datetime.now()).seconds + 1
        print(datetime.now().time(), now_time.time(), seconds)
        await asyncio.sleep(seconds)

async def main():
    include_routers(dp)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())