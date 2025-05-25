from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles
from datetime import date, timedelta


def main():
    # Autókölcsönző példány létrehozása kezdeti adatokkal
    kolcsonzo = Autokolcsonzo("Gábor Dénes")
    # 3 autó hozzáadása
    auto1 = Szemelyauto("ABC-123", "Tesla Model Y", 15000)
    auto2 = Teherauto("DEF-456", "Ford Transit", 12000)
    auto3 = Szemelyauto("GHI-789", "Volkswagen Golf", 9000)
    kolcsonzo.auto_hozzaadas(auto1)
    kolcsonzo.auto_hozzaadas(auto2)
    kolcsonzo.auto_hozzaadas(auto3)
    # 4 fiktív bérlés felvétele (ebből néhány már lezárt)
    today = date.today()
    # Múltbeli bérlések hozzáadása
    berles1 = Berles(auto1, today - timedelta(days=4))
    berles1.aktiv = False
    kolcsonzo.berlesek.append(berles1)
    berles2 = Berles(auto2, today - timedelta(days=3))
    berles2.aktiv = False
    kolcsonzo.berlesek.append(berles2)
    # Aktuális (mai napos) bérlések
    kolcsonzo.berlesek.append(Berles(auto2, today))
    kolcsonzo.berlesek.append(Berles(auto3, today))
    # (auto2 és auto3 jelenleg bérbe vannak adva, auto1 szabad)

    # Konzolos menü
    while True:
        print(f"\n---- {kolcsonzo.nev} autókölcsönző rendszer ----")
        print("1. Autók listázása")
        print("2. Autó kölcsönzése")
        print("3. Bérlés lemondása")
        print("4. Aktuális bérlések listázása")
        print("0. Kilépés")
        try:
            valasz = int(input("Válasszon egy menüpontot: "))
        except ValueError:
            print("Nem érvényes válasz. Kérem, adjon meg egy számot.")
            continue

        if valasz == 1:
            print("\nAz autók listája:")
            for auto in kolcsonzo.lista_autok():
                status = "szabad" if kolcsonzo.auto_elerheto(
                    auto.rendszam) else "kölcsönözve"
                print(
                    f"- {auto.rendszam} - {auto.tipus} ({auto.berleti_dij} Ft/nap) - {status}")
        elif valasz == 2:
            rendszam = input("Adja meg a bérelni kívánt autó rendszámát: ")
            if kolcsonzo.berel_auto(rendszam):
                print("Sikeresen kibérelte az autót!")
            else:
                # Meghatározzuk a sikertelenség okát
                auto_exists = any(
                    auto.rendszam == rendszam for auto in kolcsonzo.autok)
                if not auto_exists:
                    print("Nincs ilyen rendszámú autó a kölcsönzőben!")
                else:
                    print("Az autó jelenleg nem elérhető (már ki van bérelve).")
        elif valasz == 3:
            rendszam = input(
                "Adja meg a lemondani kívánt bérlés autójának rendszámát: ")
            # Először ellenőrizzük, hogy létezik-e ilyen autó
            auto_exists = any(
                auto.rendszam == rendszam for auto in kolcsonzo.autok)
            if not auto_exists:
                print("Nincs ilyen autó a kölcsönzőben!")
            else:
                if kolcsonzo.lemond_berles(rendszam):
                    print("A bérlést sikeresen lemondta.")
                else:
                    print("Ez az autó jelenleg nincs bérbe adva.")
        elif valasz == 4:
            aktiv_berlesek = kolcsonzo.aktualis_berlesek()
            if not aktiv_berlesek:
                print("Jelenleg nincs aktív bérlés.")
            else:
                print("\nAktuális bérlések:")
                for berles in aktiv_berlesek:
                    print(
                        f"- {berles.auto.rendszam} - {berles.auto.tipus}, bérlés dátuma: {berles.datum}")
        elif valasz == 0:
            print("Kilépés a programból. Viszontlátásra!")
            break
        else:
            print("Nem létező menüpont.")


if __name__ == "__main__":
    main()
