import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #przygotowanie danych błądzenia losowego i wyświetlanie punktów
    rw = RandomWalk(50000)
    rw.fill_walk()

    #Określenie wielkości okna wykresu
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=20) #Wyświetlenie punktu początkowego
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=20) #Wyświetlenie punktu końcowego

    #Ukrycie osi
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Utworzyć kolejne błądzenie losowe? (t/n): ')
    if keep_running.lower() == 'n':
        break
