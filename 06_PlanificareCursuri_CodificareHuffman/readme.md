### *Planificarea cursurilor (Interval Scheduling) & Codificarea Huffman*
##### Deadline: 29.07.2025, ora 23:59

***Problema 1: Planificarea cursurilor (Interval Scheduling)***\
Se dau mai multe intervale orare, fiecare reprezentând un curs [start, end].\
Din cauza suprapunerilor, nu se pot ține toate cursurile.\
Scrie un program care selectează cel mai mare număr de cursuri compatibile, adică fără suprapuneri.

*Exemplu input:*  cursuri = [(9, 11), (10, 12), (13, 14), (11, 13), (12, 14)]

*Exemplu output:*  [(9, 11), (11, 13), (13, 14)]

Indicație:\
Folosește un algoritm greedy, sortând intervalele după ora de final.

----------------------------------
***Problema 2: Codificare Huffman***\
Se dă un text. Vrem să-l codificăm cât mai eficient, folosind algoritmul Huffman. Scrie un program care:
1. Calculează frecvența fiecărui caracter.
2. Construiește arborele Huffman.
3. Afișează codul binar asociat fiecărui caracter.

*Exemplu input:*  text = "aabacabad"

*Exemplu output:*  {'b': '00', 'c': '010', 'd': '011', 'a': '1'}

Indicație:\
Folosește o structură de tip heap și creează un arbore binar de codificare.\
Nu se folosesc biblioteci externe, doar Python standard.
