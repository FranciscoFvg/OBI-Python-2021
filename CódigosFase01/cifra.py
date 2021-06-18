c = input()

result = ''

def buscarMenor(lst):
    i = float("inf")
    for nr in lst:
        if nr < i:
            i = nr
    return i

def mudar(l, pc):
  replace = str(l)

  listaDV = []
  posv = 0;

  for i, vogaln in enumerate(von):
    listaDV.append(abs(con[pc] - vogaln))
    vvm = min(listaDV)
    posv = listaDV.index(vvm)
  
  replace += str(vo[posv])

  replace += str(co[pc + 1])

  return str(replace)

con = [ 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24]
co = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']

von = [ 1, 5, 9, 15, 21]
vo = ['a','e','i','o','u']

for i, letra in enumerate(c):
  for k in vo:
    if letra == k:
      result += str(letra)
  for j ,consoante in enumerate(co):
    if letra == consoante:
      result += mudar(letra, j)

print(result)

