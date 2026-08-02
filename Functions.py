
def searchCard(name, cards):       
    for card in cards:
        if(card["card"].casefold() == name.casefold()) or (card["number"].casefold() == name.casefold()):
            return card["card"] + "(" + card["number"] + ")\nCondition: " + card["condition"] + "\nR$: " + str(card["price"]) + "\nLink: " + card["link"]
teste = ""      

