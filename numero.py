import random

NumAleatorio = int(random.random()*100)

while True:
    numero = int(input(f"Elige un numero entre el 1 al 100 para descubrir el numero magico: "))

    if numero<NumAleatorio:
        print(f"INCORRECTO, {numero} es menor al numero magico")

    elif numero>NumAleatorio:
        print(f"INCORRECTO, {numero} es mayor al numero magico")

    if numero==NumAleatorio:
        print(f"FELICIDADES, El numero {numero} es el mismo que el numero magico")
        break