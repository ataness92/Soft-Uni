from python_oop.first_steps_in_oop.project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemon = []


    def add_pokemon(self, pokemon: Pokemon): 
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught "+pokemon.pokemon_details()
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemon:
            if pokemon_name == pokemon.name:
                self.pokemon.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        message = ""

        message += f"Pokemon Trainer {self.name}\n"
        message += f"Pokemon count {len(self.pokemon)}"
        for pokemon in self.pokemon:
            message += "\n"
            message += f"- {pokemon.name} with {pokemon.health}"
        return message

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
