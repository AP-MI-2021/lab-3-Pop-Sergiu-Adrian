
from math import sqrt

def get_longest_average_below(lst, average):
    '''
        Retine secventa cea mai lunga de numere care au media mai mica de cat un numar citit de la tastatura
        :param lst o lista de nr intregi
        :param average un numar citit de la tastatura
        :return: o lista de numere care au aceasta proprietate
        '''
    current_min_index = 0
    min_index = max_index = 0
    current_average = lst[0]
    count = 1
    for current_max_index, i in enumerate(lst[1:]):
        if (current_average := current_average + i) / (count := count + 1) > average or \
                current_max_index + 2 >= len(lst):
            if current_average / count <= average:
                current_max_index += 1
            if max_index - min_index < current_max_index - current_min_index:
                min_index, max_index = current_min_index, current_max_index
            current_average = i
            count = 1
            current_min_index = (current_max_index := current_max_index + 1)
    return lst[min_index: max_index + 1]

def test_get_longest_average_below():
    assert (get_longest_average_below([2,4,6,12,45],4)==[2,4,6])
    assert(get_longest_average_below([1,7,2,9,23,56],8)==[1,7,2,9])

def is_prime(nr):
    '''
    Verify if a number nr is prime
    :param nr: int
    :return: True if is prime, False otherwise
    '''
    if nr < 2:
        return False
    if nr != 2 and nr % 2 == 0:
        return False
    for d in range(3, int(sqrt(nr)) + 1, 2):
        if nr % d == 0:
            return False
    return True

def test_is_prime():
    assert(is_prime(3) is True)
    assert (is_prime(6)is False)
    assert (is_prime(23) is True)

def valid_prime(nr):
    for i in range(len(nr)):
        if is_prime(nr[i])==0:
            return False
    return True

def get_longest_all_primes(lst):
    '''
    Determina cea mai lunga secventa de numere prime
    :param lst o lista de numere intregi
    :return o lista de numere care are acea proprietate
    '''
    lista_prime=[]
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)+1):
            if valid_prime(lst[i:j]) and len(lst[i:j]) > len(lista_prime):
                lista_prime=lst[i:j].copy()
    return lista_prime


def get_longest_concat_is_prime(lst):
    '''
    Determina cea mai lunga secventa de numere in care numarul format prin concatenare este prim
    :param lst o lista de numere intregi
    return o lista cu proprietatea respectiva
    '''
    max = []
    for stanga in range(len(lst)):
        for dreapta in range(stanga, len(lst)):
            if is_prime(int(''.join(map(str, lst[stanga: dreapta + 1])))):
                if len(max) < dreapta - stanga + 1:
                    max = lst[stanga: dreapta + 1]
    return max

def test_get_longest_concat_is_prime():
    assert (get_longest_concat_is_prime([2,3,67,78,23])==[2,3])
    assert (get_longest_concat_is_prime([2,2]) == [2])
    assert (get_longest_concat_is_prime([9,9,7]) == [9,9,7])


def menu():
    print('1. Citeste o lista ')
    print('2. Cea mai lunga secventa de numere prime')
    print('3. Cea mai lunga secventa care are media mai mica de cat un numar citit de la tastatura')
    print('4. Cea mai lunga secventa de numere prime')
    print('x. Exit')
def main():
    menu()
    lst = []
    while (option := input('Alegeti optiunea: ')):
        if option == '1':
            lst = [int(x) for x in input().split(' ')]
            print(lst)
        elif option == '2':
            print(get_longest_all_primes(lst))
        elif option == '3':
            average = float(input('Introduceti valoarea: '))
            print(get_longest_average_below(lst, average))
        elif option=='4':
            print(get_longest_concat_is_prime(lst))
        elif option=='x':
            break
        else:
            print('invalid option')
test_get_longest_average_below()
test_is_prime()
test_get_longest_concat_is_prime()

main()
