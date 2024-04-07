import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def attack_target(self, target):
        damage = random.randint(1, self.attack)
        target.take_damage(damage)
        print(f"{self.name} hits {target.name} for {damage} damage!")


class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=20)


class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, hp=50, attack=10)


def battle(player, enemy):
    print("A battle begins between you and the enemy!")
    while player.is_alive() and enemy.is_alive():
        player.attack_target(enemy)
        if not enemy.is_alive():
            print(f"The enemy {enemy.name} has been defeated!")
            break
        enemy.attack_target(player)
        if not player.is_alive():
            print("You have been defeated!")
            break


def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    enemy = Enemy("Goblin")
    battle(player, enemy)


if __name__ == "__main__":
    main()
