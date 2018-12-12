from copy import deepcopy

f = open("mapa.txt","r")

rozmiarmapy = []
mapatypow = []
mapakosztow = []
gama = 0.5
V = []
Vstary = []
listaruchow = []

for word in f.readline().split():
    rozmiarmapy.append(int(word))

print(rozmiarmapy)

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

for przejscie in range(1):
    Vstary = deepcopy(V)
    for wiersz in range(rozmiarmapy[1]):
        for kolumna in range(rozmiarmapy[0]):
            if mapatypow[wiersz][kolumna] == 1:
                print(wiersz, kolumna)
                #licze ruch do góry
                if wiersz == 0 or mapatypow[wiersz-1][kolumna] == 0:
                    ruch_do_gory = 0.8 * Vstary[wiersz][kolumna]
                else:
                    ruch_do_gory = 0.8 * Vstary[wiersz-1][kolumna]
                if kolumna == 0 or mapatypow[wiersz][kolumna-1] == 0:
                    przemieszczenia_w_lewo = 0.1 * Vstary[wiersz][kolumna]
                else:
                    przemieszczenia_w_lewo = 0.1 * Vstary[wiersz][kolumna-1]
                if kolumna == rozmiarmapy[0]-1 or mapatypow[wiersz][kolumna+1] == 0:
                    przemieszczenia_w_prawo = 0.1 * Vstary[wiersz][kolumna]
                else:
                    przemieszczenia_w_prawo = 0.1 * Vstary[wiersz][kolumna + 1]
                akcja_gora = ruch_do_gory + przemieszczenia_w_lewo + przemieszczenia_w_prawo
                print(akcja_gora)




print(mapatypow)
print(mapakosztow)

