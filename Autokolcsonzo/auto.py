from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def kategoria(self) -> str:
        """Az autó kategóriája (Személyautó vagy Teherautó)"""
        pass

    def __str__(self):
        return f"{self.rendszam} - {self.tipus} - {self.berleti_dij} Ft/nap"
