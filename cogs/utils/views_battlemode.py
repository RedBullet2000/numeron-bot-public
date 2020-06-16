import discord


def embed_gameend(ctx, user, result: dict, answer, winorlose):
    result_field = ''

    if winorlose == 'win':
        judge = 'You Win! :tada:'
    else:
        judge = 'You Lose! :sob:'

    embed = discord.Embed(title=judge,
                          description=f'**{user.name}**の勝利\n'
                                      f'相手の数字「**{answer}**」',
                          color=ctx.author.color)

    for key, value in result.items():
        result_field += f'{key}ターン目 | {value}\n'

    embed.add_field(name=f'{user.name}さんの対戦結果', value=result_field, inline=False)
    embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
    return embed


def embed_gameend_onecall(ctx, user, answer, winorlose):
    if winorlose == 'win':
        judge = 'You Win! :tada: 「**One Call :loudspeaker:**」'
    else:
        judge = 'You Lose! :sob: 「**One Call :loudspeaker:**」'

    embed = discord.Embed(title=judge,
                          description=f'**{user.name}**の勝利\n'
                                      f'相手の数字「**{answer}**」',
                          color=ctx.author.color)
    embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
    return embed


def embed_eatbite(ctx, i, num, eat, bite):
    embed = discord.Embed(title=f'{i}ターン目',
                          description=f'「**{num.content}**」 → **{eat}EAT, {bite}BITE**',
                          color=ctx.author.color)
    embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
    return embed


def embed_notification_selfnum_check(ctx, num):
    embed = discord.Embed(title=':bell:通知',
                          description=f'設定された数字は「**{num.content}**」です。これでよろしいですか?\n'
                                      f'設定を完了するには「:o:」、設定をやり直す場合は「:x:」のリアクションを押してください。',
                          color=ctx.author.color)
    embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
    return embed


def embed_notification_selfnum(ctx, num):
    embed = discord.Embed(title=':bell:通知',
                          description=f'あなたの数字は「**{num.content}**」です。',
                          color=ctx.author.color)
    embed.set_author(name='Numer0n(ヌメロン) - バトルモード')
    return embed


def embed_notification_turn(ctx, enemy):
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
