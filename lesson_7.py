#1
import os

folders_dict = {'my_project':['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in folders_dict.items():
    if os.path.exists(root):
        print(root, 'уже существует')
    else:
        for folder in folders:
            way = os.path.join(root, folder)
            os.makedirs(way)



#3
import os
import shutil

dir = 'my_dir'
if not os.path.exists(dir):
    os.mkdir(dir)

folder = r'my_project'
files = []

for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder = os.path.join(dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save)

#4
import os
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max = max(files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i += 10
    out_dict[i] = 0

for file in files:
    out_dict[10 ** len(str(file))] += 1

print(out_dict)
