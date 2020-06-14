import discord


def embed_baserule(ctx):
    embed = discord.Embed(title=':scroll: 基本ルール',
                          description='互いに任意に作成した番号を先に当てた方が勝利',
                          color=ctx.author.color)
    embed.set_author(name='Numer0n(ヌメロン) - ゲームルール')
    embed.add_field(name=':pushpin: 番号作成のルール',
                    value='0-9までのを使って、**重複無しの3桁の番号**を作成する。「550」「377」といった同じ数字を2つ以上使用した番号は作れない。',
                    inline=False)
    embed.add_field(name=':pushpin: EATとBYTEについて',
                    value='相手の数字を推理する際に数字と桁が合っていた場合は「**EAT**」（イート）、数字は合っているが桁は合っていない場合は「**BITE**」（バイト）が返される。',
                    inline=False)
    embed.add_field(name=':link: Numer0n - ウィキペディア',
                    value='[Wikipedia](https://ja.wikipedia.org/wiki/Numer0n)')
    embed.add_field(name=':link: Numer0n - フジテレビ',
                    value='[番組公式サイト](https://www.fujitv.co.jp/b_hp/numer0n/)')
    return embed


def embed_abillity(ctx):
    embed = discord.Embed(title=':scroll: 各種アビリティ',
                          description='ゲーム内で使用できるアビリティについて\n'
                                      '※ソロモードでは使用不可',
                          color=ctx.author.color)
    embed.add_field(name=':crossed_swords: アビリティ（攻撃）',
                    value='\n\n**・:yellow_square: DOUBLE(ダブル)**\n'
                          '自分のターンに2連続で相手の番号をコールできる。ただし、代償として自分の番号を1つ開示しなければならず、しかもどの桁を開示するかは相手に指定される。\n'
                          '※使用した回を含めた2回のコールで1ターンとみなすため、2回目のコール時は双方ともアイテムを使用できない。'
                          '\n\n**・:blue_square: HIGH&LOW(ハイアンドロー)**\n'
                          '相手の全ての桁の数字が、それぞれ「HIGH (5-9)」「LOW (0-4)」のどちらかを知ることができる。'
                          '\n\n**・:purple_square: TARGET(ターゲット)**\n'
                          '10種類の番号のうち1'
                          'つを指定して、相手にその数字を使用しているか否かを訊くことができる。その番号が相手の組み合わせに含まれている場合は、どの桁に入っているかも判明する。 '
                          '\n\n**・:green_square: SLASH(スラッシュ)**\n'
                          '相手が使っているナンバーの最大数から最小数を引いた「スラッシュナンバー」を訊くことができる。',
                    inline=False)
    embed.add_field(name=':shield: アビリティ（防御）',
                    value='\n\n**・:green_circle: SHUFFLE(シャッフル)**\n'
                          '自分が設定した番号カードを並べ替えて、新たな番号にすることができる。並べ替えたと見せかけてそのままにするフェイントも可能。'
                          '\n\n**・:red_circle: CHANGE(チェンジ)**\n'
                          '自分のナンバーの中から1つを選択し、その番号を手持ちのカードの中から交換できる。ただし、桁の位置と、それがHIGH・LOW'
                          'のどちらなのかを宣言する必要がある。交換する番号はLOWナンバー同士・HIGHナンバー同士に限定される。\n'
                          '※必ず他の番号と交換する必要あり。',
                    inline=False)
    return embed
