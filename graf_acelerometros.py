from microbit import *

MAX = 10

def max (maximo,posibleMaximo):
    if maximo < posibleMaximo:
        maximo = posibleMaximo
    return maximo

def min (minimo,posibleMinimo):
    if minimo > posibleMinimo:
        minimo = posibleMinimo
    return minimo

def main():
        readings = [(0,0,0)] * MAX
        while True:
            valoresx = 0
            valoresy = 0
            valoresz = 0
            n = 1
            for i in range(MAX):
                x = accelerometer.get_x()
                y = accelerometer.get_y()
                z = accelerometer.get_z()
                tupla = (x,y,z)
                readings[i] = tupla
                valoresx += x
                valoresy += y
                valoresz += z
                mediax = valoresx / n
                mediay = valoresy / n
                mediaz = valoresz / n
                print((mediax,mediay,mediaz))
                sleep(100)
                n += 1
            if button_a.is_pressed():
                maximox = -2000
                maximoy = -2000
                maximoz = -2000
                for k in range(MAX):
                    maximox = max(maximox,(readings[k][0]))
                    maximoy = max(maximoy,(readings[k][1]))
                    maximoz = max(maximoz, (readings[k][2]))
                display.scroll(" "+str(maximox)+" " + str(maximoy)+ " " + str(maximoz))
            if button_b.is_pressed():
                minimox = 2000
                minimoy = 2000
                minimoz = 2000
                for k in range(MAX):
                    minimox= min(minimox,(readings[k][0]))
                    minimoy = min(minimoy,(readings[k][1]))
                    minimoz = min(minimoz, (readings[k][2]))
                display.scroll(" "+str(minimox)+" " + str(minimoy)+ " " + str(minimoz))


if __name__ == "__main__":
    main()
