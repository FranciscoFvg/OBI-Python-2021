a , b = input().split()
a , b = int(a), int(b)

c = 0

mediana = [a,b]
mediana.sort()
mediana = mediana[0]

c = int(mediana) * 3 - a - b

print(c)