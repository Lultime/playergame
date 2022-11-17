class player:
    def __init__(self, pseudo, hearth, attact):
        self.pseudo = pseudo
        self.health = hearth
        self.attact = attact
        print ("bienvenue au joueur", pseudo, "/ points de vie:", hearth, " / nombre d attaque :", attact)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attact_vallue(self):
        return self.attact

    def damage(self, damage):
        self.health -= damage

    def attact_player(self, target_player):
        target_player.damage(self.attact)


class Warrior(player):

    def __init__(self, pseudo, hearth, attact):
        super().__init__(pseudo,hearth,attact)
        self.pseudo = pseudo
        self.health = hearth
        self.attact = attact
        self.amort = 4
        print("bienvenue au guerrier", pseudo, "/ points de vie:", hearth, " / nombre d attaque :", attact)


    def damage(self, damage):
        if self.amort>0:
           self.amort -=1
           damage=0
           super().damage(damage)

           self.health -= damage




    def blade(self):
        self.amort = 4
        print("votre armure a ete recharge")

    def get_amort_point(self):
        return self.amort

Player1 = player("lultime", 20, 6)
Player1.damage(3)

warrior = Warrior("darkwarrior", 23,4)
warrior.damage(4)

warrior.damage(4)
print("vie:" ,warrior.get_health(), "armure", warrior.get_amort_point())

warrior.damage(4)
print("vie:" ,warrior.get_health(), "armure", warrior.get_amort_point())

warrior.damage(4)
print("vie:" ,warrior.get_health(), "armure", warrior.get_amort_point())

if issubclass(Warrior, player):
    print("le guerrier est bien une specialisation de player")






