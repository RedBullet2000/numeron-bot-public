import discord


def embed_start(ctx):
    embed = discord.Embed(title=':bell:通知',
                          description='3桁の数字を生成しました。10回以内に当ててください！\n三桁の数字を入力してください↓ ※但し、すべての桁が異なる数字である事。',
                          color=ctx.author.color)
    embed.set_footer(text='endと入力する事でゲームを中断します。')
    embed.set_author(name='Numer0n(ヌメロン) - ソロモード')
    return embed


def embed_gameplay(ctx, i, predicted_num, eat_bite):
    embed = discord.Embed(title=f'{i}回目',
                          description=f'「**{predicted_num.content}**」 → **{eat_bite[0]}EAT, {eat_bite[1]}BITE**\n'
                                      f'三桁の数字を入力してください↓',
                          color=ctx.author.color)
    embed.set_footer(text='endと入力する事でゲームを中断します。')
    embed.set_author(name='Numer0n(ヌメロン) - ソロモード')
    return embed


def embed_gameclear(ctx, i, answer, result: dict):
    embed_result_field = ''
    times = 1

    embed = discord.Embed(title='You Win! :tada:',
                          description=f'{i}回目でゲームクリア！\n'
                                      f'BOTの数字「**{answer}**」',
                          color=ctx.author.color)
    embed.set_footer(text=f"{ctx.author}'s result", icon_url=ctx.author.avatar_url)
    while True:
        if times == len(result):
            break
        embed_result_field += f'{times}回目 | {result[times]}\n'
        times += 1
    embed.add_field(name='対戦結果', value=embed_result_field, inline=False)
    embed.set_author(name='Numer0n(ヌメロン) - ソロモード')
    return embed


def embed_gameover(ctx, answer):
    embed = discord.Embed(title='You Lose! :sob:',
                          description=f'10回以内に当てることが出来なかった。ゲームオーバー！\n'
                                      f'BOTの数字「**{answer}**」',
                          color=ctx.author.color)
    embed.set_footer(text=f"{ctx.author}'s result", icon_url=ctx.author.avatar_url)
    embed.set_author(name='Numer0n(ヌメロン) - ソロモード')
    return embed


def embed_notification_duplication(ctx):
    embed = discord.Embed(title=f':bell:通知',
                          description=f'数字を重複して入力することは出来ません。もう一度入力し直して下さい。',
                          color=ctx.author.color)
    embed.set_author(name='Numer0n(ヌメロン) - ソロモード')
    return embed


def embed_notification_isnotnum(ctx):
    embed = discord.Embed(title=f':bell:通知',
                          description=f'数字以外を入力することは出来ません。もう一度入力し直して下さい。',
                          color=ctx.author.color)
    embed.set_author(name='Numer0n(ヌメロン) - ソロモード')
    return embed
