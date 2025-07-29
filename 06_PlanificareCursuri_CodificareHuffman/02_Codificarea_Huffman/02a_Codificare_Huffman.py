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

class NodHuffman:
    def __init__(self, simbol, frecventa):
        self.simbol = simbol
        self.frecventa = frecventa
        self.st = None
        self.dr = None
    def __lt__(self, alt):
        return self.frecventa < alt.frecventa

def sorteaza(lista): # sortez crescător după frecvență (bubble sort)
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].frecventa > lista[j + 1].frecventa:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def huffman(frecvente):
    heap = []
    for simbol, frecventa in frecvente.items():
        heap.append(NodHuffman(simbol, frecventa))

    sorteaza(heap)

    while len(heap) > 1:
        # extrag primele 2 cele mai mici noduri ca frecvență
        st = heap.pop(0)
        dr = heap.pop(0)
        nod_intermediar = NodHuffman(None, st.frecventa + dr.frecventa)
        nod_intermediar.st = st
        nod_intermediar.dr = dr
        heap.append(nod_intermediar)  # adaug noul nod intermediar înapoi în listă
        sorteaza(heap)                # sortez iar

    return heap[0]

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


text = input("Introduceți textul: ")
# 1. Frecvența fiecărui caracter
frecvente_char ={}
for char in text:
    if char not in frecvente_char:
        frecvente_char[char] = 1
    else:
        frecvente_char[char] += 1
print(f"Frecvențe: {frecvente_char}")

# 2. Arborele Huffman
arbore = huffman(frecvente_char)

# 3. Afișarea codurilor binare asociate fiecărui caracter
codurile_binare = genereaza_coduri(arbore)
print(f"Coduri Huffman: {codurile_binare}")
