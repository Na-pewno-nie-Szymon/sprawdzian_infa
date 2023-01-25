"""
i = 0
n = input
x = input
"""
#Zadanie 1
def zad1():
    n = int(input('Podaj n: '))
    x = int(input('Podaj X: '))
    Y = 0
    silniaI = 1
    for i in range(n+1):
        if i == 0:
            silniaI = 1
        else:
            silniaI *= i 
        Y += (x**i)/silniaI

    print(f'Y = {Y}')


#zadanie2
def zad2():
    with open('infa_test_sroda/dane.txt', 'r') as F:
        file = F.readlines()
    lista = []
    for i in file:
        lista.append(int(i))

    min = lista[0]
    min_idx = 0
    maxx = lista[0]
    max_idx = 0

    for idx, val in enumerate(lista):
        if val < min:
            min = val
            min_idx = idx
        elif val > maxx:
            maxx = val
            max_idx = idx

    print(min_idx + 1, max_idx + 1)
    

def zad3():
    n = int(input('Podaj n: '))
    m = int(input('Podaj m: '))

    headers = ['*']
    for i in range(n,m+1):
        if i % 2 != 0:
            headers.append(i)
    
    tabliczka_mnozenia = [headers]
    for i in range(1, len(headers)):
        row = [headers[i]]
        for j in range(1, len(headers) ):
            row.append(headers[i] * headers[j])
        tabliczka_mnozenia.append(row)

    for num in tabliczka_mnozenia:
        print(*num, sep='\t')

def zad4():
    liczba = input('Podaj dowolną liczbę całkowitą: ')

    suma_liczby = 0
    for i in liczba:
        suma_liczby += int(i)
    
    print(suma_liczby)

def czypierwsza(liczba):
    if liczba == 2:
        return True
    else:
        for i in range(2,liczba):
            if liczba % i == 0:
                return False
        return True

def zad5():
    urs_inpt = 1
    lista_liczb = []
    while urs_inpt > 0:
        urs_inpt = int(input())
        lista_liczb.append(urs_inpt)

    #print(lista_liczb)
    liczby_pierwsze = []
    for liczba in lista_liczb:
        if czypierwsza(liczba = liczba):
            #print(liczba)
            liczby_pierwsze.append(liczba)

    for num in liczby_pierwsze:
        lista_liczb.remove(num)
    
    print(lista_liczb)

if __name__ == '__main__': zad5()
    

"""
1. Napisać funkcję która obliczy wartość wyrażenia:
   i=n
Y = E  (x**i)/i!
   i=0
I pokazać jej działanie w przykładowym programie
UWAGA: nie można użyć gotowej funkcji sum() i silni

2. W pliku 'dane.txt' (należy go wcześniej przygotować) znajdują się liczby. Należy znaleźć POZYCJĘ największej i najmniejszej
Wynik wydrukować
nie można min() i max()

3. Wypisać tabliczkę mnożenia dla liczb nieparzystych z zakresu od 'n' do 'm'. Wartości n i m podaje użytkownik

4. Uzytkownik wprowadza liczbę całkowitą. Należy napisać fukcję, która na podstawie tej liczby zwróci wynik będący sumą cyfr tej liczby

5. Użytkownik wprowadza do listy dowolną ilość liczb całkowitych. Wprowadzenie liczb kończy się z chwilą wprowadzenia liczby 0 lub mniejszej.
Należy z tak utworzonej listy usunąć wszystkie liczby pierwsze po czym wydrukować tak zmodyfikowaną.
UWAGA: mamy wydrukować listę
UWAGA: nie można użyć gotowej funkcji inprime()
"""
