def gen_fib(N):
        if N == 0:
                return []
        if N == 1:
                return ["1"]
        if N == 2:
                return ["1", "1"]
        else:
          primeiro, segundo = 1, 1
          pivot = primeiro + segundo
          lista = ["1", "1"]
          for i in range(2, N):
              lista.append(str(pivot))
              primeiro, segundo = segundo, pivot
              pivot = primeiro + segundo
          return lista

print gen_fib(10)

def fib(lst):
    numeros = lst.split(",")
    a = gen_fib(len(numeros))
    for i, numero  in enumerate(numeros):
        if a[i] != numero:
            return False
    return True

assert not fib('1,1,2,2'), 'Nao'


if fib('1,1,2,3'):
    print 'Sim'
else:
    print 'Nao'
