from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles


class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaad(self, auto):
        self.autok.append(auto)

    def auto_kereses(self, rendszam):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                return auto
        return None

    def berel(self, rendszam, datum, berlo_neve):
        auto = self.auto_kereses(rendszam)
        if not auto:
            return False, "Nincs ilyen rendszámú autó!"
        # Ellenőrizzük, hogy az autó már foglalt-e aznapra
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                return False, "Ez az autó már foglalt ezen a napon!"
        self.berlesek.append(Berles(auto, datum, berlo_neve))
        return True, f"Bérlés sikeres! Ár: {auto.berleti_dij} Ft/nap"

    def berles_lemondas(self, rendszam, datum, berlo_neve):
        for berles in self.berlesek:
            if (berles.auto.rendszam == rendszam
                    and berles.datum == datum
                    and berles.berlo_neve == berlo_neve):
                self.berlesek.remove(berles)
                return True, "Bérlés lemondva."
        return False, "Nincs ilyen bérlés!"

    def listaz_berlesek(self):
        if not self.berlesek:
            print("Nincs aktív bérlés.")
        else:
            print("Aktuális bérlések:")
            for berles in self.berlesek:
                print("  -", berles)
