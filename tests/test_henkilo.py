import unittest

from henkilo import Henkilo1, Henkilo2


class TestaaHenkilo1StringiksiMuunnos(unittest.TestCase):
    def test_nimi(self):
        henkilo = Henkilo1(nimi="Jaana", ika=40)

        tulos = str(henkilo)

        self.assertEqual(tulos, "Jaana")

    def test_tyhja_nimi(self):
        henkilo = Henkilo1(nimi="", ika=40)

        tulos = str(henkilo)

        self.assertEqual(tulos, "")


def test_henkilo2_init():
    henkilo = Henkilo2("Etu", "Suku", 1990)

    assert henkilo.etunimi == "Etu"
    assert henkilo.sukunimi == "Suku"
    assert henkilo.syntymavuosi == 1990
