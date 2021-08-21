n, m = input().split()
n, m = int(n), int(m)

ingredientes = list(range(1, n + 1))
conjutos = []
ctotal = 0

def combs_tam_n(lista, n):
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lista)):

        m = lista[i]
        reLista = lista[i + 1:]

        for p in combs_tam_n(reLista, n - 1):
            l.append([m] + p)

    return l

pares = []

for i in range(m):
    num, num2 = input().split()
    par = []
    par.append(int(num))
    par.append(int(num2))
    pares.append(par)

for i in range(n):
    conjutos.append(combs_tam_n(ingredientes, i+1))

for i, c in enumerate(conjutos):
    for p in pares:
        for j, si in enumerate(c):
            if set(p).issubset(set(si)):
                if not len(conjutos[i]) == 0:
                    print(i,j)
                    del conjutos[i][j]

for c in conjutos:
    ctotal += len(c)

print(ctotal)
