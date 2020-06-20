from discord.ext import commands

from cogs.utils import game
from cogs.utils.game import GamePlay
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
            display = GamePlay(predicted_num, generated_num_tuple)
            draw = display.draw()

            if predicted_num.content == 'end':
                """endと入力されたら処理を終了"""
                await ctx.send('ゲームを終了しました。')
                break

            if draw[0] is not True:
                await ctx.send(draw[1])
                continue

            eat_bite = draw[1]
            result[i] = f'{display.num} → **{eat_bite}**'

            if display.EAT == 3:
                """EATが3の時に処理を終了"""
                await UI.edit(embed=views.embed_gameclear(ctx, i, answer, result))
                break

            if i >= 10:
                """10回試行したら処理を終了"""
                await UI.edit(embed=views.embed_gameover(ctx, answer))
                break

            await UI.edit(embed=views.embed_gameplay(ctx, i, display.num, eat_bite))
            i += 1


def setup(bot):
    bot.add_cog(Solomode(bot))
