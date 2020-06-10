import discord
from discord.ext import commands

from cogs.utils import game
from cogs.utils import abillity
from cogs.utils import player


class Battlemode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def test(self, ctx):
    #     await ctx.channel.purge(limit=1)
    #     self.bot.game.status = 'playing'
    #     generated_num_tuple = game.generate_num()
    #     double = abillity.double()
    #     high_and_low = abillity.high_and_low(generated_num_tuple)
    #     target = abillity.target(generated_num_tuple, 1)
    #     slash = abillity.slash(generated_num_tuple)
    #     contents = ''
    #     contents += f'Double: **{double}**\n'
    #     contents += f'High & Low: HIGH | **{high_and_low[0]}**, LOW | **{high_and_low[1]}**\n'
    #     contents += f'Target: EXIST(1) | **{str(target[0])}**, DIGIT | **{game.judgement_digit(target[1])}**\n'
    #     contents += f'Slash: **{slash}**\n'
    #     embed = discord.Embed(title='Numer0n(ヌメロン) | アビリティ検証',
    #                           description=f'Generated Number: {generated_num_tuple}',
    #                           color=ctx.author.color)
    #     embed.add_field(name='Abillity', value=contents)
    #     await ctx.send(embed=embed)
    #
    # @commands.command()
    # async def join(self, ctx):
    #     await ctx.channel.purge(limit=1)
    #     if player.json_write_id(ctx.author.id) is not True:
    #         await ctx.send('プレイヤーの登録に失敗しました。')
    #         return
    #     await ctx.send(f'{ctx.author.nick or ctx.author.name}をプレイヤーとして登録しました。')
    #     user_list = []
    #     for user_data in player.json_load().values():
    #         user = self.bot.get_user(user_data[0])
    #         user_list.append(user.name)
    #     users = '\n'.join(user_list)
    #     await ctx.send(f'現在参加中のメンバー: \n{users}')
    #
    # @commands.command()
    # async def stop(self, ctx):
    #     await ctx.channel.purge(limit=1)
    #     if self.bot.game.status == 'playing':
    #         await ctx.send('ゲームが進行中につき、プレイヤーデータを変更することはできません。')
    #
    #     else:
    #         player.json_remove()
    #         await ctx.send('ゲームを終了し、プレーヤーデータをリセットしました。')
    #
    # @commands.command()
    # async def start(self, ctx):
    #     await ctx.channel.purge(limit=1)
    #
    #     if player.json_data_num() <= 1:
    #         await ctx.send('ゲーム開始には、2人のプレーヤーを登録する必要があります。\n「n/join」コマンドによりプレイヤーを登録することが出来ます。')
    #
    #     elif player.json_data_num() == 2:
    #         self.bot.game.status = 'playing'
    #         user_1 = self.bot.get_user(player.json_load()["1"][0])
    #         user_2 = self.bot.get_user(player.json_load()["2"][0])
    #         await ctx.send('ゲームを開始します。')
    #
    #         def check_user_1(msg):
    #             return msg.author == user_1
    #
    #         def check_user_2(msg):
    #             return msg.author == user_2
    #
    #         await user_1.send('重複なしの3桁の数字を入力してください。入力した数字があなたの数字となります。')
    #
    #         while True:
    #             num_user_1 = await self.bot.wait_for("message", check=check_user_1, timeout=None)
    #             await user_1.purge(limit=1)
    #             user_1_num_tuple = game.make_tuple(num_user_1)
    #             player.json_write_num(1, user_1_num_tuple)
    #
    #             if str.isdecimal(num_user_1.content) is not True:
    #                 """数字でないものが入力されたら処理を中断"""
    #                 await ctx.send('数字以外を入力することは出来ません。もう一度入力し直して下さい。')
    #                 continue
    #
    #             elif game.check_duplication(user_1_num_tuple) is not True:
    #                 """数字が重複したら処理を中断"""
    #                 await ctx.send('数字を重複して入力することは出来ません。もう一度入力し直して下さい。')
    #                 continue
    #
    #             else:
    #                 embed = discord.Embed(title='Numer0n(ヌメロン) | バトルモード',
    #                                       description=f'あなたの数字は、**{num_user_1.content}**です。',
    #                                       color=ctx.author.color)
    #                 UI_1 = await ctx.send(embed=embed)
    #                 break
    #
    #         await user_2.send('重複なしの3桁の数字を入力してください。入力した数字があなたの数字となります。')
    #
    #         while True:
    #             num_user_2 = await self.bot.wait_for("message", check=check_user_2, timeout=None)
    #             await user_2.purge(limit=1)
    #             player.json_write_num(2, game.make_tuple(num_user_2))
    #
    #             if str.isdecimal(num_user_1.content) is not True:
    #                 """数字でないものが入力されたら処理を中断"""
    #                 await ctx.send('数字以外を入力することは出来ません。もう一度入力し直して下さい。')
    #                 continue
    #
    #             elif game.check_duplication(user_1_num_tuple) is not True:
    #                 """数字が重複したら処理を中断"""
    #                 await ctx.send('数字を重複して入力することは出来ません。もう一度入力し直して下さい。')
    #                 continue
    #
    #             else:
    #                 embed = discord.Embed(title='Numer0n(ヌメロン) | バトルモード',
    #                                       description=f'あなたの数字は、**{num_user_2.content}**です。',
    #                                       color=ctx.author.color)
    #                 UI_2 = await ctx.send(embed=embed)
    #                 break
    #
    #     else:
    #         pass
    #
    # @commands.command()
    # async def set_nothing(self, ctx):
    #     self.bot.game.status = 'nothing'
    #     await ctx.send(f'game.status を {self.bot.game.status} に変更しました。')
    #
    # @commands.command()
    # async def set_playing(self, ctx):
    #     self.bot.game.status = 'playing'
    #     await ctx.send(f'game.status を {self.bot.game.status} に変更しました。')
    #
    # @commands.command()
    # async def game_status(self, ctx):
    #     await ctx.send(f'現在の game.status は {self.bot.game.status} です。')


def setup(bot):
    bot.add_cog(Battlemode(bot))