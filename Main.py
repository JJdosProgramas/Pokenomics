import json 
import customtkinter
customtkinter.set_appearance_mode("dark")
with open("Cards.json", "r") as file:
    cards = json.load(file)["cards"]
from Functions import searchCard
teste = ""      

while teste != "q":
    teste = input("Type the card you want to check(press 'q' to quit): ")
    resultado = searchCard(teste, cards)
    print(resultado)


