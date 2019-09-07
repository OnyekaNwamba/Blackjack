import os
from tkinter import PhotoImage
assets_folder = os.getcwd() + "/assets"

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return " of ".join((self.value, self.suit))

    @classmethod
    def get_back_file(cls):
        cls.back = PhotoImage(file=assets_folder+"backs/Card-Back-03.png")
        return cls.back

    def get_file(self):
        return self.img
