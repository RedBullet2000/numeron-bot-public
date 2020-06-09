import datetime
import json
import os
from pathlib import Path

import discord
from discord.ext import commands

from cogs.utils.game import Game

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f'{cwd}\n----')

bot = commands.Bot(command_prefix='n/')
bot.remove_command('help')
bot.cwd = cwd

with open('secret.json', 'r') as token:
    secret = json.load(token)
    TOKEN = secret["TOKEN"]

bot.game = Game()


@bot.event
async def on_ready():
    # 起動処理
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f"{bot.user.name}の機能について",
                          description=f"コマンドの先頭には「n/」が必要です。コマンドがわからなくなったら「n/help」でこのリストを表示出来ます。\nコマンド数：{len(bot.commands)}",
                          color=0xff80ff)
    embed.timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.add_field(name='コマンド', value='`rule`,`solo`,`vs`,')
    embed.set_footer(text=f"{bot.user.name}, Made by Red_Bullet/ブルさん*#9592", icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)


if __name__ == '__main__':
    for file in os.listdir(cwd + '/cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')

bot.run(TOKEN)
