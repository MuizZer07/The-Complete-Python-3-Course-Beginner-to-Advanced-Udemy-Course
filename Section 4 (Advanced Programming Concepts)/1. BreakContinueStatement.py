import random


playerhp = 260
enemytkl = 60
enemytkh = 80

while playerhp > 0:
    damage = random.randrange(enemytkl, enemytkh)
    playerhp = playerhp - damage

    if playerhp <= 30:
        playerhp = 30;

    print("Enemy strikes for ", damage, "points of damage. Current HP is ", playerhp)

    if playerhp > 30:
        continue

    print("You have low health. You've been teleported to the nearest inn")
    break

