from henkilo import Henkilo1, Henkilo2


def test_henkilo1_nimi():
    henkilo = Henkilo1(nimi="Jaana", ika=40)

    tulos = str(henkilo)

    assert tulos == "Jaana"


def test_henkilo1_tyhja_nimi():
    henkilo = Henkilo1(nimi="", ika=40)

    tulos = str(henkilo)

    assert tulos == ""


def test_henkilo2_init():
    henkilo = Henkilo2("Etu", "Suku", 1990)

    assert henkilo.etunimi == "Etu"
    assert henkilo.sukunimi == "Suku"
    assert henkilo.syntymavuosi == 1990
