import discord
import json

with open("ids.json", "r") as file:
    data = json.load(file)

def log_id(user_id):
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
    if not message.author.bot:
        log_id(message.author.id)

@client.event
async def on_raw_reaction_add(payload):
    if not payload.member.bot:
        log_id(payload.member.id)

@client.event
async def on_member_join(member):
    if not member.bot:
        log_id(member.id)

@client.event
async def on_member_update(before, after):
    if not after.member.bot:
        log_id(after.member.id)

@client.event
async def on_voice_state_update(member, before, after):
    if not member.bot:
        log_id(member.id)

client.run(token, bot = False)
