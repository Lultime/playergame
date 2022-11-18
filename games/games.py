
from player import player
from weapon import weapon

knife =("couteau", 3)

Player1 = player("lultime", 20, 5)
Player2 = player("iframe", 32, 5)

Player1.attact_player(Player2)
print(Player1.get_pseudo() , "attaque",Player2.get_pseudo())


print("bienvenue au joueur" , Player1.get_pseudo(), "/ points de vie:", Player1.get_health()," / nombre d attaque :", Player1.get_attact_vallue())
print("bienvenue au joueur" , Player2.get_pseudo(), "/ points de vie:", Player2.get_health()," / nombre d attaque :", Player2.get_attact_vallue())

Player3 = player("alliance", 22, 6)



