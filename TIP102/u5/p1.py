class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []


apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name) # Apolio
print(apollo.species) # Eagle
print(apollo.catchphrase) #pah
print(apollo.furniture) #[]