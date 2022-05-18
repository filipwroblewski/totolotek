import random


def set_up():
    try:
        ile_liczb = int(input('Podaj ilosc typowanych liczb (0;100): '))
        maks_liczba = int(input('Podaj maksymalna losowana liczbe (0;1000): '))
        if (not (maks_liczba > ile_liczb) or
            not (0 < maks_liczba < 1000) or
                not (0 < ile_liczb < 100)):
            print('Bledne dane')
            exit()

        return ile_liczb, maks_liczba
    except ValueError:
        print('Bledne dane')
        exit()


def losowanie():
    liczby = []
    i = 0
    while i < ile_liczb:
        liczba = random.randint(1, maks_liczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i += 1

    return liczby


def strzaly():
    typy = set()
    i = 0
    while i < ile_liczb:
        try:
            typ = int(input(f'Podaj liczbe {i+1}: '))
        except ValueError:
            print('Bledne dane')
            exit()

        if 0 < typ <= maks_liczba and typ not in typy:
            typy.add(typ)
            i += 1

    return typy


def podsumowanie(typy):
    trafione = typy & set(liczby)  # & - czesc wspolna zbiorow
    if trafione:
        print(f'Ilosc trafien: {len(trafione)}')
        print(f'Trafione liczby: {trafione}')
    else:
        print('Brak trafien')
    # print(f'Wpisane liczby: {typy}')
    # print(f'Wylosowane liczby: {liczby}')


ile_liczb, maks_liczba = set_up()
losowanie()

liczby = losowanie()

podsumowanie(strzaly())
