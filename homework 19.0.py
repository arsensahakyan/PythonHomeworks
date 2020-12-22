import math


# Ruben
class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def Is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y


class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def __str__(self):
        return self.name

    def Hit(self, actor, target):
        if not target.Is_alive():
            print('the enemy is already defeated')
        else:
            dist = math.sqrt((target.pos_x - actor.pos_x) ** 2 + (target.pos_y - actor.pos_y) ** 2)
            if dist > self.range:
                print(f"target is too far for weapon {self.name}")
            else:
                print(f"enemy was hit from weapon {self.name} , damage is {self.damage}")
                target.hp = target.hp - self.damage


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def __str__(self):
        return f"enemy is in the position({self.pos_x},{self.pos_y}) with weapon {self.weapon}"

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.Hit(self, target)
        else:
            print('i can hit only main hero')


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, hp, name):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.arsenal = []
        self.weapon = self.arsenal[0] if self.arsenal else None

    def hit(self, target):
        if self.weapon is None:
            print('i am unarmed')
        else:
            if isinstance(target, BaseEnemy):
                self.weapon.Hit(self, target)
            else:
                print('i can hit only enemy')

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.arsenal.append(weapon)
            print(f"picked up {weapon.name}")
        else:
            print('it\'s not a Weapon')

    def next_weapon(self):
        if not self.arsenal:
            print('i am unarmed')
        elif len(self.arsenal) == 1:
            print('i have one weapon')
        else:
            i = 0 if self.weapon is None else self.arsenal.index(self.weapon) + 1
            if i > len(self.arsenal) - 1: i = 0
            self.weapon = self.arsenal[i]
            print(f'i take weapon {self.weapon}')

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200: self.hp = 200
        print(f'how my health is {self.hp}')


weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)
