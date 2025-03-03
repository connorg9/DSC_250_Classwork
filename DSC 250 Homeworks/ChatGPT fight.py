import random
import matplotlib as plt

def generate_strength(age):
    """Assigns a strength score based on age."""
    if 18 <= age <= 35:
        return random.uniform(70, 100)  # Prime strength years
    elif 36 <= age <= 50:
        return random.uniform(50, 80)
    elif 51 <= age <= 70:
        return random.uniform(30, 60)
    else:
        return random.uniform(10, 40)  # Children & elderly


def get_winner(player1, player2):
    """Determines the winner based on strength."""
    if player1['strength'] > player2['strength']:
        return player1
    elif player2['strength'] > player1['strength']:
        return player2
    else:
        return random.choice([player1, player2])  # Random tiebreaker


def run_tournament(num_players=1000):
    """Simulates a global 1v1 fight tournament."""
    players = [{'age': random.randint(0, 100), 'strength': 0} for _ in range(num_players)]
    for player in players:
        player['strength'] = generate_strength(player['age'])

    round_num = 1
    while len(players) > 1:
        oldest = max(players, key=lambda x: x['age'])['age']
        youngest = min(players, key=lambda x: x['age'])['age']
        print(f"Round {round_num}: {len(players)} players remaining (Age Range: {youngest}-{oldest})")

        if len(players) % 2 == 1:
            bye_player = random.choice(players)  # Give one random player a bye
            players.remove(bye_player)
            next_round = [bye_player]
        else:
            next_round = []

        for i in range(0, len(players), 2):
            winner = get_winner(players[i], players[i + 1])
            next_round.append(winner)

        players = next_round
        round_num += 1

    print(f"Winner: Age {players[0]['age']}, Strength {players[0]['strength']:.2f}")

run_tournament(8208165300)
