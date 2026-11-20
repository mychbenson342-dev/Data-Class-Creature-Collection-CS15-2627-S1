from dataclasses import dataclass
@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: int

creature1 = Creature("Dragon", species="Friar Fliers", level=20, health=180)
creature2 = Creature("Golem", "Stone Smashers", 5, 70)
creature3 = Creature("Goblin", "Green Sprites", 12, 85)
creature4 = 1
creature2.level = 10
creature2.health = 75

print(creature1)
print(creature2)
print(creature3)
while True:
    choice = input("\n1. Add a Creature\nType 1: ")
    if choice == "1":
        while True:
            name = input("Name: ")
            species = input("Species: ")
            try:
                level = int(input("Level (whole number): "))
                health = float(input("Health (number): "))
                creature4 = Creature(name, species, level, health)
                print(creature4)
                break
            except ValueError:
                print("Wrong Restart")
        break