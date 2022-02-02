from typing import List


def fibonacci(cap: int) -> iter:
    x, y = 0, 1
    for ii in range(cap):
        yield x
        x, y = y, x + y

def elimina(lista,valor):
    for i in range(len(lista)):
        if lista[i] % valor == 0:
            del lista[i]
    return lista

def main():
    a= [12,3,1,4,5,6,7,8,9,12]
    print(elimina(a, 2))

if __name__ == '__main__':
    main()
