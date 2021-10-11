#1, 2
with open('nginx_logs.txt') as f:
    data = []
    spam = {}
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spam.setdefault(splitted[0], 0)
        spam[splitted[0]] += 1

spam = sorted(spam.items(), key=lambda x: x[1], reverse=True)
print(spam[:3])

#3
import json
from itertools import zip_longest

dict = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        sum_lines_users = sum(1 for line in users)
        sum_lines_hobby = sum(1 for line in hobby)

        if sum_lines_users > sum_lines_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)

        for line_user, line_hobby in zip_longest(users, hobby):
            dict[line_user.strip()] = line_hobby.strip() if line_hobby is not None else line_hobby

with open('task3.json', 'w', encoding='utf-8'):
    json.dump(dict, f, ensure_ascii=False)
print(dict)



