#!/usr/bin/env python3
#encoding: windows-1252

# Pida un n�mero que como m�ximo tenga tres cifras (por ejemplo ser�an v�lidos 1, 99 i 213 pero no 1001). 
#Si el usuario introduce un n�mero de m�s de tres cifras debe un informar con un mensaje de error como este: 
#�ERROR: El n�mero 1005 tiene m�s de tres cifras�.

if __name__ == "__main__":
    #declare the variable
    num = int(input("Inser the desired integer: "))
    #is the number has more than 3 digits show an error
    if num >= 1000:
        print("ERROR: the number", num, "has more than 3 digits")
    else:
        print("Fine, your number", num, "seems correct")
