# declaram si initializam un dict (map)

#lista[]
#dict{}

note_elevi={'Gigel': 10,'Marcel': 9, 'Ana': 10}

#adaugam elemente
note_elevi['Sebi']=7

#printam dictul
print(note_elevi)

#aflam elemente
print('Nota lui Gigel: ', note_elevi['Gigel'])

#actualizam valori
note_elevi['Marcel']=10
print(note_elevi)

#aflam dimensiunea
print(len(note_elevi))

# stergem valori
note_elevi.pop('Marcel')
print(note_elevi)

#ne arata ce "KEY" avem in note_elevi
print(note_elevi.keys())