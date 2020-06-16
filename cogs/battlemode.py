import discord
from discord.ext import commands

from cogs.utils.player import Player
from cogs.utils.game import Game
from cogs.utils import game
from cogs.utils import views_battlemode as views


class Battlemode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['make'])
    async def create(self, ctx):
        if self.bot.game.status == 'playing':
            await ctx.send('ゲーム中です。')
            return
        if self.bot.game.status == 'waiting':
            await ctx.send('既に参加者募集中です。')
            return
        self.bot.game.status = 'waiting'
        await ctx.send('参加者の募集を開始しました。')

    @commands.command(aliases=['enter'])
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

    @commands.command(aliases=['remove'])
    async def leave(self, ctx):
        if self.bot.game.status == "nothing":
            return await ctx.send("現在ゲームはありません。")
        elif self.bot.game.status == "playing":
            return await ctx.send("既にゲームが始まっているため退出できません。")
        member = ctx.author
        for p in self.bot.game.players:
            if member.id == p.id:
                self.bot.game.players.remove(p)
                return await ctx.send(f"{member.mention}さんがゲームから退出しました。")
        return await ctx.send("ゲームに参加していません。")

    @commands.command(aliases=['players'])
    async def player(self, ctx):
        player_fields = ''
        if self.bot.game.status == "nothing":
            return await ctx.send("現在ゲームはありません。")
        else:
            for i in range(len(self.bot.game.players)):
                player = self.bot.game.players[i]
                user = self.bot.get_user(player.id)
                player_fields += user.name + '\n'
            embed = discord.Embed(title=f':busts_in_silhouette: 現在参加中のプレイヤー | {len(self.bot.game.players)}/2',
                                  description=player_fields,
                                  color=ctx.author.color)
            embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
            await ctx.send(embed=embed)

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

        for i in range(len(self.bot.game.players)):
            player = self.bot.game.players[i]
            user = self.bot.get_user(player.id)

            def check_user(msg):
                return msg.author == user and msg.channel.type == discord.ChannelType.private

            await user.send('重複なしの3桁の数字を入力してください。入力した数字があなたの数字となります。')
            while True:
                num = await self.bot.wait_for("message", check=check_user, timeout=None)
                user_num_tuple = game.make_tuple(num)

                if str.isdecimal(num.content) is not True:
                    """数字でないものが入力されたら処理を中断"""
                    await user.send(embed=views.embed_notification_isnotnum(ctx))
                    continue

                elif game.check_duplication(user_num_tuple) is not True:
                    """数字が重複したら処理を中断"""
                    await user.send(embed=views.embed_notification_duplication(ctx))
                    continue

                else:
                    notice_num = await user.send(embed=views.embed_notification_selfnum_check(ctx, num))
                    await notice_num.add_reaction('⭕')
                    await notice_num.add_reaction('❌')
                    reaction, reaction_user = await self.bot.wait_for('reaction_add',
                                                                      check=lambda reaction, reaction_user: reaction_user.id == player.id)
                    if reaction.emoji == '⭕':
                        await user.send(embed=views.embed_notification_selfnum(ctx, num))
                        player.set_num(user_num_tuple)
                        break
                    elif reaction.emoji == '❌':
                        await user.send('もう一度重複なしの3桁の数字を入力してください。入力した数字があなたの数字となります。')
                        continue
                    else:
                        await user.send('無効なリアクションです。数字を入力し直してください。')
                        continue

        player_1 = self.bot.game.players[0]
        player_2 = self.bot.game.players[1]
        user_1 = self.bot.get_user(player_1.id)
        user_2 = self.bot.get_user(player_2.id)

        self.bot.game.stage = 'player1'

        def check_user_1(msg):
            return msg.author == user_1 and msg.channel.type == discord.ChannelType.private

        def check_user_2(msg):
            return msg.author == user_2 and msg.channel.type == discord.ChannelType.private

        while True:
            if self.bot.game.stage == 'gameend':
                """ゲームステージがgameendの時にゲームをリセットし、ループを抜ける"""
                self.bot.game = Game()
                break

            if self.bot.game.stage == 'player1':
                while True:
                    """player1の処理"""
                    await user_1.send(embed=views.embed_notification_turn(ctx, user_2))
                    num = await self.bot.wait_for("message", check=check_user_1, timeout=None)
                    user_1_predicted_num_tuple = game.make_tuple(num)

                    if str.isdecimal(num.content) is not True:
                        """数字でないものが入力されたら処理を中断"""
                        await user_1.send(embed=views.embed_notification_isnotnum(ctx))
                        continue

                    elif game.check_duplication(user_1_predicted_num_tuple) is not True:
                        """数字が重複したら処理を中断"""
                        await user_1.send(embed=views.embed_notification_duplication(ctx))
                        continue

                    else:
                        eat_bite = game.check_num(player_2.num, user_1_predicted_num_tuple)

                        if eat_bite[0] == 3:
                            """勝敗判定"""
                            if len(player_1.results) == 0 or len(player_2.results) == 0:
                                """One Call"""
                                await user_1.send(embed=views.embed_gameend_onecall(ctx, user_1, player_2.answer, 'win'))
                                await user_2.send(embed=views.embed_gameend_onecall(ctx, user_1, player_1.answer, 'lose'))
                            else:
                                await user_1.send(embed=views.embed_gameend(ctx, user_1, player_1.results, player_2.answer, 'win'))
                                await user_2.send(embed=views.embed_gameend(ctx, user_1, player_2.results, player_1.answer, 'lose'))
                            self.bot.game.stage = 'gameend'
                            break

                        player_1.add_times()
                        player_1.add_result(f'{num.content} → **{eat_bite[0]}EAT, {eat_bite[1]}BITE**')
                        await user_1.send(embed=views.embed_eatbite(ctx, player_1.times, num, eat_bite[0], eat_bite[1]))
                        self.bot.game.stage = 'player2'
                        break

            if self.bot.game.stage == 'player2':
                while True:
                    """player2の処理"""
                    await user_2.send(embed=views.embed_notification_turn(ctx, user_1))
                    num = await self.bot.wait_for("message", check=check_user_2, timeout=None)
                    user_2_predicted_num_tuple = game.make_tuple(num)

                    if str.isdecimal(num.content) is not True:
                        """数字でないものが入力されたら処理を中断"""
                        await user_2.send(embed=views.embed_notification_isnotnum(ctx))
                        continue

                    elif game.check_duplication(user_2_predicted_num_tuple) is not True:
                        """数字が重複したら処理を中断"""
                        await user_2.send(embed=views.embed_notification_duplication(ctx))
                        continue

                    else:
                        eat_bite = game.check_num(player_1.num, user_2_predicted_num_tuple)

                        if eat_bite[0] == 3:
                            """勝敗判定"""
                            if len(player_1.results) == 0 or len(player_2.results) == 0:
                                """One Call"""
                                await user_2.send(embed=views.embed_gameend_onecall(ctx, user_2, player_1.answer, 'win'))
                                await user_1.send(embed=views.embed_gameend_onecall(ctx, user_2, player_2.answer, 'lose'))
                            else:
                                await user_2.send(embed=views.embed_gameend(ctx, user_2, player_2.results, player_1.answer, 'win'))
                                await user_1.send(embed=views.embed_gameend(ctx, user_2, player_1.results, player_2.answer, 'lose'))
                            self.bot.game.stage = 'gameend'
                            break

                        player_2.add_times()
                        player_2.add_result(f'{num.content} → **{eat_bite[0]}EAT, {eat_bite[1]}BITE**')
                        await user_2.send(embed=views.embed_eatbite(ctx, player_2.times, num, eat_bite[0], eat_bite[1]))
                        self.bot.game.stage = 'player1'
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
    bot.add_cog(Battlemode(bot))