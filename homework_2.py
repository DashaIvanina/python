#1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

#2
names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in names:
    new_names = el.split()
    greeting = 'Привет, {}!'.format(new_names[-1].title())
    print(greeting)

#3
count = [57.8, 46.51, 97, 101.55, 45, 88.88, 8800.1]
print(id(count))

for el in sorted(count):
    new_count = str(el).split('.')
    result = f'{new_count[0]} руб {int(new_count[-1]):02d} коп'
    print(result)

back_count = sorted(count, reverse=True)
print(back_count)
print(sorted(back_count[0:5]))

print(id(count))

