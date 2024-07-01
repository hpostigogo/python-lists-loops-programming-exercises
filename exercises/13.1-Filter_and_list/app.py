all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def nombre_r(nombre):
    return nombre[0]=='R'

resulting_names=list(filter(nombre_r,all_names))
print(resulting_names)




