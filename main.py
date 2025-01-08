import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero(name = "Hero", health = 100)
hero.equip(iron_sword)
enemy = Enemy(name = "Enemy", health = 100, weapon = short_bow)

while hero.health != 0 and enemy.health != 0:
    os.system("clear")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    if(enemy.health == 0 and hero.health != 0):
        print(f"{hero.name} defeated {enemy.name}!")
    elif(enemy.health != 0 and hero.health == 0):
        print("The Hero is defeated...")

    input()