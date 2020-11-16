#Pida al usuario el espacio recorrido por un coche y el tiempo que ha tardado en horas y que calcule a qual velocidad media había realizado el recorrido.

if __name__ == "__main__":
    #declare and ask variables 
    distance = float(input("Insert the distance traveled in km: "))
    time = float(input("Insert the time ocurred in hores: "))
    #make the operation
    speed = distance/time
    #print the results
    print("The medium speed traveled is", speed, "Km/h")
