import pygal
from die import Die

#from count_number import counter

# создание кубика D6
die = Die()

# моделирование серии бросков с сохранением значений в списке
results = []
for roll_num in range(1000): # 100 раз бросаем кубик
    result = die.roll() # возвращает знаение кубика
    results.append(result)

    # анализ результатов
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequency = results.count(value) # подсчитываем количество каждого значения кубика в списке результатов
        frequencies.append(frequency)

# визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [item for item in range(1, die.num_sides+1)]
#hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Results'
hist.y_title = 'Frequency of results'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)

#print(counter(results))

