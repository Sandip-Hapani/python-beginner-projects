import random


def simulate_monty_hall(trials: int = 10000) -> tuple[float, float]:
    """Simulate the Monty Hall problem.

    Returns a tuple containing the win rates for:
    - staying with the original door
    - switching after the host reveals a goat
    """
    stay_wins = 0
    switch_wins = 0

    for _ in range(trials):
        doors = [0, 1, 2]
        prize_door = random.choice(doors)
        player_choice = random.choice(doors)

        # Host opens a goat door that is not the player's choice.
        available_doors = [door for door in doors if door != player_choice and door != prize_door]
        host_opens = random.choice(available_doors)

        # If the player stays, they win if their original choice is the prize door.
        if player_choice == prize_door:
            stay_wins += 1

        # If the player switches, they choose the remaining closed door.
        remaining_doors = [door for door in doors if door != player_choice and door != host_opens]
        if remaining_doors and remaining_doors[0] == prize_door:
            switch_wins += 1

    stay_rate = stay_wins / trials
    switch_rate = switch_wins / trials
    return stay_rate, switch_rate


def main() -> None:
    try:
        trials_input = input("Enter number of trials (default 10000): ").strip()
        trials = int(trials_input) if trials_input else 10000
    except ValueError:
        print("Invalid input. Using default of 10000 trials.")
        trials = 10000

    stay_rate, switch_rate = simulate_monty_hall(trials)
    print(f"After {trials} trials:")
    print(f"  Stay win rate:   {stay_rate:.2%}")
    print(f"  Switch win rate: {switch_rate:.2%}")


if __name__ == "__main__":
    main()
