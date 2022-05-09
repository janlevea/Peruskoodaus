import unittest

from kirjasto import Kirja, Luku, NumerointiVirhe

class TestLaskeSivujenLkm(unittest.TestCase):
    def test_kaksi_lukua(self):
        kirja = Kirja("Testikirja", "Kirjoittaja")
        kirja.lisaa_luku("Eka", sivuja=20)
        kirja.lisaa_luku("Toka", sivuja=80)

        tulos = kirja.lasku_sivujen_lkm()

        self.assertEqual(tulos, 100)

    def test_ei_yhtaan_lukua(self):
        kirja = Kirja("Testikirja", "Kirjoittaja")

        tulos = kirja.lasku_sivujen_lkm()

        self.assertEqual(tulos, 0)

    def test_yksi_luku(self):
        kirja = Kirja("Testikirja", "Kirjoittaja")
        kirja.lisaa_luku("Luku", sivuja=123)

        tulos = kirja.lasku_sivujen_lkm()

        self.assertEqual(tulos, 123)

class TestLisaaLuku(unittest.TestCase):
    def test_yksi_luku(self):
        kirja = Kirja("Testikirja", "Kirjoittaja")

        kirja.lisaa_luku("Testiluku", sivuja=5)

        self.assertEqual(len(kirja.luvut), 1)
        self.assertIsInstance(kirja.luvut[0], Luku)
        self.assertEqual(kirja.luvut[0].numero, 1)
        self.assertEqual(kirja.luvut[0].otsikko, "Testiluku")
        self.assertEqual(kirja.luvut[0].sivuja, 5)

    def test_kaksi_lukua(self):
        kirja = Kirja("Testikirja", "Kirjoittaja")

        kirja.lisaa_luku("Testiluku", sivuja=5)
        kirja.lisaa_luku("Toinen luku", sivuja=10)

        self.assertEqual(len(kirja.luvut), 2)
        self.assertIsInstance(kirja.luvut[0], Luku)
        self.assertIsInstance(kirja.luvut[1], Luku)
        self.assertEqual(kirja.luvut[0].numero, 1)
        self.assertEqual(kirja.luvut[0].otsikko, "Testiluku")
        self.assertEqual(kirja.luvut[0].sivuja, 5)
        self.assertEqual(kirja.luvut[1].numero, 2)
        self.assertEqual(kirja.luvut[1].otsikko, "Toinen luku")
        self.assertEqual(kirja.luvut[1].sivuja, 10)

    def test_annettu_numero(self):
        kirja = Kirja("Testikirja", "Kirjoittaja")

        kirja.lisaa_luku("Testiluku", sivuja=5, numero=42)

        self.assertEqual(kirja.luvut[0].numero, 42)

    def test_automaattinen_numero_ja_annettu_numero(self):
        kirja = Kirja("Testikirja", "Kirjoittaja")

        kirja.lisaa_luku("Testiluku 1", sivuja=5)
        kirja.lisaa_luku("Testiluku 2", sivuja=5, numero=42)
        kirja.lisaa_luku("Testiluku 3", sivuja=5)

        self.assertEqual(kirja.luvut[0].numero, 1)
        self.assertEqual(kirja.luvut[1].numero, 42)
        self.assertEqual(kirja.luvut[2].numero, 3)

    def test_automaattinen_numero_tormaa_annettuun(self):
        kirja = Kirja("Testikirja", "Kirjoittaja")

        kirja.lisaa_luku("Testiluku 1", sivuja=5, numero=2)
        with self.assertRaisesRegex(NumerointiVirhe, "Numero varattu: 2"):
            kirja.lisaa_luku("Testiluku 2", sivuja=5)         

        # self.assertEqual(len(kirja.luvut), 1)

if __name__ == '__main__':
    unittest.main()