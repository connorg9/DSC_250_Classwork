import random
import matplotlib.pyplot as plt
from collections import defaultdict


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


def generate_player():
    """Generate a single player with age and strength."""
    age = random.randint(0, 100)
    strength = generate_strength(age)
    return {'age': age, 'strength': strength}


def get_winner(player1, player2):
    """Determines the winner based on strength."""
    if player1['strength'] > player2['strength']:
        return player1
    elif player2['strength'] > player1['strength']:
        return player2
    else:
        return random.choice([player1, player2])  # Random tiebreaker


def run_tournament(num_players=1000, track_demographics=True):
    """
    Simulates a global 1v1 fight tournament without storing all players in memory.

    Args:
        num_players: Number of players in tournament
        track_demographics: Whether to track age distribution across rounds

    Returns:
        Tuple of (winner, age_distributions, age_ranges) where:
        - age_distributions is a dict mapping round numbers to age distribution lists
        - age_ranges is a dict mapping round numbers to (min_age, max_age) tuples
    """
    # Calculate number of rounds needed
    total_rounds = 0
    remaining = num_players
    while remaining > 1:
        remaining = (remaining + 1) // 2  # Account for potential bye
        total_rounds += 1

    print(f"Tournament will have {total_rounds} rounds")

    # Track age demographics and ranges by round
    age_distributions = defaultdict(list) if track_demographics else None
    age_ranges = {}  # Will store (min_age, max_age) for each round

    # First round - generate players in pairs, immediately fight, keep only winners
    round_num = 1
    remaining_players = num_players
    players = []  # Will contain just the active players for current round

    # Age tracking for the first round
    min_age = 100
    max_age = 0

    # Handle first round separately to avoid storing all players
    fights_in_round = remaining_players // 2

    # Handle odd number of players
    if remaining_players % 2 == 1:
        # Give one random player a bye
        bye_player = generate_player()
        players.append(bye_player)

        # Update age tracking
        min_age = min(min_age, bye_player['age'])
        max_age = max(max_age, bye_player['age'])

        if track_demographics:
            age_distributions[round_num].append(bye_player['age'])

    # Generate and fight pairs, keeping only winners
    for _ in range(fights_in_round):
        player1 = generate_player()
        player2 = generate_player()

        # Update age tracking
        min_age = min(min_age, player1['age'], player2['age'])
        max_age = max(max_age, player1['age'], player2['age'])

        if track_demographics:
            age_distributions[round_num].append(player1['age'])
            age_distributions[round_num].append(player2['age'])

        winner = get_winner(player1, player2)
        players.append(winner)

    # Store age range for the first round
    age_ranges[round_num] = (min_age, max_age)
    print(f"Round {round_num}: {remaining_players} players (Age Range: {min_age}-{max_age})")

    # Subsequent rounds
    round_num += 1
    remaining_players = len(players)

    while remaining_players > 1:
        # Reset age tracking for this round
        min_age = min(player['age'] for player in players)
        max_age = max(player['age'] for player in players)

        # Store age range for this round
        age_ranges[round_num] = (min_age, max_age)
        print(f"Round {round_num}: {remaining_players} players (Age Range: {min_age}-{max_age})")

        if track_demographics:
            # Record ages of all players in this round
            for player in players:
                age_distributions[round_num].append(player['age'])

        # Handle odd number of players
        if remaining_players % 2 == 1:
            bye_player = random.choice(players)
            players.remove(bye_player)
            next_round = [bye_player]
        else:
            next_round = []

        # Pair players and determine winners
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                winner = get_winner(players[i], players[i + 1])
                next_round.append(winner)

        players = next_round
        round_num += 1
        remaining_players = len(players)

    # Final winner
    winner = players[0]
    print(f"Winner: Age {winner['age']}, Strength {winner['strength']:.2f}")

    return winner, age_distributions, age_ranges


def plot_age_distributions(age_distributions, age_ranges):
    """Plot how the age distribution evolves over rounds."""
    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Get the rounds to plot (we'll only plot a subset if there are many)
    rounds = sorted(age_distributions.keys())
    max_plots = 9  # Maximum number of rounds to plot

    if len(rounds) > max_plots:
        # Choose evenly spaced rounds to plot
        indices = [int(i * (len(rounds) - 1) / (max_plots - 1)) for i in range(max_plots)]
        rounds_to_plot = [rounds[i] for i in indices]
    else:
        rounds_to_plot = rounds

    # Calculate subplot arrangement
    n_cols = 3
    n_rows = (len(rounds_to_plot) + n_cols - 1) // n_cols

    for i, round_num in enumerate(rounds_to_plot):
        plt.subplot(n_rows, n_cols, i + 1)
        plt.hist(age_distributions[round_num], bins=20, range=(0, 100))
        min_age, max_age = age_ranges[round_num]
        plt.title(f"Round {round_num} (Age Range: {min_age}-{max_age})")
        plt.xlabel("Age")
        plt.ylabel("Count")

    plt.tight_layout()
    return plt


def plot_age_range_evolution(age_ranges):
    """Create a line plot showing how the age range changes across rounds."""
    rounds = sorted(age_ranges.keys())
    min_ages = [age_ranges[r][0] for r in rounds]
    max_ages = [age_ranges[r][1] for r in rounds]

    plt.figure(figsize=(10, 6))
    plt.plot(rounds, min_ages, 'b-', marker='o', label='Minimum Age')
    plt.plot(rounds, max_ages, 'r-', marker='o', label='Maximum Age')
    plt.fill_between(rounds, min_ages, max_ages, alpha=0.2, color='gray')

    plt.title("Age Range Evolution Throughout Tournament")
    plt.xlabel("Round")
    plt.ylabel("Age")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    return plt


# Run a tournament with a reasonable number of players
num_players = 82081653  # Try with 100k players instead of 8 billion
winner, age_distributions, age_ranges = run_tournament(num_players, track_demographics=True)

