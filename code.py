# lets estimate pi generating random numbers in a x/y axis with x and y 0 <= x/y <= 1
# El area del circulo (de ahi sacamos pi) y el area del cuadrado serán aproximados por los puntos x/y dentro y fuera del circulo.

#definimos la funcion estimar pi con un argumento n que indicará el numero de puntos a dibujar.
# github working

import random;

def estimate_pi(n):
    num_points_circle = 0
    num_points_total = 1
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)

        distance = x**2 + y**2

        if distance <= 1:
            num_points_circle += 1
        num_points_total += 1

    return 4 * num_points_circle / num_points_total

