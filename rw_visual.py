import matplotlib.pyplot as plt

from random_walk import RandomWalk

#przygotowanie danych błądzenia losowego i wyświetlanie punktów
rw = RandomWalk(500000)
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s = 5)
plt.show()
