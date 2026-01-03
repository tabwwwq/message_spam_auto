# Telegram Scheduled Message Sender

This project is a simple bot for automatically sending messages to a Telegram chat or channel on a schedule using the [Telethon](https://github.com/LonamiWebs/Telethon) library in Python.

---

## Features

- **Automated Messaging:** Sends a customizable list of messages automatically at regular intervals to any specified chat (group, channel, supergroup, etc).
- **Randomized Delay:** After posting all messages, the bot waits a random number of minutes before repeating, making behavior look more natural.
- **Easy Configuration:** Just supply your `api_id`, `api_hash`, phone number, `chat_id`, and your list of messages.

---

## Usage

### 1. Get Telegram API credentials

- Visit [my.telegram.org](https://my.telegram.org), log in with your phone number, and create an application.
- Note your `api_id` and `api_hash`.

### 2. Find your `chat_id`

- For groups and channels, you can retrieve it using Telethon, Telegram bots like [userinfobot](https://t.me/userinfobot), or by inspecting Telegram JSON exports.
- Example format: `-1001234567890`

### 3. Edit the script

Replace example values in the script:

```python
api_id = 1234567                # Your API ID from my.telegram.org
api_hash = 'abc123yourhash'     # Your API hash from my.telegram.org
phone = '+1 999 999 9999'       # Your phone number with country code
chat_id = -1001234567890        # Target chat/channel id (starts with -100 for supergroups/channels)
password = 'yourpassword'       # If your account has two-step verification
messages = ["message1", "message2", "message3"]
```

### 4. Install Telethon

```sh
pip install telethon
```

### 5. Run the script

```sh
python your_script_name.py
```

---

## Example Code

```python
from telethon import TelegramClient
import asyncio
import random

api_id = 1234567
api_hash = 'YOUR_API_HASH'
phone = '+1 999 999 9999'
chat_id = -1001234567890
password = 'YOUR_PASSWORD'

messages = ["Hello!", "This is an automated message.", "Stay tuned!"]

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
        print(f"Waiting {wait_minutes} minutes before the next message cycle...")
        await asyncio.sleep(wait_minutes * 60)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Notes

- **Keep your credentials safe.** Never commit your `api_id`, `api_hash`, phone number, or password to public repositories.
- **Telegram limits and anti-spam:** Over-automation or abuse may result in account restrictions or bans. Use responsibly!
- **Two-step verification:** If your account has 2FA, set the `password` variable.
- **Session file:** The first time, the script will create a `session` file for authentication. Reuse it for subsequent logins.

---

## When to Use

- Automated reminders
- Channel or group announcements
- Repeating notifications

---

## License

This project is provided for educational and demonstration purposes. The author is not responsible for any abuse or consequences of use.
