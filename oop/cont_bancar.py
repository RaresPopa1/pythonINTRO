#aici definim

class contBancar:
    #constructorul
    def __init__(self,titularCont, iban): #self e ca this in java
        #atribute
        self.titularCont = titularCont
        self.iban=iban
        self.sold = 0
        self.activ=False
        self.pin=7777
        self.incercariActivare=0

    def salut(self):
        print(f'Buna {self.titularCont}')

    def interogareSold(self):
        self.salut()
        print(f'Titular {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Nr incercari {self.incercariActivare}')
        print('-----------------------------------')

    def activareCont(self, pinUtilizator):
        if pinUtilizator == self.pin:
            print('Card activat!')
            self.activ=True
        else:
            print('Pin Gresit!')
            self.incercariActivare=self.incercariActivare+1
            #self.incercariActivare+=1

    def alimentareCont(self, suma):
        self.sold+=suma
        print(f'Ati alimentat {suma}')
        print(f'Aveti in cont {self.sold}')

    def plataCard(self, suma):
        #variabile scope
        if suma<=self.sold:
            self.sold-=suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente!')





