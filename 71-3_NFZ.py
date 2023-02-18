class Choroba:
    def __init__(self, d, r):
        self.nazwa = d
        self.data_zachor = r

    def __str__(self):
        return f"{self.nazwa}, zachorowanie: {self.data_zachor}."



class ChoroboManager:
    def __init__(self):
        self.listaChorob = []


    def dodajChor (self, d,r):
        jakas = Choroba(d,r)
        self.listaChorob.append(jakas)
        print("dodana")


    def pokaChor (self):
        print(f"Pacjent: {self.getImie()} {self.getNazwisko()} cierpiał (lub cierpi) na takie przypadłości:")
        for g in self.listaChorob:
            print(g)
        print()


    def usunChor (self, par):
        for g in self.listaChorob:
            if (g.nazwa == par):
                self.listaChorob.remove(g)
                print("Choroba zniknęła. W końcu.")
                print("")


class Pacjent(ChoroboManager):
    def __init__(self, t, c):
        super().__init__()
        self.__imie = t
        self.__nazwisko = c
        self.menuPacj()


    def getImie(self):
        return self.__imie


    def setImie(self, h):
        self.__imie = h


    def getNazwisko(self):
        return self.__nazwisko


    def setNazwisko(self, h):
        self.__nazwisko = h


    def menuPacj(self):
        while (True):
            print(f"Definiujesz pacjenta: {self.getImie()}, {self.getNazwisko()}. Możesz wykonać następujące czynności:")
            dec = input("1-dodaj chorobe, 2-pokaz choroby, 3-usun, 4-koniec \n")

            if (dec == '1'):
                ghgh = input("Podaj nazwę choroby: ")
                bvbv = input("Podaj datę zachorowania: ")
                self.dodajChor(ghgh, bvbv)

            if (dec == '2'):
                self.pokaChor()

            if (dec == '3'):
                hhhhh = input("Podaj nazwę choroby: ")
                self.usunChor(hhhhh)

            if (dec == '4'):
                break


    def __str__(self):
        return f"Dane pacjenta {self.__imie}, {self.__nazwisko}"
        # return f"Dane pacjenta {self.__imie}, {self.__nazwisko}, {self.pokaChor()}"



class PacjentManager:
    def __init__(self):
        self.listaPacjentow = []

    def dodajPacj (self,t,c):
        ktos = Pacjent(t,c)
        self.listaPacjentow.append(ktos)
        print("dodany")


    def pokaPacj (self):
        for g in self.listaPacjentow:
            print(g) # Tutaj korzystam z metody STRING z klasy Pacjent
            # print(g.getImie(), g.getNazwisko()) # Tutaj wymieniam konkretne wartości.


    def edytujPacj (self, frek):
        for g in self.listaPacjentow:
            if (g.getNazwisko() == frek):
                g.menuPacj()


    def usunPacj (self, par):
        for g in self.listaPacjentow:
            if (g.getNazwisko() == par):
                self.listaPacjentow.remove(g)
                print("Już go nie ma.")
                print("")



class Przychodnia(PacjentManager):
    def __init__ (self,n,m):
        super().__init__()
        self.nazwaPrzych = n
        self.miasto = m


    def menu(self):
        print(f"Witaj w przychodni {self.nazwaPrzych}")
        while(True):
            print(f"#### MENU przychodni {self.nazwaPrzych} ####")
            dec = input(" 1- dodaj pacjenta do przychodni, 2-pokaż listę pacjentów, 3-edytuj dane pacjenta, 4-usun pacjenta z przychodni, 5-koniec \n")

            if (dec == '1'):
                ghgh = input("Podaj imię pacjenta: ")
                bvbv = input("Podaj nazwisko pacjenta: ")
                self.dodajPacj(ghgh, bvbv)

            if (dec == '2'):

                self.pokaPacj()

            if (dec == '3'):
                hhhhh = input("Podaj nazwisko pacjenta: ")
                self.edytujPacj(hhhhh)

            if (dec == '4'):
                hhhhh = input("Podaj nazwisko pacjenta: ")
                self.usunPacj(hhhhh)

            if (dec == '5'):
                break



class PrzychManager:
    def __init__(self):
        self.listaPrzychodni = []


    def dodajPrzych (self,n,m):
        ktos = Przychodnia(n,m)
        self.listaPrzychodni.append(ktos)
        print("dodana")


    def pokaPrzych (self):
        for g in self.listaPrzychodni:
            print(f'Przychodnia "{g.nazwaPrzych}" w mieście {g.miasto}')


    def usunPrzych (self, par):
        for g in self.listaPrzychodni:
            if (g.nazwaPrzych == par):
                self.listaPrzychodni.remove(g)
                print("Już jej nie ma.")
                print("")


    def edytujPrzych (self, par):
        # print(self.listaPrzychodni)
        for g in self.listaPrzychodni:
            if (g.nazwaPrzych == par):
                g.menu()



class Organizacja(PrzychManager):
    def __init__(self, l):
        super().__init__()
        self.nazwaOrganizacji = l
        self.menu()

    # konstruktor inicjalizujący pole publiczne nazwaFirmy
    # wysołanie konstruktora z nadklasy
    # wywołanie metody menu()


    def menu(self):

        print(f"Witaj w {self.nazwaOrganizacji}")
        while(True):
            print()
            print(f"#### MENU {self.nazwaOrganizacji} ####")
            dec = input("1-dodaj przychodnię, 2-pokaz przychodnie, 3-usun przychodnię, 4 - edytuj pacjentów przychodni, 5-koniec: \n")

            if (dec == '1'):
                ghgh = input("Podaj nazwę przychodni: ")
                bvbv = input("Podaj miasto: ")
                self.dodajPrzych(ghgh, bvbv)

            if (dec == '2'):
                self.pokaPrzych()

            if (dec == '3'):
                hhhhh = input("Podaj nazwę przychodni: ")
                self.usunPrzych(hhhhh)

            if (dec == '4'):
                blurp = input("Do której przychodni wchodzimy?: ")
                self.edytujPrzych(blurp)

            if (dec == '5'):
                break


osPrawna = Organizacja("NFZ")

