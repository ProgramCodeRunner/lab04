import random


def FindEquivalentElement(mass):
    elem = set.intersection(*map(set, mass))

    numerOfElem = 0
    for _ in elem:
        numerOfElem = numerOfElem + 1

    print("Количество одинаковых элементов: ", numerOfElem)
    print("Общие элементы списков:")
    print(elem)


if __name__ == '__main__':
    print("Введите количество списков: ")
    m = int(input())
    print("Введите размерность списков: ")
    n = int(input())

    massOfLists = [0] * m

    for i in range(m):
        globals()['a{}'.format(i)] = [0] * n
        for j in range(n):
            globals()['a{}'.format(i)][j] = int(random.random() * 1000)
        tempMass = globals()['a{}'.format(i)]
        massOfLists[i] = sorted(tempMass, reverse=False)

    print("Полученные списки: ")
    for i in range(m):
        print(massOfLists[i])

    FindEquivalentElement(massOfLists)
