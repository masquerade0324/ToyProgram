import os

path = "/write/your/path"
dirs = os.listdir(path)

for dir in dirs:
    if len(dir) == 8 and dir.isdigit():
        os.rename(path + "/" + dir, path + "/" + dir[0:4] + "-" + dir[4:6] + "-" + dir[6:8])

print(os.listdir(path))
