import hetu3

class VakioHetu:
    def __str__(self):
        return "HETU42"

    def ika(self):
        return 42


def main() -> None:
    ht = hetu3.Henkilotunnus('200588-777P')
    ht2 = VakioHetu()
    nayta_ika(ht)
    nayta_ika(ht2)


def nayta_ika(h):
    i = h.ika()
    print("Henkilötunnuksen", h, "ikä on", i)


if __name__ == '__main__':
    main()
