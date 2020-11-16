#!/usr/bin/env python3
#encoding: windows-1252

#Pida al usuario el precio de un producto y el nombre del producto y muestre el mensaje con el precio del IVA (21%).
#Por ejemplo: “Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 euros en total”.

if __name__ == "__main__":
    #declare the variable and its value.
    item = str(input("insert an item: "))
    price = float(input("insert its price: "))
    #calcule the variable
    total = price * 1.21
    #print the answer
    print("your", item, "costs", "%.2f" % price, "€ and with the 21% IVA the price is", "%.2f" %  total, "€")