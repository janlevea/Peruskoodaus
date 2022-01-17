class Henkilo1:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

    def __str__(self):
        return self.nimi


class Henkilo2:
    def __init__(self, etunimi, sukunimi, syntymavuosi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.syntymavuosi = syntymavuosi

    @property
    def nimi(self):
        return self.etunimi + " " + self.sukunimi

    @property
    def ika(self):
        return self.laske_ika()

    def laske_ika(self):
        return 2022 - self.syntymavuosi

    def __str__(self):
        return self.nimi


if __name__ == "__main__":
    jaska = Henkilo2("Jaakko", "Saariluoma", 1967)
    minna = Henkilo2("Minna", "Canth", 1897)
    taina = Henkilo1("Taina", 32)

    henkilot = [jaska, minna, taina]

    # for henkilo in henkilot:
    #     print("Henkilö", henkilo.nimi, "on", henkilo.ika, "vuotta vanha.")

    print(jaska)
    print(minna)
    print(taina)
