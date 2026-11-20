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
creature4 = Creature(name= None, species=None, level=None, health=None)
creature2.level = 10
creature2.health = 75

print(creature1)
print(creature2)
print(creature3)

while True:
  bleh =  input("\n1. Add a Creature")
  if bleh == "1":
      input("\n What name would you like to add for your creature?")



