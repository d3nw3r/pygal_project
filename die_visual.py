from die import Die
from count_number import counter

# создание кубика D6
die = Die()

# моделирование серии бросков с сохранением значений в списке
results = []
for roll_num in range(100): # 100 раз бросаем кубик
    result = die.roll() # возвращает знаение кубика
    results.append(result)

print(results)

print(counter(results))

