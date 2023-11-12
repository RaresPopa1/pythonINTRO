'''
Variabila = Zona din memoria calc care tine date
Variabila = cutiuta in care punem valori
'''

#am declarat si initializat variabila marca
marca_masina = 'Volvo'
model_masina = 'XC 60'

#nu putem sa punem spatiu in numele variabilei
#incepe cu litera mica
#loosely typed - nu trebuie sa specificam tipurile
#aici nu avem ; la finalul prop.

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

# Suprascriere
model_masina = 'XC 60 facelift'

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

nume= 'Popa'
prenume= 'Rares'
varsta = 23
print(f'Proprietarul este: {nume} {prenume} si in varsta de {varsta}')