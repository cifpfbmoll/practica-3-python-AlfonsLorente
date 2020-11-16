#!/usr/bin/env python3
#encoding: windows-1252

# Pida un número que como máximo tenga tres cifras (por ejemplo serían válidos 1, 99 i 213 pero no 1001). 
#Si el usuario introduce un número de más de tres cifras debe un informar con un mensaje de error como este: 
#“ERROR: El número 1005 tiene más de tres cifras”.

if __name__ == "__main__":
    #declare the variable
    num = int(input("Inser the desired integer: "))
    #is the number has more than 3 digits show an error
    if num >= 1000:
        print("ERROR: the number", num, "has more than 3 digits")
    else:
        print("Fine, your number", num, "seems correct")
