import discord
from discord.ext import commands
import json

def log_id(id):
    with open("ids.json", "r") as file:
        data = json.load(file)

    if id not in data:
        data.append(id)

        with open("ids.json", "w") as file:
            json.dump(data, file)

        print(" [+]", id, "Total:", len(data))

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(' [!] Started logging ids\n')

@bot.event
async def on_message(message):
    if not message.author.bot:
        log_id(message.author.id)

@bot.event
async def on_raw_reaction_add(payload):
    if not payload.member.bot:
        log_id(payload.member.id)

@bot.event
async def on_member_join(member):
    if not member.bot:
        log_id(member.id)

@bot.event
async def on_member_update(before, after):
    if not after.member.bot:
        log_id(after.member.id)

@bot.event
async def on_voice_state_update(member, before, after):
    if not member.bot:
        log_id(member.id)

bot.run("", bot = False)
