n = int(input())

numeros = []
numerosCertos = []
soma = 0

for i in range(n):
  pn = input()
  numeros.append(int(pn))

for i in numeros:
  if i != 0:
    numerosCertos.append(i)
  else:
    numerosCertos.pop()

for i in numerosCertos:
  soma += i

print(soma)