def printGreeting():
    print("Buna ziua! Bine ati venit!")

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

def mediaNr(a,b,c):
    return (a+b+c)/3

def piValue():
   return 3.14

#ex: daca pers e majora, altfel flase
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False

#-------ZONA DE APELARE-------
printGreeting()
printGreetingByName('Rares', 'Popa')
print(mediaNr(3,3,4))
print(piValue())
print(verificareMajor(17))

#se ia varsta utilizator
age=int(input('Introduceti varsta dvs '))
if verificareMajor(age):
    print('Cont creat. Bine ai venit!')
else:
    print('Nu ai varsta minima necesara!')