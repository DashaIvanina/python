#1
def gen_num(n):
    for i in range(1, n, 2):
        yield i

gen_num_100 = gen_num(100)

print(next(gen_num_100))
print(next(gen_num_100))
print(next(gen_num_100))
print(next(gen_num_100))
print(next(gen_num_100))

2
gen = (i for i in range(1, 100, 2))
print(next(gen))
print(type(gen))

#3
import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

gen = ((i,j) for i, j in itertools.zip_longest(tutors, klasses))
print(next(gen))
print(next(gen))

print(type(gen))

#4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new = [num for i, num in enumerate(src) if num > src[i-1] and i != 0]
print(new)


#5
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

gen = [el for el in src if src.count(el) == 1]
print(gen)





