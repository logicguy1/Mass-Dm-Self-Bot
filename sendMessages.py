import discord
import json

client = discord.Client()

@client.event
async def on_ready():
    print(' [!] Started Dmming Ids\n')

    with open("ids.json", "r") as file:
        data = json.load(file)

    for index, user_id in enumerate(data):
        member = await client.fetch_user(user_id)
        try:
            await member.send("YOUR MESSAGE HERE")
            print(f" [+] Sent message {index + 1} / {len(data)}")
        except Exception as e:
            print(f" [!] {e}")

    print(" [+] Done")

bot.run("", bot = False)
