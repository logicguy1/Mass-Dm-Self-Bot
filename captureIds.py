import discord
import json

with open("ids.json", "r") as file:
    data = json.load(file)

def log_id(member):
    if member.bot: # Skip bots
        return

    user_id = member.id
    if user_id not in data:
        data.append(user_id)

        with open("ids.json", "w") as file:
            json.dump(data, file)

        print(f" [+] {user_id} Total: {len(data)}")

client = discord.Client()
token = input("Enter your token\n> ")

@client.event
async def on_ready():
    print(' [!] Started logging ids\n')

@client.event
async def on_message(message):
    log_id(message.author)

@client.event
async def on_raw_reaction_add(payload):
    log_id(payload.member)

@client.event
async def on_member_join(member):
    log_id(member)

@client.event
async def on_member_update(before, after):
    log_id(after.member)

@client.event
async def on_voice_state_update(member, before, after):
    log_id(member)

client.run(token, bot = False)
