from auto import Auto


class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ajtok_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ajtok_szama = ajtok_szama

    def __str__(self):
        return f"Személyautó: {self.tipus} ({self.rendszam}), {self.ajtok_szama} ajtó, {self.berleti_dij} Ft/nap"
