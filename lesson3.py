#1
numbers = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(number):
    if number[:1].istitle() == False:
            print(numbers.get(number, 'такой цифры нет'))
    elif number [:1].istitle() == True:
        number = number.lower()
        print(numbers.get(number, 'такой цифры нет').title())

num_translate('four')

#2

from random import randrange
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(amount):
    jokes = []
    for joke in range(amount):
        joke = ' '.join([nouns[randrange(len(nouns))], adverbs[randrange(len(adverbs))], adjectives[randrange(len(adjectives))]])
        jokes.append(joke)
    print(jokes)


get_jokes(1)

#3

def thesaurus(*args):
    namelist = list(map(str, args))
    dictionary = {}
    for name in namelist:
        first_word = name[0]
        dictionary[first_word] = dictionary.get(first_word, []) + [name]
    return print(dictionary)


thesaurus("Иван", "Мария", "Петр", "Илья")

