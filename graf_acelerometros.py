from microbit import *

MAX = 10

def max (numero1,numero2):
    """
        Esta funcion devuelve el valor maximo entre dos dados.
        @param numero1: primer numero que se quiere saber si es mayor que el otro.
        @param numero2 : segundo numero que se quiere saber si es mayor que el otro.
    """
    if numero1 < numero2:
        numero1 = numero2
    return numero1

def min (numero1,numero2):
    """
        Esta funcion devuelve el valor minimo entre dos dados.
        @param numero1: primer numero que se quiere saber si es menor que el otro.
        @param numero2 : segundo numero que se quiere saber si es menor que el otro.
    """
    if numero1 > numero2:
        numero1 = numero2
    return numero1

def mostrarCoordenadasMaximas(lista):
    """
        Esta funcion muestra en el display del microbit, los valores maximos de cada eje de los almacenados en la lista.
        @param lista: lista de tuplas, las cuales son de tres posiciones, que contiene los valores de cada eje.
    """
    # Inicializamos valores de maximo a un valor muy bajo para que siempre se sustituya con el primero
    maximox = -2000
    maximoy = -2000
    maximoz = -2000
    # Recorremos la lista para encontrar el maximo valor de cada eje
    for i in range(MAX):
        maximox = max(maximox,(lista[i][0]))
        maximoy = max(maximoy,(lista[i][1]))
        maximoz = max(maximoz, (lista[i][2]))
    display.scroll(" "+str(maximox)+" " + str(maximoy)+ " " + str(maximoz))

def mostrarCoordenadasMinimas(lista):

    """
        Esta funcion muestra en el display del microbit, los valores minimos de cada eje de los almacenados en la lista.
        @param lista: lista de tuplas, las cuales son de tres posiciones, que contiene los valores de cada eje.
    """
    # Inicializamos valores de minimo a un valor muy alto para que siempre se sustituya con el primero
    minimox = 2000
    minimoy = 2000
    minimoz = 2000
 # Recorremos la lista para encontrar el maximo valor de cada eje
    for i in range(MAX):
        minimox= min(minimox,(lista[i][0]))
        minimoy = min(minimoy,(lista[i][1]))
        minimoz = min(minimoz, (lista[i][2]))
    display.scroll(" "+str(minimox)+" " + str(minimoy)+ " " + str(minimoz))

def main():
        # Inicializamos la lista con 10 tuplas cuyas valores son (0,0,0)
        readings = [(0,0,0)] * MAX

        while True:
            # Inicializamos los valores de cada eje
            valoresx = 0
            valoresy = 0
            valoresz = 0
            # Inicializamos un contador para contar las veces que se pasa por el bucle
            contador = 1

            for i in range(MAX):
                # Obtenemos posiciones x,y,z del acelerometro
                x = accelerometer.get_x()
                y = accelerometer.get_y()
                z = accelerometer.get_z()
                # Las guardamos en una tupla y almacenamos la tupla en la posicion adecuada de la lista
                tupla = (x,y,z)
                readings[i] = tupla
                # Acumulamos el valor de cada eje para poder hacer la media
                valoresx += x
                valoresy += y
                valoresz += z
                # Hacemos la media
                mediax = valoresx / contador
                mediay = valoresy / contador
                mediaz = valoresz / contador
                # Mostramos la media de cada eje y paramos la ejecucion 100 ms
                print((mediax,mediay,mediaz))
                sleep(100)
                # Aumentamos el contador
                contador += 1

                if button_a.is_pressed():
                    mostrarCoordenadasMaximas(readings)

                if button_b.is_pressed():
                    mostrarCoordenadasMinimas(readings)


if __name__ == "__main__":
    main()
