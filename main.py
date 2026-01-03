from telethon import TelegramClient
import asyncio
import random

api_id = * # api_hash my.telegram.org
api_hash = '9hj12easdasda123dasas78sad782ddda' # api_hash visit my.telegram.org
phone = '+1 999 999 9999' #phone number visit my.telegram.org
chat_id = -100********** # chat_id
password = '**********'  # your Telegram password

messages = ["message1", "message2", "message3"]

async def main():
    client = TelegramClient('session', api_id, api_hash)
    await client.start(phone=phone, password=password)
    print("Authorization successful")

    while True:
        for msg in messages:
            print(f"Trying to send a message: {msg}")
            try:
                result = await client.send_message(chat_id, msg)
                print(f"Message sent! API response: {result}")
            except Exception as e:
                print(f"Error sending message: {e}")
            await asyncio.sleep(10)  # 10 seconds between messages

        wait_minutes = random.randint(121, 130)
        print(f"Delay {wait_minutes} minutes until the next sending cycle...")
        await asyncio.sleep(wait_minutes * 60)

if __name__ == "__main__":
    asyncio.run(main())
