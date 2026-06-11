
from src.core.game import Game

game = Game()
    
game.start_game()

while True:
    game.next_question()
    game.load_question()

    if game.process_answer(1):
        if game.end_game():
            print("parabens vc ganhou!")
            break
    else:
        print("vc perdeu")
        break

print("fim do jogo")