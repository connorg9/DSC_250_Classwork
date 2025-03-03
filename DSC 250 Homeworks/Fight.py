
import numpy as np

players = 8208165300
extra = 0
round = 1

print("Starting players: ", players)

while players > 1:
    players += extra

    if players % 2 != 0:  # If odd, set aside one player for a bye
        extra = 1
        players -= 1

    players //= 2  # Proceed to the next round
    print("Players left after round {0}: {1}".format(round, players))
    round += 1


