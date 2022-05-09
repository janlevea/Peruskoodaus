"""
Jotain aivan perusasioiden esittelyjä.
"""
from datetime import datetime


OLETUSLUKU = 43

def main():
    #print("Tästä lähtee")
    # vari = "musta"
    # funktio2("huhuhu", f"{vari} koira")
    # funktio2(elukka2="toka elukka", elukka="eka elukka", elukka3uhuhuh="moi", joku_muu="huh huh")

    # a = 2

    # if not isinstance(a, (int, float)):
    #     print("a ei ole luku")
    # elif a == 0 or a == 1:
    #     print("a oli nolla tai 1")
    # elif a == 2:
    #     print("a oli 2")
    # elif a > 0:
    #     print("a oli jokin positiivinen luku")
    # else:
    #     print("a oli jotain muuta")


















    # import datetime

    # a = datetime.timedelta(seconds=1)

    # if a or not b:
    #     print(f"{a!r} oli tosi")
    # else:
    #     print(f"{a!r} ei ollut tosi")




    # tietorakenne = {
    #     "joku juttu": {
    #         "muu asia": {
    #             "lista": [1, 2, 3, [4, 5], object(), datetime.datetime(1995, 12, 31)],
    #             "toinen avain": 333,
    #             "kolmas avain": 2,
    #             'merkkijono': 40,
    #             42: 111,
    #             None: "tyhjä",
    #             "tervehdys": "moi"
    #         }
    #     },
    #     "asioita": [],
    # }

    # tietorakenne["joku juttu"]["muu asia"]["merkkijono"]
    
    # lista = [3, "moi", 4.5, object()]
    # toinen_lista = tietorakenne["joku juttu"]["muu asia"]["lista"]

    # for alkio in list(lista):
    #     print("ollaan alkiossa", alkio)
    #     lista.append("hei")
    #     toinen_lista.append("hei")

    # print("toinen_lista", toinen_lista)
    # print(tietorakenne)


    def kerro_kirjasta(kirja):
        nimi = kirja.nimi
        sivuja = kirja.lasku_sivujen_lkm()

        print(f'Kirjassa "{nimi}" on {sivuja} sivua.')


    from kirjasto import hassu_kirja, hopo_kirja

    kerro_kirjasta(hopo_kirja)
    kerro_kirjasta(hassu_kirja)





    # Context manager ja with

    # Tiedoston avaaminen ja sulkeminen ilman
    # with-lauseketta saattaa jättää tiedoston
    # auki virheen sattuessa:
    #
    # file = open("tiedosto.txt", "wt")
    # file.write("Moi!\n")
    # print("hei")
    # joku_funktio()  # tapahtuu virhe, poikkeus nousee
    # file.write("Viimeinen rivi\n")  # tätä ei kutsuta...
    # file.close()  # ...tai tätä, jos aiemmalla rivillä oli poikkeus

    # with-lausekkeen avulla tiedosto suljetaan automaattisesti
    # myös poikkeuksen noustessa:
    #
    # with open("tiedosto.txt", "wt") as file:
    #     file.write("Moi!\n")
    #     print("hei")
    #     joku_funktio()
    #     file.write("Viimeinen rivi\n")





















def funktio2(elukka, elukka2, luku=OLETUSLUKU):
    print("Tää on funktio 2")
    print("Elukka on", elukka + ". Toinen elukka on", elukka2 + ". Luku on", str(luku) + ". Ja jotain.")
    print(f"Elukka on {elukka:^12}. Toinen elukka on {elukka2:^7}. Luku on {luku:08}. Ja jotain.")
    joku_teksti = f"Elukka on {elukka}"

    funktio3(joku_teksti)

    print("Toinen elukka on", elukka2)
    print("Luku on", luku)


def funktio3(muuttuja):
    print(muuttuja)


if __name__ == '__main__':
    main()
