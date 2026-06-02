# Monty Hall Problem

## What is the Monty Hall Problem?

The Monty Hall problem is a famous probability puzzle based on a game show scenario. There are three doors:

- Behind one door is a prize (usually a car).
- Behind the other two doors are goats.

The player picks one door. Then the host, who knows what is behind every door, opens one of the other two doors to reveal a goat. After the host reveals the goat, the player is given a choice:

- stay with the original door
- switch to the remaining unopened door

The surprising result is:

- staying wins about 1 out of 3 times
- switching wins about 2 out of 3 times

## Case scenarios and probabilities

There are three equally likely initial placements for the prize and three equally likely initial choices by the player. The key observation is that the player’s first choice has only a 1/3 chance of being correct.

### Scenario 1: The player initially chooses the prize door

- Probability: 1/3
- Host opens one of the two goat doors.
- If the player stays, they win.
- If the player switches, they lose.

Result: stay wins, switch loses.

### Scenario 2: The player initially chooses a goat door

- Probability: 2/3
- The prize is behind one of the two doors the player did not choose.
- The host opens the other goat door.
- If the player stays, they lose.
- If the player switches, they win.

Result: stay loses, switch wins.

### Why switching is better

Because the initial choice is only correct 1/3 of the time, the initial choice is wrong 2/3 of the time.

- If the initial choice is correct (1/3 chance), staying wins and switching loses.
- If the initial choice is wrong (2/3 chance), staying loses and switching wins.

Therefore:

- stay win probability = 1/3
- switch win probability = 2/3

This is the core paradox: after the host reveals a goat, the remaining unopened door has a higher chance of containing the prize than the original door.

## What does this simulation do?

The `monty-hall.py` script simulates the Monty Hall problem many times and compares the win rate for both strategies:

- staying with the original door
- switching after the host reveals a goat

For each trial, the simulation:

1. randomly places the prize behind one of three doors
2. randomly chooses a door for the player
3. has the host open a goat door that is not the player’s choice
4. checks whether staying would win
5. checks whether switching to the remaining door would win

After running the requested number of trials, it prints the win percentages for both strategies.

## How to run

From the `Monty-Hall-Problem` folder, run:

```bash
python monty-hall.py
```

Then enter the number of trials, or press Enter to use the default of `10000`.

The expected output should show a much higher win rate when switching than when staying.
