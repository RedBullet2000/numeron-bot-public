import discord
from discord.ext import commands

from cogs.utils import game


class Solomode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def solo(self, ctx):

        result = {}
        i = 0

        await ctx.channel.purge(limit=1)
        generated_num_tuple = game.generate_num()
        embed = discord.Embed(title='Numer0n(ヌメロン) | ソロモード',
                              description='3桁の数字を生成しました。10回以内に当ててください！\n三桁の数字を入力してください↓ ※但し、すべての桁が異なる数字である事。',
                              color=ctx.author.color)
        embed.set_footer(text='endと入力する事でゲームを中断します。')
        UI = await ctx.send(embed=embed)

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
                embed_result_field = ''
                times = 1

                answer = ''.join(map(str, generated_num_tuple))
                embed_result = discord.Embed(title='Numer0n(ヌメロン) | ソロモード',
                                             description=f'{i}回目でゲームクリア！ | 答え: **{answer}**',
                                             color=ctx.author.color)
                embed_result.set_footer(text=f"{ctx.author}'s result", icon_url=ctx.author.avatar_url)
                while True:
                    if times == len(result):
                        break
                    embed_result_field += f'{times}回目 | {result[times]}\n'
                    times += 1
                embed_result.add_field(name='対戦結果', value=embed_result_field, inline=False)
                await UI.edit(embed=embed_result)
                break

            elif i >= 10:
                """10回試行したら処理を終了"""
                answer = ''.join(map(str, generated_num_tuple))
                embed_gameover = discord.Embed(title='Numer0n(ヌメロン) | ソロモード',
                                               description=f'10回以内に当てることが出来なかった。ゲームオーバー！ | 答え: **{answer}**',
                                               color=ctx.author.color)
                embed_gameover.set_footer(text=f"{ctx.author}'s result", icon_url=ctx.author.avatar_url)
                await UI.edit(embed=embed_gameover)
                break

            embed = discord.Embed(title='Numer0n(ヌメロン) | ソロモード',
                                  description=f'{i}回目: {predicted_num.content} → **{eat_bite[0]}EAT, {eat_bite[1]}BITE**\n'
                                              f'三桁の数字を入力してください↓',
                                  color=ctx.author.color)
            embed.set_footer(text='endと入力する事でゲームを中断します。')
            await UI.edit(embed=embed)


def setup(bot):
    bot.add_cog(Solomode(bot))
