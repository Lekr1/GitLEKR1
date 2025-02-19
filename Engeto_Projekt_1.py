"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lenka Krylová
email: l.krylova@centrum.cz
"""

# Přihlášení pomocí uživatelského jména a hesla
uzivatele = [
    {"jmeno": "Bob", "heslo": "123"},
    {"jmeno": "Ann", "heslo": "pass123"},
    {"jmeno": "Mike", "heslo": "password123"},
    {"jmeno": "Liz", "heslo": "pass123"}
    ]

prihlasovaci_jmeno = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")

for uzivatel in uzivatele:
    if uzivatel['jmeno'] == prihlasovaci_jmeno and uzivatel['heslo'] == heslo:
        print("-" * 20, "\nVítejte v aplikaci, {}!".format(uzivatel["jmeno"]))
        break
else:
    print("Nejste registrovaný uživatel")
    exit()

import string

# Seznam textů
TEXTS = [
    "Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US and the Union Pacific Railroad, which traverse the valley.", 
    "At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.",
    "The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present."
]

# Vyžádání čísla textu od uživatele
print("Máme k dispozici 3 texty k analýze. Vyberte číslo od 1 do 3.")
vyber = input("Zadejte číslo textu (1, 2 nebo 3): ").strip()

# Kontrola vstupu
if not vyber.isdigit() or int(vyber) not in range(1, 4):
    print("Neplatný vstup! Zadejte číslo od 1 do 3.")
    exit()

# Výběr textu
vyber = int(vyber)
vybrany_text = TEXTS[vyber - 1]

# Příprava textu
slova = vybrany_text.split()
cista_slova = [slovo.strip(string.punctuation) for slovo in slova]  # Odstranění interpunkce

# Počítání statistik
pocet_slov = len(cista_slova)
velka_pismena_zacatek = sum(1 for slovo in cista_slova if slovo.istitle())
velka_pismena = sum(1 for slovo in cista_slova if slovo.isupper())
mala_pismena = sum(1 for slovo in cista_slova if slovo.islower())
pocet_cisel = sum(1 for slovo in cista_slova if slovo.isdigit())
suma_cisel = sum(int(slovo) for slovo in cista_slova if slovo.isdigit())

# Zobrazení statistik
print("-" * 30)
print(f"Počet slov: {pocet_slov}")
print(f"Počet slov začínajících velkým písmenem: {velka_pismena_zacatek}")
print(f"Počet slov psaných VELKÝMI písmeny: {velka_pismena}")
print(f"Počet slov psaných malými písmeny: {mala_pismena}")
print(f"Počet čísel: {pocet_cisel}")
print(f"Suma všech čísel: {suma_cisel}")

# Vytvoření sloupcového grafu četnosti délek slov
delky_slov = [len(slovo) for slovo in cista_slova]
cetnost_delek = {}

for delka in delky_slov:
    cetnost_delek[delka] = cetnost_delek.get(delka, 0) + 1

print("\nSloupcový graf četnosti délek slov:")
for delka, cetnost in sorted(cetnost_delek.items()):
    print(f"{delka}| {'*' * cetnost} | {cetnost}")