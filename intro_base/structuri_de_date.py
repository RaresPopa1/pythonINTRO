# listele in phyton pot cuprinde elemente de tipuri diferite
# au dimensiune dinamica

fructe = ['mar', 'bnn', 'portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un nou element !!!!!
fructe.append('struguri')

#suprascriem un element
fructe[1]='para'

#afisam lista iar
print(fructe)

#aflam dimensiunea!!!!
print(len(fructe))

#scoate && ne da ult element!!!!
last = fructe.pop()
print('ultimul element: ',last)
print('lista: ',fructe)

#de cate ori apare un element?
print('3 apare de: ', fructe.count(3), ' ori')

#extinem lista !!!!
fructe_exotice=['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)



