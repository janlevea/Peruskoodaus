class NumerointiVirhe(ValueError):
    pass


class Kirja:
    def __init__(self, nimi, kirjoittaja):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.luvut = []

    def lisaa_luku(self, otsikko, sivuja, numero=None):
        if numero is None:
            numero = len(self.luvut) + 1
        self.luvut.append(
            Luku(
                numero=numero,
                otsikko=otsikko,
                sivuja=sivuja,
            )
        )
        self.tarkista_lukujen_numerointi()

    def tarkista_lukujen_numerointi(self):
        numerot = set()
        for luku in self.luvut:
            if luku.numero in numerot:
                raise NumerointiVirhe(f"Numero varattu: {luku.numero}")
            numerot.add(luku.numero)

    def lasku_sivujen_lkm(self):
        return sum(luku.sivuja for luku in self.luvut)


class Luku:
    def __init__(self, numero, otsikko, sivuja):
        self.numero = numero
        self.otsikko = otsikko
        self.sivuja = sivuja


hassu_kirja = Kirja(nimi="Hassukirja", kirjoittaja="Hassu Klovni")
hassu_kirja.lisaa_luku("Johdanto", sivuja=123)
hassu_kirja.lisaa_luku("Johtopäätökset", sivuja=222)

# tekisi saman kuin alla:
#  hopo_kirja = Kirja("Höpökirja", "Hiiri Höpönen")
hopo_kirja = Kirja(nimi="Höpökirja", kirjoittaja="Hiiri Höpönen")
hopo_kirja.lisaa_luku("Johdanto", sivuja=3)
hopo_kirja.lisaa_luku("Hei vaan", sivuja=12)


hopo_kirja_dictionaryna = {
    "nimi": "Höpökirja",
    "kirjoittaja": "Hiiri Höpönen",
    "luvut": [
        {
            "numero": 1,
            "otsikko": "Johdanto",
            "sivuja": 3,
        },
        {
            "numero": 2,
            "otsikko": "Hei vaan",
            "suvuja": 12,
        },
    ]
}
