from cogs.utils import game


def double():
    """アビリティ（攻撃）｜ダブル"""
    pass


def high_and_low(target_num: tuple):
    """アビリティ（攻撃）｜ハイアンドロー"""
    HIGH = 0
    LOW = 0
    high = (5, 6, 7, 8, 9)
    low = (0, 1, 2, 3, 4)
    i = 0
    while i < 5:
        if high[i] in target_num:
            HIGH += 1
        if low[i] in target_num:
            LOW += 1
        i += 1
    return HIGH, LOW


def target(target_num: tuple, num: int):
    """アビリティ（攻撃）｜ターゲット"""
    if num in target_num:
        return True, target_num.index(num)
    else:
        return False, '---'


def slash(target_num: tuple):
    """アビリティ（攻撃）｜スラッシュ"""
    value = max(target_num) - min(target_num)
    return value


def shuffle(before_num: tuple, after_num: tuple) -> bool:
    """アビリティ（防御）｜シャッフル"""
    if len(list(set(before_num)) and set(after_num)) == 3:
        return True


def change(before_num: tuple, digit: str, num: int):
    """アビリティ（防御）｜チェンジ"""
    index = game.judgement_index(digit)
    before_num_list = list(before_num)
    before_num_list[index] = num
    after_num = tuple(before_num_list)
    if game.check_duplication(after_num) is not True:
        return False
    elif before_num == after_num:
        return False
    else:
        return after_num
