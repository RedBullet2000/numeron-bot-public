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
