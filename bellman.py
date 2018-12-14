from copy import deepcopy
import math

f = open("mapa.txt","r")

rozmiarmapy = []
mapatypow = []
mapakosztow = []
gama = 0.5
V = []
Vstary = []
listaruchow = []
politykaruchu = []



for word in f.readline().split():
    rozmiarmapy.append(int(word))

print(rozmiarmapy)

for wiersz in range(rozmiarmapy[1] ):
    politykaruchu.append([0])
    for kolumna in range(rozmiarmapy[0] - 1):
        politykaruchu[wiersz].append(0)
print (politykaruchu)



for linia in range(rozmiarmapy[1]):
    mapatypow.append(f.readline().split())
f.readline()
for lanes in f.readlines():
    mapakosztow.append(lanes.split())

for i in range(rozmiarmapy[1]):
    for j in range(rozmiarmapy[0]):
        mapatypow[i][j] = int(mapatypow[i][j])

for i in range(rozmiarmapy[1]):
    for j in range(rozmiarmapy[0]):
        mapakosztow[i][j] = int(mapakosztow[i][j])

V = deepcopy(mapakosztow)
for przejscie in range(100):
    Vstary = deepcopy(V)
    roznice = []

    for wiersz in range(rozmiarmapy[1]):
        for kolumna in range(rozmiarmapy[0]):
            if mapatypow[wiersz][kolumna] == 1:
                print(wiersz, kolumna)
                #licze akcje ruch do góry
                if wiersz == 0 or mapatypow[wiersz-1][kolumna] == 0:
                    ruch_do_gory = 0.8 * Vstary[wiersz][kolumna]
                else:
                    ruch_do_gory = 0.8 * Vstary[wiersz-1][kolumna]
                if kolumna == 0 or mapatypow[wiersz][kolumna-1] == 0:
                    przemieszczenie_w_lewo = 0.1 * Vstary[wiersz][kolumna]
                else:
                    przemieszczenie_w_lewo = 0.1 * Vstary[wiersz][kolumna-1]
                if kolumna == rozmiarmapy[0]-1 or mapatypow[wiersz][kolumna+1] == 0:
                    przemieszczenie_w_prawo = 0.1 * Vstary[wiersz][kolumna]
                else:
                    przemieszczenie_w_prawo = 0.1 * Vstary[wiersz][kolumna + 1]
                akcja_gora = ruch_do_gory + przemieszczenie_w_lewo + przemieszczenie_w_prawo
                #print(akcja_gora)
                #licze akcje ruch w prawo
                if kolumna == rozmiarmapy[0]-1 or mapatypow[wiersz][kolumna + 1] == 0:
                    ruch_w_prawo = 0.8 * Vstary[wiersz][kolumna]
                else:
                    ruch_w_prawo = 0.8 * Vstary[wiersz][kolumna + 1]
                if wiersz == 0 or mapatypow[wiersz - 1][kolumna] == 0:
                    przemieszczenie_w_gore = 0.1 * Vstary[wiersz][kolumna]
                else:
                    przemieszczenie_w_gore = 0.1 * Vstary[wiersz - 1][kolumna]
                if wiersz == rozmiarmapy[1]-1 or mapatypow[wiersz + 1][kolumna] == 0:
                    przemieszczenie_w_dol = 0.1 * Vstary[wiersz][kolumna]
                else:
                    przemieszczenie_w_dol = 0.1 * Vstary[wiersz + 1][kolumna]
                akcja_prawo = ruch_w_prawo + przemieszczenie_w_gore + przemieszczenie_w_dol
                #print(akcja_prawo)
                #licze akcje ruchu w dół
                if wiersz == rozmiarmapy[1]-1 or mapatypow[wiersz + 1][kolumna] == 0:
                    ruch_w_dol = 0.8 * Vstary[wiersz][kolumna]
                else:
                    ruch_w_dol = 0.8 * Vstary[wiersz + 1][kolumna]
                if kolumna == 0 or mapatypow[wiersz][kolumna - 1] == 0:
                    przemieszczenie_w_lewo = 0.1 * Vstary[wiersz][kolumna]
                else:
                    przemieszczenie_w_lewo = 0.1 * Vstary[wiersz][kolumna - 1]
                if kolumna == rozmiarmapy[0]-1 or mapatypow[wiersz][kolumna + 1] == 0:
                    przemieszczenie_w_prawo = 0.1 * Vstary[wiersz][kolumna]
                else:
                    przemieszczenie_w_prawo = 0.1 * Vstary[wiersz][kolumna + 1]
                akcja_dol = ruch_w_dol + przemieszczenie_w_lewo + przemieszczenie_w_prawo
                #print(akcja_dol)
                #licze akcje w lewo
                if kolumna == 0 or mapatypow[wiersz][kolumna - 1] == 0:
                    ruch_w_lewo = 0.8 * Vstary[wiersz][kolumna]
                else:
                    ruch_w_lewo = 0.8 * Vstary[wiersz][kolumna - 1]
                if wiersz == 0 or mapatypow[wiersz - 1][kolumna] == 0:
                    przemieszczenie_w_gore = 0.1 * Vstary[wiersz][kolumna]
                else:
                    przemieszczenie_w_gore = 0.1 * Vstary[wiersz - 1][kolumna]
                if wiersz == rozmiarmapy[1]-1 or mapatypow[wiersz + 1][kolumna] == 0:
                    przemieszczenie_w_dol = 0.1 * Vstary[wiersz][kolumna]
                else:
                    przemieszczenie_w_dol = 0.1 * Vstary[wiersz + 1][kolumna]
                akcja_lewo = ruch_w_lewo + przemieszczenie_w_gore + przemieszczenie_w_dol
                #print(akcja_lewo)
                #wybieranie najepszej akcji
                if akcja_gora > akcja_prawo:
                    najlepsza_akcja = akcja_gora
                else:
                    najlepsza_akcja = akcja_prawo
                if najlepsza_akcja < akcja_dol:
                    najlepsza_akcja = akcja_dol
                if najlepsza_akcja < akcja_lewo:
                    najlepsza_akcja = akcja_lewo
                #Ustalanie najlepszej polityki ruchu
                if najlepsza_akcja == akcja_gora:
                    politykaruchu[wiersz][kolumna] = 1
                elif najlepsza_akcja == akcja_prawo:
                    politykaruchu[wiersz][kolumna] = 2
                elif najlepsza_akcja == akcja_dol:
                    politykaruchu[wiersz][kolumna] = 3
                elif najlepsza_akcja == akcja_lewo:
                    politykaruchu[wiersz][kolumna] = 4
                V[wiersz][kolumna] = mapakosztow[wiersz][kolumna] + gama * najlepsza_akcja

    for wartosci in range(rozmiarmapy[1]):
        for kolumna in range(rozmiarmapy[0] - 1):
            roznice.append(Vstary[wartosci][kolumna] - V[wartosci][kolumna])
    minimalna = math.fabs(min(roznice))
    if minimalna < 0.0001:
        print(przejscie)
        break







print(mapatypow)
print(mapakosztow)
print(politykaruchu)
print(V)
