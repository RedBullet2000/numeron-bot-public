import random

from cogs.utils.player import Players


class Game:
    def __init__(self):
        self.status = 'nothing'
        self.stage = 'idle'
        self.players = Players()


class GamePlay:
    def __init__(self, num, target: tuple):
        self.num = num.content
        self.target = target
        self.tuple = self.convert()
        self.EAT = 0
        self.BITE = 0

    def convert(self):
        if self.is_decimal() is True:
            num_list = []
            for nums in self.num:
                num_list.append(int(nums))
            return tuple(num_list)

    def draw(self):
        if self.is_decimal() is not True:
            return False, "ValueError: is not decimal"
        elif self.check_duplication() is not True:
            return False, "ValueError: unexpected number"
        else:
            return True, self.check_num()

    def check_duplication(self):
        if len(self.tuple) == len(set(self.tuple)) and len(self.tuple) == 3:
            return True

    def is_decimal(self):
        if str.isdecimal(self.num) is True:
            return True

    def check_num(self):
        i = 0
        while i < 3:
            if self.tuple[i] == self.target[i]:
                self.EAT += 1
            elif self.tuple[i] in self.target:
                self.BITE += 1
            else:
                pass
            i += 1
        return f"{self.EAT}EAT, {self.BITE}BITE"


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
