import random

class Pokemon:
    def __init__(self, name, hp, catch_rate, exp=0, level=1, evolution=None, moves=None):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.catch_rate = catch_rate
        self.exp = exp
        self.level = level
        self.evolution = evolution
        self.moves = moves if moves else []

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp}, Level: {self.level}, EXP: {self.exp})"

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.hp += 10
        self.max_hp += 10
        print(f"{self.name} leveled up to level {self.level}!")
        if self.evolution and self.level >= self.evolution['level']:
            self.evolve()

    def evolve(self):
        print(f"{self.name} is evolving!")
        self.name = self.evolution['name']
        self.hp += self.evolution['hp_increase']
        self.max_hp += self.evolution['hp_increase']
        print(f"{self.name} evolved!")

    def attack(self, other_pokemon):
        if not self.moves:
            print(f"{self.name} has no moves to attack with!")
            return False

        move = random.choice(self.moves)
        damage = random.randint(move['min_damage'], move['max_damage'])
        other_pokemon.hp -= damage
        print(f"{self.name} uses {move['name']} and attacks {other_pokemon.name} for {damage} damage!")
        if other_pokemon.hp <= 0:
            print(f"{other_pokemon.name} fainted!")
            return True
        return False

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def catch_pokemon(self, pokemon):
        if random.random() <= pokemon.catch_rate:
            self.pokemons.append(pokemon)
            print(f"{self.name} caught a {pokemon.name}!")
        else:
            print(f"{pokemon.name} escaped!")

    def show_pokemons(self):
        if self.pokemons:
            print(f"{self.name}'s Pokemons:")
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f"{self.name} has no Pokemons.")

    def heal_pokemons(self):
        for pokemon in self.pokemons:
            pokemon.hp = pokemon.max_hp
        print(f"All of {self.name}'s Pokemons have been healed!")

    def battle(self, wild_pokemon):
        if not self.pokemons:
            print("You have no Pokemons to battle with!")
            return

        my_pokemon = random.choice(self.pokemons)
        print(f"{my_pokemon.name} is battling {wild_pokemon.name}!")

        while my_pokemon.hp > 0 and wild_pokemon.hp > 0:
            action = input(f"Do you want {my_pokemon.name} to (a)ttack, (u)se a special move, or (r)un away? ").lower()
            if action == 'a':
                if my_pokemon.attack(wild_pokemon):
                    my_pokemon.gain_exp(990)
                    break
                if wild_pokemon.attack(my_pokemon):
                    print(f"{my_pokemon.name} lost the battle!")
                    break
            elif action == 'u':
                if not my_pokemon.moves:
                    print(f"{my_pokemon.name} has no special moves to use!")
                else:
                    move = random.choice(my_pokemon.moves)
                    damage = random.randint(move['min_damage'], move['max_damage']) * 1.5  # Special move does more damage
                    wild_pokemon.hp -= damage
                    print(f"{my_pokemon.name} uses special move {move['name']} and attacks {wild_pokemon.name} for {damage} damage!")
                    if wild_pokemon.hp <= 0:
                        print(f"{wild_pokemon.name} fainted!")
                        my_pokemon.gain_exp(990)
                        break
                    if wild_pokemon.attack(my_pokemon):
                        print(f"{my_pokemon.name} died in the battle!")
                        self.pokemons.remove(my_pokemon)
                        break
            elif action == 'r':
                print(f"{my_pokemon.name} ran away!")
                break
            else:
                print("Invalid action. Please choose again.")

        self.heal_pokemons()

def main():
    trainer_name = input("Enter your name: ")
    trainer = Trainer(trainer_name)

    wild_pokemons = [
      Pokemon("Bulbasaur", 45, 0.3, evolution={'name': 'Ivysaur', 'level': 16, 'hp_increase': 25}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Vine Whip', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Charmander", 39, 0.4, evolution={'name': 'Charmeleon', 'level': 16, 'hp_increase': 30}, moves=[{'name': 'Scratch', 'min_damage': 5, 'max_damage': 10}, {'name': 'Ember', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Squirtle", 44, 0.3, evolution={'name': 'Wartortle', 'level': 16, 'hp_increase': 25}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Water Gun', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Caterpie", 45, 0.2, evolution={'name': 'Metapod', 'level': 7, 'hp_increase': 20}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}]),
        Pokemon("Weedle", 40, 0.2, evolution={'name': 'Kakuna', 'level': 7, 'hp_increase': 20}, moves=[{'name': 'Poison Sting', 'min_damage': 5, 'max_damage': 10}]),
        Pokemon("Pidgey", 40, 0.3, evolution={'name': 'Pidgeotto', 'level': 18, 'hp_increase': 25}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Gust', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Rattata", 30, 0.4, evolution={'name': 'Raticate', 'level': 20, 'hp_increase': 30}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Quick Attack', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Spearow", 40, 0.3, evolution={'name': 'Fearow', 'level': 20, 'hp_increase': 30}, moves=[{'name': 'Peck', 'min_damage': 5, 'max_damage': 10}, {'name': 'Fury Attack', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Ekans", 35, 0.3, evolution={'name': 'Arbok', 'level': 22, 'hp_increase': 30}, moves=[{'name': 'Bite', 'min_damage': 10, 'max_damage': 15}, {'name': 'Poison Sting', 'min_damage': 5, 'max_damage': 10}]),
        Pokemon("Pikachu", 35, 0.4, evolution={'name': 'Raichu', 'level': 22, 'hp_increase': 30}, moves=[{'name': 'Thunder Shock', 'min_damage': 10, 'max_damage': 15}, {'name': 'Quick Attack', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Sandshrew", 50, 0.3, evolution={'name': 'Sandslash', 'level': 22, 'hp_increase': 30}, moves=[{'name': 'Scratch', 'min_damage': 5, 'max_damage': 10}, {'name': 'Slash', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Nidoran♀", 55, 0.3, evolution={'name': 'Nidorina', 'level': 16, 'hp_increase': 25}, moves=[{'name': 'Scratch', 'min_damage': 5, 'max_damage': 10}, {'name': 'Double Kick', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Nidoran♂", 46, 0.3, evolution={'name': 'Nidorino', 'level': 16, 'hp_increase': 25}, moves=[{'name': 'Peck', 'min_damage': 5, 'max_damage': 10}, {'name': 'Double Kick', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Clefairy", 70, 0.2, evolution={'name': 'Clefable', 'level': 22, 'hp_increase': 30}, moves=[{'name': 'Pound', 'min_damage': 5, 'max_damage': 10}, {'name': 'Double Slap', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Vulpix", 38, 0.3, evolution={'name': 'Ninetales', 'level': 22, 'hp_increase': 30}, moves=[{'name': 'Ember', 'min_damage': 10, 'max_damage': 15}, {'name': 'Quick Attack', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Jigglypuff", 115, 0.2, evolution={'name': 'Wigglytuff', 'level': 22, 'hp_increase': 30}, moves=[{'name': 'Pound', 'min_damage': 5, 'max_damage': 10}, {'name': 'Double Slap', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Zubat", 40, 0.3, evolution={'name': 'Golbat', 'level': 22, 'hp_increase': 30}, moves=[{'name': 'Leech Life', 'min_damage': 5, 'max_damage': 10}, {'name': 'Bite', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Oddish", 45, 0.3, evolution={'name': 'Gloom', 'level': 21, 'hp_increase': 25}, moves=[{'name': 'Absorb', 'min_damage': 5, 'max_damage': 10}, {'name': 'Acid', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Paras", 35, 0.3, evolution={'name': 'Parasect', 'level': 24, 'hp_increase': 30}, moves=[{'name': 'Scratch', 'min_damage': 5, 'max_damage': 10}, {'name': 'Leech Life', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Venonat", 60, 0.3, evolution={'name': 'Venomoth', 'level': 31, 'hp_increase': 35}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Poison Powder', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Diglett", 10, 0.4, evolution={'name': 'Dugtrio', 'level': 26, 'hp_increase': 20}, moves=[{'name': 'Scratch', 'min_damage': 5, 'max_damage': 10}, {'name': 'Mud-Slap', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Meowth", 40, 0.4, evolution={'name': 'Persian', 'level': 28, 'hp_increase': 30}, moves=[{'name': 'Scratch', 'min_damage': 5, 'max_damage': 10}, {'name': 'Bite', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Psyduck", 50, 0.3, evolution={'name': 'Golduck', 'level': 33, 'hp_increase': 35}, moves=[{'name': 'Scratch', 'min_damage': 5, 'max_damage': 10}, {'name': 'Water Gun', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Mankey", 40, 0.3, evolution={'name': 'Primeape', 'level': 28, 'hp_increase': 30}, moves=[{'name': 'Scratch', 'min_damage': 5, 'max_damage': 10}, {'name': 'Karate Chop', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Growlithe", 55, 0.3, evolution={'name': 'Arcanine', 'level': 30, 'hp_increase': 35}, moves=[{'name': 'Bite', 'min_damage': 10, 'max_damage': 15}, {'name': 'Ember', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Poliwag", 40, 0.3, evolution={'name': 'Poliwhirl', 'level': 25, 'hp_increase': 30}, moves=[{'name': 'Bubble', 'min_damage': 5, 'max_damage': 10}, {'name': 'Water Gun', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Abra", 25, 0.2, evolution={'name': 'Kadabra', 'level': 16, 'hp_increase': 25}, moves=[{'name': 'Teleport', 'min_damage': 0, 'max_damage': 0}]),
        Pokemon("Machop", 70, 0.3, evolution={'name': 'Machoke', 'level': 28, 'hp_increase': 30}, moves=[{'name': 'Karate Chop', 'min_damage': 10, 'max_damage': 15}, {'name': 'Low Kick', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Bellsprout", 50, 0.3, evolution={'name': 'Weepinbell', 'level': 21, 'hp_increase': 25}, moves=[{'name': 'Vine Whip', 'min_damage': 10, 'max_damage': 15}, {'name': 'Acid', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Tentacool", 40, 0.3, evolution={'name': 'Tentacruel', 'level': 30, 'hp_increase': 35}, moves=[{'name': 'Poison Sting', 'min_damage': 5, 'max_damage': 10}, {'name': 'Water Gun', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Geodude", 40, 0.3, evolution={'name': 'Graveler', 'level': 25, 'hp_increase': 30}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Rock Throw', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Ponyta", 50, 0.3, evolution={'name': 'Rapidash', 'level': 40, 'hp_increase': 40}, moves=[{'name': 'Ember', 'min_damage': 10, 'max_damage': 15}, {'name': 'Stomp', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Slowpoke", 90, 0.3, evolution={'name': 'Slowbro', 'level': 37, 'hp_increase': 35}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Water Gun', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Magnemite", 25, 0.3, evolution={'name': 'Magneton', 'level': 30, 'hp_increase': 30}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Thunder Shock', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Farfetch'd", 52, 0.3, evolution=None, moves=[{'name': 'Peck', 'min_damage': 5, 'max_damage': 10}, {'name': 'Slash', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Doduo", 35, 0.3, evolution={'name': 'Dodrio', 'level': 31, 'hp_increase': 35}, moves=[{'name': 'Peck', 'min_damage': 5, 'max_damage': 10}, {'name': 'Fury Attack', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Seel", 65, 0.3, evolution={'name': 'Dewgong', 'level': 34, 'hp_increase': 35}, moves=[{'name': 'Headbutt', 'min_damage': 10, 'max_damage': 15}, {'name': 'Aurora Beam', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Grimer", 80, 0.3, evolution={'name': 'Muk', 'level': 38, 'hp_increase': 35}, moves=[{'name': 'Pound', 'min_damage': 5, 'max_damage': 10}, {'name': 'Sludge', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Shellder", 30, 0.3, evolution={'name': 'Cloyster', 'level': 30, 'hp_increase': 30}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Ice Beam', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Gastly", 30, 0.3, evolution={'name': 'Haunter', 'level': 25, 'hp_increase': 30}, moves=[{'name': 'Lick', 'min_damage': 5, 'max_damage': 10}, {'name': 'Night Shade', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Onix", 35, 0.3, evolution=None, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Rock Throw', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Drowzee", 60, 0.3, evolution={'name': 'Hypno', 'level': 26, 'hp_increase': 30}, moves=[{'name': 'Pound', 'min_damage': 5, 'max_damage': 10}, {'name': 'Confusion', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Krabby", 30, 0.3, evolution={'name': 'Kingler', 'level': 28, 'hp_increase': 30}, moves=[{'name': 'Vice Grip', 'min_damage': 10, 'max_damage': 15}, {'name': 'Bubble', 'min_damage': 5, 'max_damage': 10}]),
        Pokemon("Voltorb", 40, 0.3, evolution={'name': 'Electrode', 'level': 30, 'hp_increase': 30}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Spark', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Exeggcute", 60, 0.3, evolution={'name': 'Exeggutor', 'level': 30, 'hp_increase': 30}, moves=[{'name': 'Barrage', 'min_damage': 5, 'max_damage': 10}, {'name': 'Confusion', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Cubone", 50, 0.3, evolution={'name': 'Marowak', 'level': 28, 'hp_increase': 30}, moves=[{'name': 'Bone Club', 'min_damage': 10, 'max_damage': 15}, {'name': 'Headbutt', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Hitmonlee", 50, 0.3, evolution=None, moves=[{'name': 'Double Kick', 'min_damage': 10, 'max_damage': 15}, {'name': 'High Jump Kick', 'min_damage': 15, 'max_damage': 20}]),
        Pokemon("Hitmonchan", 50, 0.3, evolution=None, moves=[{'name': 'Comet Punch', 'min_damage': 10, 'max_damage': 15}, {'name': 'Fire Punch', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Lickitung", 90, 0.3, evolution=None, moves=[{'name': 'Lick', 'min_damage': 5, 'max_damage': 10}, {'name': 'Stomp', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Koffing", 40, 0.3, evolution={'name': 'Weezing', 'level': 35, 'hp_increase': 30}, moves=[{'name': 'Tackle', 'min_damage': 5, 'max_damage': 10}, {'name': 'Sludge', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Rhyhorn", 80, 0.3, evolution={'name': 'Rhydon', 'level': 42, 'hp_increase': 40}, moves=[{'name': 'Horn Attack', 'min_damage': 10, 'max_damage': 15}, {'name': 'Stomp', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Chansey", 250, 0.2, evolution={'name': 'Blissey', 'level': 42, 'hp_increase': 40}, moves=[{'name': 'Pound', 'min_damage': 5, 'max_damage': 10}, {'name': 'Double Slap', 'min_damage': 10, 'max_damage': 15}]),
        Pokemon("Tangela", 65, 0.3, evolution=None, moves=[{'name': 'Vine Whip', 'min_damage': 10, 'max_damage': 15}, {'name': 'Absorb', 'min_damage': 5, 'max_damage': 10}]),
    ]

    while True:
        action = input("Do you want to (c)atch a Pokemon, (s)how your Pokemons, or (b)attle? (q to quit): ").lower()
        if action == 'c':
            wild_pokemon = random.choice(wild_pokemons)
            print(f"A wild {wild_pokemon.name} appeared!")
            catch = input(f"Do you want to catch {wild_pokemon.name}? (y/n): ").lower()
            if catch == 'y':
                trainer.catch_pokemon(wild_pokemon)
            else:
                print(f"{wild_pokemon.name} ran away!")
        elif action == 's':
            trainer.show_pokemons()
        elif action == 'b':
            wild_pokemon = random.choice(wild_pokemons)
            print(f"A wild {wild_pokemon.name} appeared!")
            trainer.battle(wild_pokemon)
        elif action == 'q':
            break
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
