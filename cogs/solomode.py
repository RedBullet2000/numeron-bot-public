from discord.ext import commands

from cogs.utils import game
from cogs.utils import views_solomode as views


class Solomode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def solo(self, ctx):

        result = {}
        i = 0

        await ctx.channel.purge(limit=1)
        generated_num_tuple = game.generate_num()
        answer = ''.join(map(str, generated_num_tuple))
        UI = await ctx.send(embed=views.embed_start(ctx))

        def check_msg(msg):
            return msg.author == ctx.author

        while True:
            predicted_num = await self.bot.wait_for("message", check=check_msg, timeout=None)
            await ctx.channel.purge(limit=1)

            if predicted_num.content == 'end':
                """endと入力されたら処理を終了"""
                await ctx.send('ゲームを終了しました。')
                break

            if str.isdecimal(predicted_num.content) is not True:
                """数字でないものが入力されたら処理を中断"""
                await ctx.send('数字以外を入力することは出来ません。もう一度入力し直して下さい。')
                continue

            predicted_num_tuple = game.make_tuple(predicted_num)

            if game.check_duplication(predicted_num_tuple) is not True:
                """数字が重複したら処理を中断"""
                await ctx.send('数字を重複して入力することは出来ません。もう一度入力し直して下さい。')
                continue

            eat_bite = game.check_num(generated_num_tuple, predicted_num_tuple)
            i += 1
            result[i] = f'{predicted_num.content} → **{eat_bite[0]}EAT, {eat_bite[1]}BITE**'

            if eat_bite[0] == 3:
                """EATが3の時に処理を終了"""
                await UI.edit(embed=views.embed_gameclear(ctx, i, answer, result))
                break

            elif i >= 10:
                """10回試行したら処理を終了"""
                await UI.edit(embed=views.embed_gameover(ctx, answer))
                break

            await UI.edit(embed=views.embed_gameplay(ctx, i, predicted_num, eat_bite))


def setup(bot):
    bot.add_cog(Solomode(bot))
