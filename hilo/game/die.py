import random

class Die:

    def __init__(self):
        self.value_card = 0


    def show_card(self):
        self.value_card = random.randint(1,13) 
