import unittest

from henkilo import Henkilo1


class TestaaStringiksiMuunnos(unittest.TestCase):
    def test_nimi(self):
        henkilo = Henkilo1(nimi="Jaana", ika=40)

        tulos = str(henkilo)

        self.assertEqual(tulos, "Jaana")

    def test_tyhja_nimi(self):
        henkilo = Henkilo1(nimi="", ika=40)

        tulos = str(henkilo)

        self.assertEqual(tulos, "")
