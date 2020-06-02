import discord
from discord.ext import commands


class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rule(self, ctx):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title='Numer0n(ヌメロン) | ゲームルール',
                              description='互いに任意に作成した番号を先に当てた方が勝利',
                              color=ctx.author.color)
        embed.add_field(name='番号作成のルール',
                        value='0-9までのを使って、**重複無しの3桁の番号**を作成する。「550」「377」といった同じ数字を2つ以上使用した番号は作れない。',
                        inline=False)
        embed.add_field(name='EATとBYTEについて',
                        value='相手の数字を推理する際に数字と桁が合っていた場合は「**EAT**」（イート）、数字は合っているが桁は合っていない場合は「**BITE**」（バイト）が返される。',
                        inline=False)
        await ctx.author.send(embed=embed)


def setup(bot):
    bot.add_cog(Rules(bot))
