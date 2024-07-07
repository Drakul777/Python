
from model.player import Player
from model.weapon import Weapon

knife = Weapon("Couteau", 3)

player1 = Player("Graven", 20, 3)
player1.set_weapon(knife)

player2 = Player("Bob", 20, 5)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())

print("Points de vie :", player1.get_health(), "/ points d'attaque :", player1.get_attack_value())
print("Points de vie :", player2.get_health(), "/ points d'attaque :", player2.get_attack_value())
