# User story 1: som besökare, vill jag kunna lägga till en produkt i kundvagnen, så att jag kan köpa den.

# Acceptanskriterier:
# 1. det ska finnas en funktion för att lägga till en produkt i databasen: add_item(name, price)
# (ett mer realistikt exempel hade använt "id" istället

class ShoppingCart:
    def set_database(self, database):
        self.database = database

    def add_item(self, name, price):
        self.database.add_item_to_cart(name, price)

    pass
