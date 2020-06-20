class Player:
    def __init__(self, discord_id: int):
        self.id = discord_id
        self.num = ()
        self.times = 0
        self.results = {}
        self.answer = 0
        self.offensive_abillity = True
        self.defensive_abillity = True

    def set_num(self, num: tuple):
        self.num = num
        self.answer = ''.join(map(str, self.num))
        return self

    def add_times(self):
        self.times += 1
        return self

    def add_result(self, data):
        times = self.times
        self.results[times] = data
        return self


class Players(list):
    def get(self, player_id) -> Player:
        for p in self:
            if p.id == player_id:
                return p
