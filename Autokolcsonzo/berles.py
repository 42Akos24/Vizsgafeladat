from datetime import date
# from auto import Auto  # not strictly needed to import Auto for functionality


class Berles:
    def __init__(self, auto, datum: date):
        self.auto = auto
        self.datum = datum
        # Egy napos bérlés: ha a dátum megegyezik a mai nappal, akkor aktív (még nincs visszahozva).
        # Ha korábbi dátum, akkor már lezárult bérlés.
        self.aktiv = True if datum == date.today() else False

    def __str__(self):
        status = "aktív" if self.aktiv else "lezárt"
        return f"Bérlés - Autó: {self.auto.rendszam} ({self.auto.tipus}), Dátum: {self.datum}, Státusz: {status}"
