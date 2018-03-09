from random import *
import os

class Dealer:
    def deal_a_card(self):
        random_number = randrange(1, 13)
        return random_number

dealer = Dealer()

class Player:
    def __init__(self, cards_in_hand=[]):
        self.cards_in_hand = cards_in_hand

    def answer(self):
        choice = input("Press y for yes or n for no\t")
        if choice=="y":
            card = dealer.deal_a_card()
            print(f"Dealt card is: {card}")
            self.cards_in_hand.append(card)
        else:
            print("No card dealt this round")
        print(f"Cards in hand: {self.cards_in_hand}")

    def checkSum(self):
        summation = sum((self.cards_in_hand))
        print(f"Total sum of cards is : {summation}")
        if summation > 21:
            print("BUST!!!")
            return "n"
        else:
            return "y"

def main():
    os.system('clear')
    print("Welcome to terminal blackjack!")
    choice=input("Start playing ? y/n\t")
    player = Player()
    print("Let's begin - deal ?")
    while choice=="y":
        game=player.checkSum()
        if game=="y":
            player.answer()
            print("deal ?")
        else:
            break

main()
