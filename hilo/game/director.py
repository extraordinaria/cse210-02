from game.card import Card

class Director:


    def __init__(self):

        self.hilo = Card()
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.guess_card = ""
        self.hilo.show_card()
        self.card_number = self.hilo.value_card

    def start_game(self):

        while self.is_playing:

            self.do_body_game()
            self.show_score()
            self.get_inputs()

    def do_body_game(self):

        if not self.is_playing:
            return

        
        self.hilo.show_card()  
        print (f"The card is: {self.card_number}")

        self.guess_card = input("Higher or lower? [h/l] ")
        


    def show_score(self):

        if not self.is_playing:
            return

        self.hilo.show_card()
        self.hilo.compare_card()
        self.next_card = self.hilo.value_card_2
        print(f"Next card was: {self.next_card}")

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
            self.card_number = self.next_card

        else:
            return

    
        