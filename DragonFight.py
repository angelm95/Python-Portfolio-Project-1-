# Character stats

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.attack = 100


player1 = Player("Deagono", 1000)
player2 = Player("Slados", 1000)

print("P1:", player1.name, " -- HP:", player1.hp, "-- Attack: ", player1.attack)
print("P2:", player2.name, " -- HP:", player2.hp, "-- Attack: ", player2.attack)

Deagono_attack = 100
Deagono_hp = 1000

Slados_attack = 100
Slados_hp = 1000


def dragon_duel():
    print("The dragon duel has begun")
    player1.hp -= 500
    player2.hp -= 500
    print("P1:", player1.name, " -- HP:",
          player1.hp, "-- Attack: ", player1.attack)
    print("P2:", player2.name, " -- HP:",
          player2.hp, "-- Attack: ", player2.attack)
