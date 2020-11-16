#!/usr/bin/env python3
#encoding: windows-1252
import sys
#Pide al usuario que introduzca 3 calificaciones, y calcule la media de estas.
if __name__ == "__main__":
    #declare the variables and ask the marks
    mark1 = float(input("insert the first mark: "))
    #Break execution if the mark is greater than 10 or lower than 0 (same with the others)
    if mark1 > 10.0 or mark1 < 0.0:
        sys.exit("Note cant be greater than 10, or lower than 0")
    mark2 = float(input("insert the second mark: "))
    if mark2 > 10.0 or mark2 < 0.0:
        sys.exit("Note cant be greater than 10, or lower than 0")
    mark3 = float(input("insert the third mark: "))
    if mark3 > 10.0 or mark3 < 0.0:
        sys.exit("Note cant be greater than 10, or lower than 0")
    #Make the calculation of the meduim
    mediumMark = (mark1 + mark2 + mark3)/3
    #print the answer
    print("The medium mark is ", "%.2f" % mediumMark)
    