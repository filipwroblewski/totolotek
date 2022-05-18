from totolotek import ustawienia, losowanie, strzaly, podsumowanie


ile_losowan = int(input('Podaj ilosc losowan: '))
for i in range(ile_losowan):
    a, b = ustawienia()
    losowanie(a, b)

    arr = losowanie(a, b)

    podsumowanie(arr, strzaly(a, b))
