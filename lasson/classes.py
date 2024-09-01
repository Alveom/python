class pokemon: 
    def __init__(self , name, level, hp, damage, defence, attack) -> None:
        self.name = name 
        self.level = level 
        self.hp = hp 
        self.damage = damage 
        self.defence = defence
        self.attack = attack 

    def nameHop(self):
        print(f' your attack {self.attack}')


    def PokemonInformationPrint(self):
         print(f'Your pokemon name is {self.name}. Your pokemon level is {self.level}. Your pokemon defence is {self.defence}')


def pokemonInformation():
    picacu = pokemon('Picacu', 35 , 120 , 65, 120, 25)
    picacu.PokemonInformationPrint()
    picacu.nameHop()

def main():
    pokemonInformation()


if __name__ == "__main__":
    main()