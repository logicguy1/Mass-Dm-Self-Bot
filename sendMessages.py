import discord
import json

client = discord.Client()
token = input(" Enter your token\n> ")
message = input(" Enter your message\n> ")


@client.event
async def on_ready():
    print(" [!] Started Dmming Ids\n")

    with open("ids.json", "r") as file:
        data = json.load(file)

    for index, user_id in enumerate(data):
        member = await client.fetch_user(user_id)
        try:
            await member.send(message)
            print(f" [+] Sent message {index + 1} / {len(data)}")
        except Exception as e:
            print(f" [!] {e}")

    print(" [+] Done")

    await client.close()  # Close bot


client.run(token, bot=False)
