import pytest

from henkilo import Henkilo1, Henkilo2


@pytest.mark.parametrize("teksti", ["", "Jaana"])
def test_henkilo1_str(teksti):
    henkilo = Henkilo1(nimi=teksti, ika=40)

    tulos = str(henkilo)

    assert tulos == teksti


def test_henkilo2_init():
    henkilo = Henkilo2("Etu", "Suku", 1990)

    assert henkilo.etunimi == "Etu"
    assert henkilo.sukunimi == "Suku"
    assert henkilo.syntymavuosi == 1990
