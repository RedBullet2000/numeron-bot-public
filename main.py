import datetime
import json
import os
from pathlib import Path
import platform
import sys

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
    print(f'Python {sys.version}')
    print(f'Discordpy {discord.__version__}')


@bot.command(aliases=['info'])
async def help(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f":pushpin: {bot.user.name}の利用方法",
                          description=f"コマンドの先頭には「n/」が必要です。コマンドがわからなくなったら「n/help」でこのヘルプを表示出来ます。\n"
                                      f"コマンド数：{len(bot.commands)}"
                                      f"\n\n**:scroll: How to Play Numer0n (バトルモード)**"
                                      f"\n(※ヌメロンのルールについては「n/rule」でご確認ください。)"
                                      f"\n\n:one: 「n/create」でゲームを作成する。"
                                      f"\n\n:two: 「n/join」を参加者本人が入力してゲームに参加する。\n(※「n/player」で現在の参加者を確認できます。)"
                                      f"\n\n:three: 「n/start」でゲーム開始。\n(※参加者が2人いないと開始できません)"
                                      f"\n\n:four:  BOTから届いたDMを確認してDMでゲームを進める。",
                          color=ctx.author.color)
    embed.timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.add_field(name='コマンド',
                    value='`rule`,`solo`,`create`,`join`,`leave`,`start`,`set_nothing`,`set_playing`,'
                          '`game_status`,`help`,`bot_info`',
                    inline=False)
    embed.set_footer(text=f"{bot.user.name}, Made by Red_Bullet/ブルさん*#9592", icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def bot_info(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=':pushpin: Numer0n-Botについて',
                          description='Numer0n-Botは、以前民放で放映されていた対戦型のゲームNumer0nをdiscordのサーバー上で遊べるようにしたものです。 '
                                      '現在、ソロモードと対戦モードが実装されています。',
                          color=ctx.author.color)
    embed.timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    embed.add_field(name='開発環境',
                    value=f'Python **{platform.python_version()}**\nDiscordpy **{discord.__version__}**')
    embed.add_field(name='ライセンス',
                    value='This bot is under **[MIT license](https://en.wikipedia.org/wiki/MIT_License)**')
    embed.add_field(name='開発者', value=f'Red_Bullet/ブルさん*#9592')
    embed.add_field(name='GitHubレポジトリ',
                    value='**[Numer0n-Bot Project](https://github.com/RedBullet2000/numeron-bot-public)**')
    embed.add_field(name='ファイル構造',
                    value='↓(詳細は上記レポジトリのREADME.md参照)',
                    inline=False)
    embed.set_image(url='https://i.gyazo.com/3a415c57ad3247511a837815b4bfc966.png')
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=f"{bot.user.name}, Made by Red_Bullet/ブルさん*#9592", icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)


if __name__ == '__main__':
    for file in os.listdir(cwd + '/cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')

bot.run(TOKEN)
