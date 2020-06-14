import discord


def embed_gameend(ctx, user, result: dict, answer, winorlose):
    judge = ''
    result_field = ''
    times = 1

    if winorlose == 'win':
        judge = 'You Win! :tada:'
    elif winorlose == 'lose':
        judge = 'You Lose! :sob:'

    embed = discord.Embed(title=judge,
                          description=f'**{user.name}**の勝利\n'
                                      f'相手の数字「**{answer}**」',
                          color=ctx.author.color)
    while True:
        if times == len(result):
            break
        result_field += f'{times}回目 | {result[times]}\n'
        times += 1
    embed.add_field(name=f'{user.name}さんの対戦結果', value=result_field, inline=False)
    embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
    return embed


def embed_eatbite(ctx, i, num, eat, bite):
    embed = discord.Embed(title=f'{i}回目',
                          description=f'「**{num.content}**」 → **{eat}EAT, {bite}BITE**',
                          color=ctx.author.color)
    embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
    return embed


def embed_notification(ctx, enemy):
    embed = discord.Embed(title=':bell:通知',
                          description=f'あなたの番です。{enemy.name}さんの3桁の数字を当ててください。',
                          color=ctx.author.color)
    embed.set_footer(text='三桁の数字を入力してください↓')
    embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
    return embed


def embed_notification_duplication(ctx):
    embed = discord.Embed(title=':bell:通知',
                          description=f'数字を重複して入力することは出来ません。もう一度入力し直して下さい。',
                          color=ctx.author.color)
    embed.set_footer(text='三桁の数字を入力してください↓')
    embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
    return embed


def embed_notification_isnotnum(ctx):
    embed = discord.Embed(title=':bell:通知',
                          description=f'数字以外を入力することは出来ません。もう一度入力し直して下さい。',
                          color=ctx.author.color)
    embed.set_footer(text='三桁の数字を入力してください↓')
    embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
    return embed
