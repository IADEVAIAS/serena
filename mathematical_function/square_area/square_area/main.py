import math


class Poligono:
    def area(self):
        pass


class Quadrato(Poligono):
    def __init__(self, lato):
        self.lato = lato

    def area(self):
        return self.lato * self.lato


class Rettangolo(Poligono):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza


class Cerchio(Poligono):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio ** 2


def main():
    scelta = input("Quale poligono vuoi calcolare l'area? (quadrato/rettangolo/cerchio): ").lower()

    if scelta == "quadrato":
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        figura = Quadrato(lato)
    elif scelta == "rettangolo":
        base = float(input("Inserisci la lunghezza della base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        figura = Rettangolo(base, altezza)
    elif scelta == "cerchio":
        raggio = float(input("Inserisci il raggio del cerchio: "))
        figura = Cerchio(raggio)
    else:
        print("Scelta non valida.")
        return

    print("L'area del", scelta, "è:", figura.area())


if __name__ == "__main__":
    main()
