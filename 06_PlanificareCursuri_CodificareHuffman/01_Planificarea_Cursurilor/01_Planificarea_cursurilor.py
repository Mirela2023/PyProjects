''' Problema 1: Planificarea cursurilor (Interval Scheduling)

Se dau mai multe intervale orare, fiecare reprezentând un curs [start, end].
Din cauza suprapunerilor, nu se pot ține toate cursurile.
Scrie un program care selectează cel mai mare număr de cursuri compatibile, adică fără suprapuneri.

Exemplu input: cursuri = [(9, 11), (10, 12), (13, 14), (11, 13), (12, 14)]

Exemplu output: [(9, 11), (11, 13), (13, 14)]

Indicație:
Folosește un algoritm greedy, sortând intervalele după ora de final.  '''

def interval_scheduling(intervale):
    intervale.sort(key=lambda x: x[1])  # sortare după final
    rezultat = []
    end_time = 0
    for inceput, sfarsit in intervale:
        if inceput >= end_time:
            rezultat.append((inceput, sfarsit))
            end_time = sfarsit
    return rezultat

print("--- PLANIFICAREA CURSURILOR ---")
cursuri = []
n = int(input("Câte cursuri doriți să introduceți? "))
for i in range(n):
    print(f"Introduceți intervalul orar pt Cursul {i+1}:")
    start = int(input("  Ora start: "))
    end = int(input("  Ora end: "))
    cursuri.append((start, end))

print(f"Lista cursurilor este: {cursuri}")

rezultat = interval_scheduling(cursuri)
print(f"Cursuri compatibile: {rezultat}")
