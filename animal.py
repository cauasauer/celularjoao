class Animal():
    quantiade_pata = 4
    tem_rabo = False
    tem_pelo = True
    especie = ''

class Cachorro(Animal):
    tem_pelo = True
    especie = 'Canis Lupus Familiaris'
    raca = 'Shitzu'
    nome = 'Sérgio'
    porte = 'Pequeno'
    sexo = 'transforme'

    def latir():
        return 'AUAUAUAUAUAUAUAUAUAUAAUAUAU'
    
    def comer():
        return 'mamamamamam'
    
    def dormir():
        return 'ZZZZZZZZZZZ'

print(Cachorro.comer)
print(Cachorro.dormir)
print(Cachorro.latir)
print(Cachorro.especie)
print(Cachorro.nome)
print(Cachorro.quantiade_pata)
print(Cachorro.porte)
print(Cachorro.raca)
print(Cachorro.sexo)
print(Cachorro.tem_pelo)
print(Cachorro.tem_rabo)
