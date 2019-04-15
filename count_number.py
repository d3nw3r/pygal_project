def counter(list):
    """функция подсчитывает количество каждого значения"""
    count_number = {'count1': 0, 'count2': 0, 'count3':0,
                    'count4': 0, 'count5': 0, 'count6': 0}
    for item in list:
        if item == 1:
            count_number['count1'] += 1
        elif item == 2:
            count_number['count2'] += 1
        elif item == 3:
            count_number['count3'] += 1
        elif item == 4:
            count_number['count4'] += 1
        elif item == 5:
            count_number['count5'] += 1
        else:
            count_number['count6'] += 1
    return count_number
