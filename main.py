def wypisz_samochod(marka, model):
    print("{0},{1}".format(marka,model))

def czystary(wiek):
    MAX = 15
    if wiek < MAX:
        return False
    else:
        return True

if __name__=="__main__":
    marka = 'Fiat'
    model = 'Punto'
    wiek = 10

    wypisz_samochod(marka, model)
    if wiek < 15:
        print('Nowe')
    else:
        print('Stare')




#if_name_=="_main_":

#imie = 'Irmina'
#nazwisko = 'B'

#pelne_imie = imie + '' + nazwisko

#ilosc_zwierzat_domowych = 2
#cena = 2 * 120

#print(cena)
#print(pelne_imie)



#print("Witaj w swiecie, {0}!".format(imie))
