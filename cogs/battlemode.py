import discord
from discord.ext import commands

from cogs.utils import game
from cogs.utils import abillity


class Battlemode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.channel.purge(limit=1)
        generated_num_tuple = game.generate_num()
        double = abillity.double()
        high_and_low = abillity.high_and_low(generated_num_tuple)
        target = abillity.target(generated_num_tuple, 1)
        slash = abillity.slash(generated_num_tuple)
        contents = ''
        contents += f'Double: **{double}**\n'
        contents += f'High & Low: HIGH | **{high_and_low[0]}**, LOW | **{high_and_low[1]}**\n'
        contents += f'Target: EXIST(1) | **{str(target[0])}**, DIGIT | **{game.judgement_digit(target[1])}**\n'
        contents += f'Slash: **{slash}**\n'
        embed = discord.Embed(title='Numer0n(ヌメロン) | アビリティ検証',
                              description=f'Generated Number: {generated_num_tuple}',
                              color=ctx.author.color)
        embed.add_field(name='Abillity', value=contents)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Battlemode(bot))