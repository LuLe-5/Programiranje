'''
moja_lista = []
moja_lista.append(10)
moja_lista.append(20)
moja_lista.append(30)

print(moja_lista)

print(moja_lista[1])

print(moja_lista[1:4])

print(moja_lista[0:2])

moja_lista.remove(20)

print(moja_lista)



moja_lista = []
moja_lista.append('Jabuka')
moja_lista.append('Banana')
moja_lista.append('Kruška')
moja_lista.append('Naranča')

print(moja_lista)
print(moja_lista[0])



# Ovo je 2D lista (3 retka, 3 stupca)
ormar = [
    ['majica', 'kapa', 'sal'],    # 0. redak (polica)
    ['hlace', 'carape', 'remen'], # 1. redak
    ['jakna', 'cipele', 'cizme']  # 2. redak
]


for redak in ormar:
    print(redak[1])
'''
def pronadji_broj (lista, trazeni_broj):
    for broj in lista:
        if broj == trazeni_broj:
            provjera = True
        else:
            provjera = False

    if provjera:
        print(f"Broj {trazeni_broj} je na listi")
    else:
        print(f"Broj {trazeni_broj} nije na listi")

provjera = False

lista_brojeva = [10, 20, 30, 40, 50]
trazeni_broj = 30

pronadji_broj(lista_brojeva, trazeni_broj)


