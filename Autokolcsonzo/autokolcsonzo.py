from datetime import date
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles


class Autokolcsonzo:
    def __init__(self, nev: str):
        self.nev = nev
        self.autok = []      # Az autók listája
        self.berlesek = []   # A bérlések listája (aktív és korábbi egyaránt)

    def auto_hozzaadas(self, auto):
        """Új autó hozzáadása a kölcsönző listájához"""
        self.autok.append(auto)

    def berel_auto(self, rendszam: str) -> bool:
        """Autó bérlése rendszám alapján (ha elérhető)"""
        # Megkeressük az autót a rendszám alapján
        kivalasztott_auto = None
        for auto in self.autok:
            if auto.rendszam == rendszam:
                kivalasztott_auto = auto
                break
        if kivalasztott_auto is None:
            return False  # nincs ilyen autó a kölcsönzőben
        # Ellenőrizzük, hogy nincs-e már aktív bérlése ennek az autonak
        for berles in self.berlesek:
            if berles.auto == kivalasztott_auto and berles.aktiv:
                return False  # az autó már ki van bérelve jelenleg
        # Létrehozzuk az új bérlést a mai dátummal
        uj_berles = Berles(kivalasztott_auto, date.today())
        self.berlesek.append(uj_berles)
        return True

    def lemond_berles(self, rendszam: str) -> bool:
        """Bérlés lemondása rendszám alapján (ha létező aktív bérlés)"""
        # Megkeressük az aktív bérlést az adott rendszámú autóra
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.aktiv:
                berles.aktiv = False  # a bérlést lezárjuk (lemondjuk)
                return True
        return False  # nem található ilyen aktív bérlés

    def aktualis_berlesek(self):
        """Lekérdezi az összes jelenleg aktív bérlést"""
        return [berles for berles in self.berlesek if berles.aktiv]

    def lista_autok(self):
        """Lekérdezi az összes autó listáját"""
        return self.autok

    def auto_elerheto(self, rendszam: str) -> bool:
        """Ellenőrzi, hogy a megadott rendszámú autó jelenleg elérhető-e (nincs kölcsönben)"""
        kivalasztott_auto = None
        for auto in self.autok:
            if auto.rendszam == rendszam:
                kivalasztott_auto = auto
                break
        if kivalasztott_auto is None:
            return False
        for berles in self.berlesek:
            if berles.auto == kivalasztott_auto and berles.aktiv:
                return False
        return True
