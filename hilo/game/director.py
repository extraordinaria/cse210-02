from game.card import Card

class Director:


    def __init__(self):

        self.hilo = Card()
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.guess_card = ""
        self.card = 0

    def start_game(self):

        while self.is_playing:

            self.do_body_game()
            self.show_score()
            self.get_inputs()

    def do_body_game(self):

        if not self.is_playing:
            return

        self.card = self.hilo.value_card
        print (f"The card is: {self.card}")

        self.guess_card = input("Higher or lower? [h/l] ")
        


    def show_score(self):

        if not self.is_playing:
            return

        next_card = self.hilo.value_card_2
        print(f"Next card was: {next_card}")

        if self.hilo.h_l_card == self.guess_card:
            self.score = 100
        else:
            self.score = -75
        self.total_score += self.score
        print(f"Your score is {self.total_score}")


    def get_inputs(self):

        if self.total_score > 0:
            ask_player = input("Play again? [y/n] ")
            self.is_playing = (ask_player == "y")
            print()

        else:
            return

    
        