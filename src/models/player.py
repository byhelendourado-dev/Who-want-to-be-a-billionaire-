"""Player class."""

class Player:

    def __init__(self):
        self.current_score = 0
        self.prize_ammount = 0
        self.progress = 0
        self.lifeline_usage = 3

    def update_score(self):
        pass

    def advance_level(self):
        pass

    def use_lifeline(self):
        if self.lifeline_usage > 0:
            self.lifeline_usage -= 1
            return True

        return False

jogador = Player()
print(jogador.use_lifeline())
print(jogador.use_lifeline())
print(jogador.use_lifeline())
print(jogador.use_lifeline())
print(jogador.use_lifeline())
print(jogador.use_lifeline())
print(jogador.use_lifeline())

jogador2 = Player()
print(jogador2.use_lifeline())