#aici rulam
from oop.cont_bancar import contBancar

cont1=contBancar('Rares Popa', 'RO001')
cont2=contBancar('Ioan Popa', 'RO002')

cont1.activareCont(7777)
cont1.alimentareCont(300)
cont1.plataCard(500)
cont1.interogareSold()


cont2.activareCont(3333)
cont2.activareCont(7777)

cont2.alimentareCont(700)

cont2.plataCard(100)
cont2.plataCard(400)

cont2.interogareSold()
