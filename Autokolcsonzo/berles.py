class Berles:
    def __init__(self, auto, datum, berlo_neve):
        self.auto = auto
        self.datum = datum
        self.berlo_neve = berlo_neve

    def __str__(self):
        return f"{self.datum} - {self.auto.rendszam} - {self.auto.tipus} ({self.berlo_neve})"
