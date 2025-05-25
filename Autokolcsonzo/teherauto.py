from auto import Auto


class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, max_terheles):
        super().__init__(rendszam, tipus, berleti_dij)
        self.max_terheles = max_terheles

    def __str__(self):
        return f"Teherautó: {self.tipus} ({self.rendszam}), Max terhelés: {self.max_terheles} kg, {self.berleti_dij} Ft/nap"
