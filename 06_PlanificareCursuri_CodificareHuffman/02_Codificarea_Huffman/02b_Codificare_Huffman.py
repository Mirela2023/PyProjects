""" Problema 2: Codificare Huffman
Se dă un text. Vrem să-l codificăm cât mai eficient, folosind algoritmul Huffman.
Scrie un program care:
1. Calculează frecvența fiecărui caracter.
2. Construiește arborele Huffman.
3. Afișează codul binar asociat fiecărui caracter.

Exemplu input: text = "aabacabad"
Exemplu output: {'b': '00', 'c': '010', 'd': '011', 'a': '1'}

Indicație:
Folosește o structură de tip heap și creează un arbore binar de codificare.
- Nu se folosesc biblioteci externe, doar Python standard. """

import heapq
from collections import Counter

# Nodul din arborele Huffman
class NodHuffman:
    def __init__(self, simbol, frecventa):
        self.simbol = simbol
        self.frecventa = frecventa
        self.st = None
        self.dr = None
    def __lt__(self, alt):
        return self.frecventa < alt.frecventa

# Determină frecvența caracterelor din textul introdus
def determinare_frecvente(input_text):
    if not input_text:
        return {}
    else:
        frecv = Counter(input_text)
        return frecv

# Construiește arborele Huffman
def huffman(frecvente):
    heap = [NodHuffman(simbol, frec) for simbol, frec in frecvente.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        st = heapq.heappop(heap)
        dr = heapq.heappop(heap)
        nod_nou = NodHuffman(None, st.frecventa + dr.frecventa)
        nod_nou.st = st
        nod_nou.dr = dr
        heapq.heappush(heap, nod_nou)
    return heap[0] # rădăcina arborelui

# Generează codurile binare parcurgând arborele
def genereaza_coduri(nod, cod="", coduri=None):
    if coduri is None:
        coduri = {}
    if nod is None:
        return coduri
    if nod.simbol is not None:
        coduri[nod.simbol] = cod
    genereaza_coduri(nod.st, cod + "0", coduri)
    genereaza_coduri(nod.dr, cod + "1", coduri)
    return coduri

# Execuție
text = input("Introduceți textul: ")
# 1. Frecvența fiecărui caracter
frecvente_char =determinare_frecvente(text)
print(f"Frecvențe: {dict(frecvente_char)}")

# 2. Arborele Huffman
arbore = huffman(frecvente_char)

# 3. Afișarea codurilor binare asociate fiecărui caracter
codurile_binare = genereaza_coduri(arbore)
print(f"Coduri Huffman: {codurile_binare}")
