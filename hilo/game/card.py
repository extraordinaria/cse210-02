import random

class Card:

    def __init__(self):
        self.value_card = 0
        self.value_card_2 = 0
        self.h_l_card = ""


    def show_card(self):
        self.value_card = random.randint(1,13) 
        self.value_card_2 = random.randint(1,13)

        while self.value_card_2 == self.value_card:
             self.value_card_2 = random.randint(1,13)

    def compare_card(self):
        if self.value_card_2 > self.value_card:
            self.h_l_card = "h"
        else:
            self.h_l_card = "l"
        

