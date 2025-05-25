from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto


def feltolt_alapadatok(kolcsonzo):
    auto1 = Szemelyauto("AAA-111", "Toyota Corolla", 10000, 4)
    auto2 = Szemelyauto("BBB-222", "Opel Astra", 12000, 5)
    auto3 = Teherauto("CCC-333", "Ford Transit", 18000, 3500)
    kolcsonzo.auto_hozzaad(auto1)
    kolcsonzo.auto_hozzaad(auto2)
    kolcsonzo.auto_hozzaad(auto3)
    # 4 db alap bérlés
    kolcsonzo.berel("AAA-111", "2024-06-01", "Kiss Béla")
    kolcsonzo.berel("BBB-222", "2024-06-02", "Nagy Anna")
    kolcsonzo.berel("CCC-333", "2024-06-03", "Teszt Elek")
    kolcsonzo.berel("AAA-111", "2024-06-04", "Fekete Géza")


def main():
    kolcsonzo = Autokolcsonzo("Teszt Autókölcsönző")
    feltolt_alapadatok(kolcsonzo)

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ MENÜ ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")
        valasztas = input("Választás (1-4): ")

        if valasztas == "1":
            rendszam = input("Rendszám: ").strip().upper()
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ").strip()
            berlo = input("Bérlő neve: ").strip()
            siker, uzenet = kolcsonzo.berel(rendszam, datum, berlo)
            print(uzenet)
        elif valasztas == "2":
            rendszam = input("Rendszám: ").strip().upper()
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ").strip()
            berlo = input("Bérlő neve: ").strip()
            siker, uzenet = kolcsonzo.berles_lemondas(rendszam, datum, berlo)
            print(uzenet)
        elif valasztas == "3":
            kolcsonzo.listaz_berlesek()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")


if __name__ == "__main__":
    main()
