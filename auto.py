class Auto:
    def __init__(self, rekisterinumero, omistaja):
        self.rekisterinumero = rekisterinumero
        self.omistaja = omistaja

    def __str__(self):
        return "Auto (" + self.rekisterinumero + ")"
