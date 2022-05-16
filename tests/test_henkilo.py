import pytest

from henkilo import Henkilo1, Henkilo2


@pytest.mark.parametrize("teksti", ["", "Jaana", "_"])
@pytest.mark.parametrize("luku", [0, 40])
def test_henkilo1_str(teksti, luku):
    henkilo = Henkilo1(nimi=teksti, ika=luku)

    tulos = str(henkilo)

    assert tulos == teksti


def test_henkilo2_init():
    henkilo = Henkilo2("Etu", "Suku", 1990)

    assert henkilo.etunimi == "Etu"
    assert henkilo.sukunimi == "Suku"
    assert henkilo.syntymavuosi == 1990


def test_henkilo2_nimi():
    henkilo = Henkilo2("Tiina", "Testaaja", 1995)
    
    tulos = henkilo.nimi

    assert tulos == "Tiina Testaaja"
