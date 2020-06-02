import random

import discord
from discord.ext import commands


def generate_num():
    """ランダムな3桁の数字をタプルに入れて生成"""
    while True:
        first_num = random.randint(1, 9)
        second_num = random.randint(0, 9)
        third_num = random.randint(0, 9)
        num = (first_num, second_num, third_num)
        if check_duplication(num) is True:
            return num
        else:
            pass


def check_duplication(num):
    """すべての桁で数字が重複していないか判定"""
    if len(num) == len(set(num)) and len(num) == 3:
        return True


def check_num(est_num, gen_num):
    """位置が一致のときにEATに加算、数字が一致の時にBITEに加算"""
    EAT = 0
    BITE = 0
    i = 0
    while i < 3:
        if est_num[i] == gen_num[i]:
            EAT += 1
        elif est_num[i] in gen_num:
            BITE += 1
        else:
            pass
        i += 1
    return EAT, BITE


def make_list(est_num):
    """与えられた数字からリストを作成"""
    est_num_list = []
    for num in est_num.content:
        est_num_list.append(int(num))
    return est_num_list


class Solomode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def solo(self, ctx):
        await ctx.channel.purge(limit=1)
        gen_num_tuple = generate_num()
        embed = discord.Embed(title='Numer0n(ヌメロン) | ソロモード',
                              description='3桁の数字を生成しました。10回以内に当ててください！\n三桁の数字を入力してください↓ ※但し、すべての桁が異なる数字である事。',
                              color=ctx.author.color)
        embed.set_footer(text='endと入力する事でゲームを中断します。')
        UI = await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author

        result = {}
        i = 0
        while True:
            est_num = await self.bot.wait_for("message", check=check, timeout=None)
            await ctx.channel.purge(limit=1)

            if est_num.content == 'end':
                await ctx.send('ゲームを中断しました。')
                break

            est_num_list = make_list(est_num)

            if check_duplication(est_num_list) is not True:
                await ctx.send('数字を重複して入力することは出来ません。もう一度入力し直して下さい。')
                continue

            eat_byte = check_num(gen_num_tuple, est_num_list)
            i += 1
            result[i] = f'{est_num.content} | **{eat_byte[0]}EAT, {eat_byte[1]}BITE**'

            if eat_byte[0] == 3:
                answer = ''.join(map(str, gen_num_tuple))
                embed_result = discord.Embed(title='Numer0n(ヌメロン) | ソロモード',
                                             description=f'{i}回目でゲームクリア！ | 答え: **{answer}**',
                                             color=ctx.author.color)
                embed_result.set_footer(text=f"{ctx.author}'s result", icon_url=ctx.author.avatar_url)
                times = 1
                while True:
                    if times == len(result):
                        break
                    embed_result.add_field(name=f'{times}回目', value=result[times], inline=False)
                    times += 1
                await UI.edit(embed=embed_result)
                break

            elif i >= 10:
                answer = ''.join(map(str, gen_num_tuple))
                embed_gameover = discord.Embed(title='Numer0n(ヌメロン) | ソロモード',
                                               description=f'10回以内に当てることが出来なかった。ゲームオーバー！ | 答え: **{answer}**',
                                               color=ctx.author.color)
                embed_gameover.set_footer(text=f"{ctx.author}'s result", icon_url=ctx.author.avatar_url)
                await UI.edit(embed=embed_gameover)
                break

            embed = discord.Embed(title='Numer0n(ヌメロン) | ソロモード',
                                  description=f'{i}回目: {est_num.content} | **{eat_byte[0]}EAT, {eat_byte[1]}BITE**\n'
                                              f'三桁の数字を入力してください↓',
                                  color=ctx.author.color)
            embed.set_footer(text='endと入力する事でゲームを中断します。')
            await UI.edit(embed=embed)


def setup(bot):
    bot.add_cog(Solomode(bot))
