# Flow control - if else
# evalueaza conditii si bifurca codul in functie de rezultat

piesa_faina=True

print('Pornim radio')
if piesa_faina == True:
    print('Dam mai tare')
    print('Fredonam')
print('Oprim radio')

#if else
# daca numarul este par printam acest lucru
# altfel printam impar
nr = 4
if nr%2==0:
    print('Par')
else: print('Impar')

#este un nr pozitiv?
if(nr>0):
    print('pozitiv')
else: print('nu este pozitiv')

#if, else if, else
# cum ne saluta in functie de ora?
#citim date de la tastatura si ne asiguram ca sunt transformate din string in int.
ora = int(input('Introdu ora '))
if ora < 0: print('ora negativa')
elif ora <= 11: print('Buna dimineata!')
elif ora <= 18: print('Buna ziua!')
elif ora <= 21: print('Buna seara!')
elif ora <= 24: print('Noapte buna!')
else: print('ora prea mare')

#ctrl+/ ca sa excluzi linii de cod mai multe

#robotel telefonic
optiune = int(input('alege o optiune'))
if optiune==0: print('meniu anterior')
elif optiune==1: print('ati ales romana')
elif optiune==2: print('ati ales engleza')
else: print('nu am identificat optiunea, mai incearca')