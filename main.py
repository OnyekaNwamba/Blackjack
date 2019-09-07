from .Game import Game
from .Hand import Hand
from .Deck import Deck

class GameState:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)

        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

        self.has_winner = ''

if __name__ == "__main__":
    game = Game()
    game.play()
