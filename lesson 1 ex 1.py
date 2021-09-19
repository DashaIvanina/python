num = range(1, 1000)
new_num = [i ** 3 for i in num if i % 2 != 0]  # создаем список кубов нечетных чисел

print(new_num)

new_num2 = []
sum_numbers = 0
for num in new_num:
    i = num
    while num != 0:
        sum_numbers += num % 10
        num = num // 10
    if sum_numbers % 7 == 0:
        new_num2.append(i)
    sum_numbers = 0
print(sum(new_num2))

sum_numbers17 = 0
for num in new_num:
    sum17 = 0
    i = num
    num += 17
    while num != 0:
        sum17 += num % 10
        num = num // 10
    if sum17 % 7 == 0:
        sum_numbers17 += i

print(sum_numbers17)

