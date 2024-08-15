voted = {}
print(voted)

def verifica_eleitor(nome):
    if voted.get(nome):
        print("Liberado!")
    else:
        voted[nome] = True
        print("Precisa votar!")

verifica_eleitor("Clark")
verifica_eleitor("Clark")
verifica_eleitor("Cris")
verifica_eleitor("Clark")
verifica_eleitor("Cris")

print(voted)