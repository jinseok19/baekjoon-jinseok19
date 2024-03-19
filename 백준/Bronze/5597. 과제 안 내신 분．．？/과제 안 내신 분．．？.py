import sys
class_name = []

for i in range(1,29):
    class_name.append(int(sys.stdin.readline()))

for i in range(1,31):
    if i not in class_name:
        print(i)
