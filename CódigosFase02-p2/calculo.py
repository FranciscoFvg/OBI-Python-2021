s = int(input())
a = int(input())
b = int(input())

interval = list(range(a,(b+1)))
interval = [format(x, '02d') for x in interval]

sumInterval = []
for n in interval:
    sumInterval.append(sum(int(i) for i in n))

check = 0

for n in sumInterval:
    if n == s:
        check += 1

print(check)
