
class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bvn", self.pseudo, "/ Points de vie :", health, "/ points d'attaque :", self.attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage
    def attack_player(self, target_player):
        damage = self.attack

class Warrior(Player):

    def __init__(self, pseudo, health, attack, armor):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("Bvn", self.pseudo, "/ Points de vie :", health, "/ points d'attaque :", self.attack)

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        super().damage(damage)

    def blade(self):
        self.armor = 3
        print("Les points d armure on été rechargés")

    def get_armor_point(self):
        return self.armor


warrior = Warrior("DarkWarrior", 30, 4, 3)
warrior.damage(10)
print("vie:", warrior.health, "armure:", warrior.get_armor_point())

if issubclass(Warrior, Player) :
    print("Le guerrier est bien une spécialisation de player")