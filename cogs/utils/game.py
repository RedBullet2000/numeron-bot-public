import random

from cogs.utils.player import Player, Players


class Game:
    def __init__(self):
        self.status = 'nothing'
        self.channel = None
        self.players = Players()


def generate_num():
    """ランダムな3桁の数字をタプルに入れて生成"""
    while True:
        first_num = random.randint(0, 9)
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


def check_num(predicted_num, target_num):
    """位置が一致のときにEATに加算、数字が一致の時にBITEに加算"""
    EAT = 0
    BITE = 0
    i = 0
    while i < 3:
        if predicted_num[i] == target_num[i]:
            EAT += 1
        elif predicted_num[i] in target_num:
            BITE += 1
        else:
            pass
        i += 1
    return EAT, BITE


def make_tuple(num):
    """与えられた数字からタプルを作成"""
    num_list = []
    for nums in num.content:
        num_list.append(int(nums))
    return tuple(num_list)


def judgement_digit(index: int) -> str:
    """インデックスから桁を判定"""
    if index == 0:
        return '100'
    elif index == 1:
        return '10'
    elif index == 2:
        return '1'
    else:
        pass


def judgement_index(digit: str) -> int:
    """桁からインデックスを判定"""
    if digit == '100':
        return 0
    elif digit == '10':
        return 1
    elif digit == '1':
        return 2
    else:
        pass
