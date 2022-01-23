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
        while self.guess_card != "h" and self.guess_card != "l":
            self.guess_card = input("You have enter a correct answer: higher or lower? [h/l] ")
        


    def show_score(self):

        if not self.is_playing:
            return

        self.hilo.show_card()
        self.next_card = self.hilo.value_card_2
        while self.next_card == self.card_number:
            self.next_card = self.hilo.value_card_2
        print(f"Next card was: {self.next_card}")

        if self.card_number < self.next_card:
            h_l_card = "h"
        elif self.card_number > self.next_card:
            h_l_card = "l"

        if h_l_card == self.guess_card:
            self.score = 100
        else:
            self.score = -75
        self.total_score += self.score
        print(f"Your score is {self.total_score}")
        


    def get_inputs(self):

        if self.total_score > 0:
            ask_player = input("Play again? [y/n] ")
            while ask_player != "y" and ask_player != "n":
                ask_player = input("You have enter a correct answer: Play again? [y/n] ")
            self.is_playing = (ask_player == "y")
            print()

            if self.is_playing:
                self.card_number = self.next_card

        else:
            self.is_playing = False
            

        

    
        