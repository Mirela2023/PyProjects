### Șirul lui Fibonacci

Scrie un program care calculează al n-lea element din șirul lui Fibonacci. Șirul este definit astfel:\
• F(0) = 0\
• F(1) = 1\
• F(n) = F(n-1) + F(n-2), pentru n ≥ 2

Rezolvă problema în 3 pași:\
*1. Metoda rudimentară*\
Folosește doar variabile, condiții și o buclă pentru a obține rezultatul.\
Programul trebuie să pornească de la F(0) = 0 și F(1) = 1 și să continue până la F(n), unde n este o valoare dată în cod.

*2. Backtracking*\
Sugestie: poți folosi un dicționar sau o listă pentru a stoca rezultatele deja obținute.

*3. Cu bibliotecă Python*\
Folosește o funcție gata făcută dintr-o bibliotecă Python pentru a calcula Fibonacci.\
• functools.lru_cache aplicat peste funcția recursivă\
• sympy.fibonacci(n) din biblioteca SymPy\
• orice altă soluție Python care returnează rapid F(n)

*Exemplu de test:*\
Pentru n = 10, rezultatul trebuie să fie 55.
