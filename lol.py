import sys

lol = sys.stdin.readlines()
print(lol)
p = "".join(lol)
print(p)
count = 0
for i in p:
    if i == "\n":
        count += 1
print(count)
