#dalmatienii
for i in range(1,102):
    print(f'Damatianul cu nr {i}')

#dalmatienii din 2 in 2
for i in range(1,102,2):
    print(f'Damatianul cu nr {i}')

#parcurgere lista cu for prin INDEX - i ia valoarea indexului din range. Nu a numarului. Cu numere[i] adica numere[0] - vedem 3 de ex.
numere=[3,7,10,20,30] # de ex cand nu stii lista. SI TE FOLOSESTI DE INDEX
for i in  range(0, len(numere)):
    print(f'Indexul curent este {i}')
    print(f'Numarul curent este {numere[i]}')

#for each - Aici i(numar) ia valoarea fiecarui numar din lista. Mai sus ia valoarea indexului din Range ul dat, iar ca sa vedem numarul cerem numere[i] - adica numere de index
s=0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s=s+numar
print(f'Suma este {s}')

for i in numere:
    print (f'Numar curent este {i}')

#de cate ori apare 3 in [3,2,3,5,3] Tema!

lista=[3,2,3,5,3] # metoda cu FOR (for each)
apare=1
for i in lista:
    if(i==3):
        print(f'Numarul 3 apare de {apare} dati')
        apare=apare+1

lista = [3,2,3,5,3] # medota cu lista lista.count(3)
print('Numarul 3 apare de ', lista.count(3), ' ori.')