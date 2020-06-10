import json


class Player:
    def __init__(self, discord_id: int):
        self.id = discord_id
        self.num = ()
        self.UI = None

    def set_num(self, num: tuple):
        self.num = num
        return self


class Players(list):
    def get(self, player_id) -> Player:
        for p in self:
            if p.id == player_id:
                return p


def json_load() -> dict:
    """登録したプレイヤーデータを呼び出す"""
    with open('player.json', 'r') as f:
        player_dict = json.load(f)
        return player_dict


def json_write_id(value: str) -> bool:
    """jsonへのプレーヤーデータの登録"""
    with open('player.json', 'r') as f:
        player_dict = json.load(f)
        if len(player_dict) >= 2:
            """既にプレイヤーが2人登録されている場合はFalseを返す"""
            return False
        elif len(player_dict) == 1:
            if player_dict["1"][0] == value:
                """同じプレイヤーを登録しようとした場合はFalseを返す"""
                return False
            """2人目のプレイヤーをkey2として登録"""
            player_dict["2"] = [value, 0]
            with open('player.json', 'w') as f:
                json.dump(player_dict, f)
            return True
        """1人目のプレイヤーをkey1として登録"""
        player_dict["1"] = [value, 0]
        with open('player.json', 'w') as f:
            json.dump(player_dict, f)
        return True


def json_write_num(user: int, user_num: tuple):
    with open('player.json', 'r') as f:
        player_dict = json.load(f)
        player_dict[str(user)][1] = user_num
    with open('player.json', 'w') as f:
        json.dump(player_dict, f)


def json_remove():
    """登録したプレーヤーデータを全削除"""
    with open('player.json', 'r') as f:
        player_dict = json.load(f)
    player_dict.clear()
    with open('player.json', 'w') as f:
        json.dump(player_dict, f)


def json_data_num() -> int:
    """登録されているデータの数を返す"""
    with open('player.json', 'r') as f:
        player_dict = json.load(f)
        return len(player_dict)
