import os
import discord
import asyncio
from pystyle import Colors, Colorate
from datetime import datetime
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("$ven1337 X Kotaro666")
os.system('cls' if os.name == 'nt' else 'clear')  
print(Colorate.Horizontal(Colors.rainbow, """
                                            ⠀⠀⠀⠀⠀⠀⠀⣠⣒⣪⡝⠃⠀⠀⠀⠀⠀⠀⠀⣀⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⣷⡀⠀⠀⣀⣄⢠⣾⣿⣿⣷⣴⠂⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣴⣿⣿⠏⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼⣿⣿⣿⣽⣿⣿⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⠁⣀⣿⣿⣿⣿⡻⣿⣟⠆⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⢀⣠⣤⠶⢿⠟⠙⢻⣿⣿⣿⣿⠃⠘⣿⣿⣿⣿⡟⠋⣛⡿⣷⠦⣄⣀⠀⠀
                                            ⢀⣴⠋⠁⣾⣿⣿⣿⣷⣄⣹⣿⣿⠟⠀⠀⠛⣿⣿⣯⣴⣾⣿⣿⣿⣷⠀⠙⢷⡀
                                            ⠉⠁⠀⠀⠙⢿⡿⣿⣿⣷⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣾⣿⣿⢿⡿⠃⠀⠀⠈⠁
                                            ⠀⠀⠀⠀⠀⠈⢻⣟⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣯⠉⠁⠀⠀⠀⠀⣰⠃⠈⠉⢿⣿⣿⢄⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠨⠿⠿⠁⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⣀⡠⠬⢿⠿⠭⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠥⠤⠄⠐⠊⠀⠀⠀⠀
    """))


async def send_messages(token, target_id, message_content):
    num_messages = 200

    try:
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            print(Colorate.Horizontal(Colors.rainbow, f'Successfully Logged In As {client.user.name} using token {token}'))

            try:
                target_user = await client.fetch_user(int(target_id))

                for i in range(num_messages):
                    try:
                        await target_user.send(message_content)
                        current_time = datetime.now().strftime('%H:%M:%S')
                        print(Colorate.Horizontal(Colors.rainbow, f"{current_time}: Message sent to {target_user.name}"))
                    except discord.Forbidden:
                        print(Colorate.Horizontal(Colors.rainbow, f"Failed to send message. The user may have disabled direct messages or blocked the bot."))
                        break
                    except Exception as e:
                        print(Colorate.Horizontal(Colors.rainbow, f"An error occurred while sending message: {e}"))
                        break
            finally:
                await client.close()

        await client.start(token)
    except Exception as e:
        print(Colorate.Horizontal(Colors.rainbow, f"An error occurred {e}"))

async def main():
    try:
        with open('token.txt', 'r') as file:
            tokens = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(Colorate.Horizontal(Colors.rainbow, f"token.txt not found"))
        return

    target_id = input("Discord User ID: ")
    message_content = input("Message: ")

    tasks = [send_messages(token, target_id, message_content) for token in tokens]

    try:
        await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        print(Colorate.Horizontal(Colors.rainbow, f"\n Stopped"))

if __name__ == "__main__":
    asyncio.run(main())