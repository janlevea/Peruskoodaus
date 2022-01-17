import auto
import henkilo


def kysy_auton_tiedot():
    reknum = input("Rekisterinumero:")
    if not reknum:
        return None
    omistaja = kysy_henkilon_tiedot("Omistajan")
    return auto.Auto(reknum, omistaja)


def kysy_henkilon_tiedot(kenen):
    etunimi = input(kenen + " etunimi:")
    sukunimi = input(kenen + " sukunimi:")
    syntymavuosi = input(kenen + " syntymävuosi:")
    return henkilo.Henkilo2(etunimi, sukunimi, syntymavuosi)


def main():
    autot = []

    while True:
        uusi_auto = kysy_auton_tiedot()
        if not uusi_auto:
            break
        autot.append(uusi_auto)

    for a in autot:
        print(a)


if __name__ == "__main__":
    main()
