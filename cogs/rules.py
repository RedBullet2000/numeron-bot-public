from discord.ext import commands

from cogs.utils import views_rule as views


class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rules'])
    async def rule(self, ctx):
        await ctx.send(embed=views.embed_baserule(ctx))
        await ctx.send(embed=views.embed_abillity(ctx))


def setup(bot):
    bot.add_cog(Rules(bot))
