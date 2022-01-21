from game.die import Die

class director:


    def __init__(self):

        self.hilo = Die()
        self.is_playing = True
        self.score = 300
        self.total_score = 0

    def start_game(self):

        while self.is_playing:

            self.do_body_game()
            self.show_score()
            self.get_inputs()

    def do_body_game(self):

        if not self.is_playing:
            return

        card = self.hilo.show_card
        print (f"The card is: {card}")

        guess_card = input("Higher or lower? [h/l] ")
        


    def show_score(self):

        if not self.is_playing:
            return

        next_card = self.hilo.show_card

    def get_inputs(self):

        ask_player = input("Play again? [y/n] ")
        self.is_playing = (ask_player == "y")
        print()

        if self.is_playing:
            card = self.hilo.show_card
            print (f"The card is: {card}")

    
        