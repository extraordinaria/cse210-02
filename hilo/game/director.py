from game.card import Card
class Director:
    '''
    The director of the HiLo game.
    '''
    def __init__(self):
        self.hilo = Card()
        self.current_value = self.hilo.value_card
        self.is_playing = True
        self.total_score = 300
        self.new_card_value = -1
        self.guess_card = ""

    def start_game(self):
        while self.is_playing:
            self.do_body_game()
            self.show_score()
            self.get_inputs()
            self.current_value = self.new_card_value
    
    def do_body_game(self):
        if not self.is_playing:
            return
        print (f"The card is: {self.current_value}")
        self.guess_card = input("Higher or lower? [h/l] ")
        while self.guess_card.lower() != "h" and self.guess_card.lower() != "l":
            self.guess_card = input("You have entered an incorrect answer: higher or lower? [h/l] ")
    
    def show_score(self):
        if not self.is_playing:
            return
        # While the cards are the same value, pick a new card instead
        the_same = True
        while the_same:
            self.next_card = Card()
            if self.next_card.value_card == self.current_value:
                the_same = True
            else:
                the_same = False
        
        print(f"Next card was: {self.next_card.value}")
        self.new_card_value = self.next_card.value_card
        if self.guess_card.lower() == 'h' and (self.current_value < self.new_card_value):
            self.total_score += 100
        elif self.guess_card.lower() == 'l' and (self.current_value > self.new_card_value):
            self.total_score += 100
        else:
            self.total_score -= 75
        print(f"Your score is {self.total_score}")

    def get_inputs(self):
        if self.total_score > 0:
            ask_player = input("Play again? [y/n] ")
            while ask_player.lower() != "y" and ask_player.lower() != "n":
                ask_player = input("You have entered an incorrect answer: Play again? [y/n] ")
            self.is_playing = (ask_player == "y")
            print()
        else:
            self.is_playing = False

        

    
        