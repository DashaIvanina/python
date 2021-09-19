for i in range(1,101):
    if i % 10 == 0 or i / 11 == 1 or i / 12 == 1 or i / 13 == 1 or i / 14 == 1 or i % 10 == 5 or i % 10 == 6 or i % 10 == 7 or i % 10 == 8 or i % 10 == 9:
        print(i, 'Процентов')
    if i % 10 == 1 and i != 11:
        print(i, 'Процент')
    if (i > 12 and i % 10 == 2) or (i > 13 and i % 10 == 3) or (i > 14 and i % 10 == 4) or i == 2 or i == 3 or i == 4:
        print(i, 'Процента')
