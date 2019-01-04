import pygal

from die import Die

ilosc = int(input('Ile razy rzucić kościa?: '))

#Utworzenie kosci do gry
die_1 = Die()
die_2 = Die()

#Wykonanie rzutów i zapisanie na liste wyników
results = []
for roll_num in range(ilosc):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analiza wyników
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Wizualizacja wyników
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = 'Wynik rzucania dwiema kośćmi D6 ' + str(ilosc) + ' razy'
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = 'Wynik'
hist.y_title = 'Częstotliwość występowania wartości'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
