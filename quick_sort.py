import random

"""
Działa. Oto podsumowanie wszystkich zmian:

Linia 9 — zamieniono arytmetyczne (tab[idx1]-tab[idx2])*(tab[idx2]-tab[idx3])>=0 na porównanie łańcuchowe (tab[idx1] <= tab[idx2] <= tab[idx3]) or (...) — stringów nie można odejmować.
Linie 34–35 — dodano brakujący parametr limit do rekurencyjnych wywołań.
Linia 31 — zmieniono < limit na >= limit (warunek był odwrócony, uniemożliwiał jakąkolwiek rekurencję).
Linia 39 — poprawiono len(lst_-1) → len(lst_)-1.
"""

def Partition(tab, start, stop):
    idx1 = random.randint(start, stop-1)
    idx2 = random.randint(start, stop-1)
    idx3 = random.randint(start, stop-1)
    idx = idx1

    if (tab[idx1][0] <= tab[idx2][0] <= tab[idx3][0]) or (tab[idx3][0] <= tab[idx2][0] <= tab[idx1][0]):
        idx = idx2

    tab[idx], tab[stop] = tab[stop], tab[idx]
    pivot = tab[stop][0]
    j = start

    for i in range(start, stop):
        if tab[i][0] < pivot:
            tab[j], tab[i] = tab[i], tab[j]
            j += 1
        elif tab[i][0] == pivot:
            m = random.randint(0, 1)
            if m == 0:
                tab[j], tab[i] = tab[i], tab[j]
                j += 1
    
    tab[j], tab[stop] = tab[stop], tab[j]

    return j

def QuickSortR(tab, start, stop, limit) :
    if stop-start >= limit:
        pivot = Partition(tab, start, stop)

        QuickSortR(tab, start, pivot - 1, limit)
        QuickSortR(tab, pivot + 1, stop, limit)

if __name__ == "__main__":
    lst_ = [('fdsfs', 3), ('zffx', 1), ("ABCSD", 6)]
    QuickSortR(lst_, 0, len(lst_)-1, 1)
    print(lst_)