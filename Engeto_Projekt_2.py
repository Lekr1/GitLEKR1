"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lenka Krylová
email: l.krylova@centrum.cz
"""

import random

def pozdrav_hrace():
    print("Ahoj hráči!")
    print("Vítej ve hře Bulls and Cows.")
    print("Vaším úkolem je uhodnout čtyřmístné číslo, kde každá číslice je unikátní a číslo nezačíná nulou.")

def vygeneruj_tajne_cislo():
    cislice = list(range(1, 10))  # První číslice nemůže být nula
    prvni_cislice = random.choice(cislice)
    cislice.remove(prvni_cislice)
    zbytek = random.sample(cislice + [0], 3)  # Zbývající čísla mohou obsahovat nulu
    tajne_cislo = [prvni_cislice] + zbytek
    return ''.join(map(str, tajne_cislo))

def validuj_vstup(vstup):
    if not vstup.isdigit():
        return "Vstup musí obsahovat pouze číslice."
    if len(vstup) != 4:
        return "Vstup musí být čtyřmístné číslo."
    if vstup[0] == '0':
        return "Číslo nesmí začínat nulou."
    if len(set(vstup)) != 4:
        return "Číslo nesmí obsahovat duplicitní číslice."
    return None

def vypocitej_bulls_a_cows(tip, tajne_cislo):
    bulls = sum(1 for a, b in zip(tip, tajne_cislo) if a == b)
    cows = sum(1 for c in tip if c in tajne_cislo) - bulls
    return bulls, cows

def jednotne_mnozne_cislo(pocet, jednotka):
    if pocet == 1:
        return f"{pocet} {jednotka}"
    else:
        return f"{pocet} {jednotka}s"

def hra():
    pozdrav_hrace()
    tajne_cislo = vygeneruj_tajne_cislo()
    # Debug: Odkomentujte následující řádek pro zobrazení tajného čísla během vývoje
    # print(f"[DEBUG] Tajné číslo: {tajne_cislo}")

    while True:
        tip = input("Zadejte svůj tip (čtyřmístné číslo): ")
        chyba = validuj_vstup(tip)
        if chyba:
            print(f"Chyba: {chyba}")
            continue

        bulls, cows = vypocitej_bulls_a_cows(tip, tajne_cislo)
        print(f"Výsledek: {jednotne_mnozne_cislo(bulls, 'bull')}, {jednotne_mnozne_cislo(cows, 'cow')}")

        if bulls == 4:
            print("Gratuluji! Uhodli jste tajné číslo.")
            break

if __name__ == "__main__":
    hra()