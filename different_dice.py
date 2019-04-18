import pygal
from die import Die

# создание двух кубиков D6
die_1 = Die()
die_2 = Die(10)

# моделирование серии бросков с сохранением значений в списке
results = []
for roll_num in range(50000): # 50000 раз бросаем кубик
    result = die_1.roll() + die_2.roll() # возвращает знаение кубика
    results.append(result)

# анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value) # подсчитываем количество каждого значения кубика в списке результатов
    frequencies.append(frequency)

# визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling D6 and D10 50000 times"
hist.x_labels = [item for item in range(2, max_result+1)]
hist.x_title = 'Results'
hist.y_title = 'Frequency of results'

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg')

print(frequencies)

#print(counter(results))

