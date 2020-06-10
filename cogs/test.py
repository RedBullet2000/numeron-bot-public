import discord
from discord.ext import commands

from cogs.utils.player import Player
from cogs.utils import game


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create(self, ctx):
        if self.bot.game.status == 'playing':
            await ctx.send('ゲーム中です。')
            return
        if self.bot.game.status == 'waiting':
            await ctx.send('既に参加者募集中です。')
            return
        self.bot.game.status = 'waiting'
        self.bot.game.channel = ctx.channel
        await ctx.send('参加者の募集を開始しました。')

    @commands.command()
    async def join(self, ctx):
        if self.bot.game.status == "nothing":
            return await ctx.send("現在ゲームはありません。")
        elif self.bot.game.status == "playing":
            return await ctx.send("現在ゲーム進行中です。")
        elif len(self.bot.game.players) == 2:
            return await ctx.send("参加できるメンバーが上限に達しています。")
        member = ctx.author
        for p in self.bot.game.players:
            if member.id == p.id:
                return await ctx.send("すでにゲームに参加しています。")
        player = Player(member.id)
        self.bot.game.players.append(player)
        await ctx.send(f"{member.mention}さんが参加しました。")

    @commands.command()
    async def leave(self, ctx):
        if self.bot.game.status == "nothing":
            return await ctx.send("現在ゲームはありません。")
        elif self.bot.game.status == "playing":
            return await ctx.send("既にゲームが始まっているため退出できません。")
        member = ctx.author
        for p in self.bot.game.players:
            if member.id == p.id:
                self.bot.game.players.remove(p)
                return await ctx.send("ゲームから退出しました。")
        return await ctx.send("ゲームに参加していません。")

    @commands.command()
    async def start(self, ctx):
        if self.bot.game is None:
            await ctx.send('まだ参加者を募集していません。')
            return
        if self.bot.game.status == 'playing':
            await ctx.send('既にゲーム中です。')
            return
        if len(self.bot.game.players) < 2:
            return await ctx.send("人数がゲーム開始人数に満たないため、ゲームを開始できません。")
        self.bot.game.status = 'playing'
        await ctx.send('ゲームを開始します。')
        n = len(self.bot.game.players)
        for i in range(n):
            player = self.bot.game.players[i]
            user = self.bot.get_user(player.id)

            def check(msg):
                return msg.author == user

            await user.send('重複なしの3桁の数字を入力してください。入力した数字があなたの数字となります。')
            while True:
                num = await self.bot.wait_for("message", check=check, timeout=None)
                user_num_tuple = game.make_tuple(num)
                player.set_num(user_num_tuple)

                if str.isdecimal(num.content) is not True:
                    """数字でないものが入力されたら処理を中断"""
                    await user.send('数字以外を入力することは出来ません。もう一度入力し直して下さい。')
                    continue

                elif game.check_duplication(user_num_tuple) is not True:
                    """数字が重複したら処理を中断"""
                    await user.send('数字を重複して入力することは出来ません。もう一度入力し直して下さい。')
                    continue

                else:
                    embed = discord.Embed(title='Numer0n(ヌメロン) | バトルモード',
                                          description=f'あなたの数字は、**{num.content}**です。',
                                          color=ctx.author.color)
                    await user.send(embed=embed)
                    break

    @commands.command()
    async def set_nothing(self, ctx):
        self.bot.game.status = 'nothing'
        await ctx.send(f'game.status を {self.bot.game.status} に変更しました。')

    @commands.command()
    async def set_playing(self, ctx):
        self.bot.game.status = 'playing'
        await ctx.send(f'game.status を {self.bot.game.status} に変更しました。')

    @commands.command()
    async def game_status(self, ctx):
        await ctx.send(f'現在の game.status は {self.bot.game.status} です。')


def setup(bot):
    bot.add_cog(Test(bot))