import os

print(os.listdir())
for dir in (dir for dir in next(os.walk('.'))[1] if not dir.startswith('.')):
    for file in next(os.walk(dir))[2]:
        path = os.path.join(dir, file)
        if os.stat(path).st_size == 0:
            print(path)
            os.remove(path)
