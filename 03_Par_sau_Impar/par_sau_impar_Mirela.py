import random

# Variabile
scor_user = 0
scor_pc = 0
runda_totala = 0
victorii_user_consecutive = 0
victorii_pc_consecutive = 0

# FUNCȚII accesate în partea principală a programului
# Funcția pt alegerea "par" sau "impar"
def alege_par_impar():
    alegere = input("Alegi 'par' sau 'impar'? ").strip().lower() # elimină spațiile și transformă în litere mici
    while alegere not in ['par', 'impar']:
        alegere = input("Te rog alege doar 'par' sau 'impar': ").strip().lower()
    return alegere

# Funcție pt introducerea unui număr între 0 și 10
def introdu_numar():
    raspuns = input("Scrie un număr între 0 și 10: ")
    while not raspuns.isdigit() or int(raspuns) < 0 or int(raspuns) > 10:
        print("Numărul nu este valid.")
        raspuns = input("Scrie din nou un număr între 0 și 10: ")
    return int(raspuns)

# Funcție care calculează suma
def calculeaza_suma(num1, num2):
    return num1 + num2

# Funcție care verifică dacă un număr este par
def este_par(numar):
    return numar % 2 == 0

# Funcție care verifică dacă utilizatorul a câștigat
def verifica_castigator(alegere, rezultat):
    return alegere == rezultat

# Funcție care afișează scorul curent
def afiseaza_scor(scor_user, scor_pc, runda):
    print("\nScor după", runda, "runde:")
    print("Tu:", scor_user)
    print("Calculatorul:", scor_pc)


# Partea principală
while True:
    print("\n*** Runda", runda_totala + 1, "***")

    alegere = alege_par_impar()
    numar_user = introdu_numar()
    numar_pc = random.randint(0, 10)
    print("Calculatorul a ales:", numar_pc)

    suma = calculeaza_suma(numar_user, numar_pc)
    print("Suma este:", suma)

    if este_par(suma):
        rezultat = "par"
    else:
        rezultat = "impar"

    print("Suma este număr", rezultat + ".")

    if verifica_castigator(alegere, rezultat):
        print("Ai câștigat runda!")
        scor_user += 1
        victorii_user_consecutive += 1
        victorii_pc_consecutive = 0

        # Victorii consecutive: mesaje pentru user
        if victorii_user_consecutive == 2:
            print("Ai câștigat 2 runde la rând!")
        elif victorii_user_consecutive == 3:
            print("3 runde consecutive! Bravo!")
        elif victorii_user_consecutive > 3:
            print("Wow, ești de neoprit! Ai", victorii_user_consecutive, "victorii consecutive!")
    else:
        print("Calculatorul a câștigat runda.")
        scor_pc += 1
        victorii_user_consecutive = 0
        victorii_pc_consecutive += 1

        # Victorii consecutive: mesaje pentru calculator
        if victorii_pc_consecutive == 2:
            print("Calculatorul a câștigat 2 runde consecutiv.")
        elif victorii_pc_consecutive == 3:
            print("Calculatorul are 3 victorii consecutive!")
        elif victorii_pc_consecutive > 3:
            print("Calculatorul are", victorii_pc_consecutive, "victorii consecutive.")

    runda_totala += 1

    # Mesaj special pentru scor 3–0
    if scor_user == 3 and scor_pc == 0:
        print("Conduci cu 3-0! Super început!")
    elif scor_pc == 3 and scor_user == 0:
        print("Calculatorul conduce cu 3-0! Concentrează-te!")

    # Întreabă dacă mai vrei să joci
    raspuns = input("Vrei să joci din nou? (da / nu): ").strip().lower()
    while raspuns != "da" and raspuns != "nu":
        raspuns = input("Te rog, scrie 'da' sau 'nu': ").strip().lower()
    if raspuns == "nu":
        break

# Partea finală
afiseaza_scor(scor_user, scor_pc, runda_totala)

if scor_user > scor_pc:
    print("Felicitări! Ai câștigat jocul final!")
elif scor_user < scor_pc:
    print("Calculatorul a câștigat jocul final. Mai încearcă!")
else:
    print("Este egalitate!")