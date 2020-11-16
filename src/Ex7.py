#!/usr/bin/env python3
#encoding: windows-1252

#Pida al usuario tres número que serán el día, mes y año. Comprueba que la fecha introducida es válida.  Por ejemplo: 
#32/01/2017->Fecha incorrecta
#29/02/2017->Fecha incorrecta
#30/09/2017->Fecha correcta.
import sys

if __name__ == "__main__":
    #declare the variables
    day = int(input("Insert the day: "))
    month = int(input("Insert the month: "))
    year = int(input("Insert the year: "))
    #if days are greater than 31 in the 31-days month, show incorrect
    if day > 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        print(day, '/', month, '/', year, "-> incorrect date")
    #if days are greater than 30 in the 30-days month, show incorrect
    elif day > 30 and (month == 4 or month == 6 or month == 9 or month == 11):
        print(day, '/', month, '/', year, "-> incorrect date")
    #if the days are greater than 28 in february
    elif day > 28 and month == 2:
        print(day, '/', month, '/', year, "-> incorrect date")
    #Other errors that could happen
    elif(day < 0 or month < 1 or month > 12):
        print(day, '/', month, '/', year, "-> incorrect date")
    #the date is correct, print is correct
    else:
        print(day, '/', month, '/', year, "-> correct date")
        

