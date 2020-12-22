# Ruben
class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def Move(self, delta_x, delta_y):
        self.pos_x = delta_x
        self.pos_y = delta_y

    def Is_alive(self):
        return self.hp > 0

    def Get_damage(self, amount):
        self.hp -= amount

    def Get_cords(self):
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
            dist = abs(actor.pos_x - target.pos_x) + abs(actor.pos_y - target.pos_y)
            print(f'dist = {dist}')
            if dist > self.range:
                print(f"target is too far for weapon {self.name}")
            else:
                print(f"enemy was hit from weapon {self.name} , damage is {self.damage}")
                target.hp = target.hp - self.damage


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, hp, weapon):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def __str__(self):
        return f"enemy is in the position({self.pos_x},{self.pos_y}) with weapon {self.weapon}"

    def Hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.Hit(self, target)
        else:
            print('i can hit only main hero')


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, hp, weapon):
        super().__init__(pos_x, pos_y, hp)
        self.arsenal = []
        self.weapon = weapon

    def Hit(self, target):
        if self.weapon is None:
            print('i am unarmed')
        else:
            if isinstance(target, BaseEnemy):
                self.weapon.Hit(self, target)
            else:
                print('i can hit only enemy')

    def Add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.arsenal.append(weapon)
            self.weapon = weapon
            print(f"picked up {weapon.name}")
        else:
            print('it\'s not a Weapon')

    def Next_weapon(self):
        if not self.arsenal:
            print('i am unarmed')
        elif len(self.arsenal) == 1:
            print('i have one weapon')
        else:
            i = self.arsenal.index(self.weapon) + 1
            if i > len(self.arsenal) - 1: i = 0
            self.weapon = self.arsenal[i]
            print(f'i take weapon {self.weapon}')

    def Heal(self, amount):
        self.hp += amount
        if self.hp > 200: self.hp = 200
        print(f'how my health is {self.hp}')


weapon1 = Weapon('gmp', 20, 5)
weapon2 = Weapon('gmp2', 40, 5)
weapon3 = Weapon('gmp3', 60, 5)
arsen = MainHero(10, 5, 200)
arsen.Add_weapon(weapon1)
arsen.Add_weapon(weapon2)
arsen.Add_weapon(weapon3)
hayk = BaseEnemy(10, 9, 200, weapon1)

print(arsen.Is_alive())
print(arsen.Get_cords())
hayk.Hit(arsen)
print(arsen.hp)
arsen.Next_weapon()
arsen.Next_weapon()
arsen.Hit(hayk)
print(hayk.hp)
