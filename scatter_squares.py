import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Blues, edgecolor = 'none', s = 40)

#Zdefiniowanie tytułu wykresu i etykiety osi
plt.title('Kwadraty liczb', fontsize = 24)
plt.xlabel('Wartość', fontsize = 14)
plt.ylabel('Kwadraty wartości', fontsize = 14)

#zdefiniowanie zakresu dla każdej osi
plt.axis([0, 5100, 0, (y_values[-1])])

plt.savefig('squares_plot.png', bbox_inches = 'tight')
