# Hacker Simulator

A fictional cybersecurity-themed terminal game built in Python.

Hacker Simulator is an interactive command-line game where the player takes on fictional cybersecurity contracts, makes decisions, completes missions, earns money and experience, and manages their heat and energy levels.

The project was created as a programming exercise to practice Python fundamentals while building a more complete game system with progression, random outcomes, terminal animations, and interactive gameplay.

This project does not perform real hacking, network scanning, password cracking, or unauthorized access.

---

## Features

* Interactive player name and game setup
* Five-mission campaign
* Multiple choices and mission paths
* Player level and experience system
* Money and reward system
* Energy management system
* Heat and detection system
* Randomized mission outcomes
* Multiple possible endings
* Colorized terminal interface
* Character-by-character terminal typing
* Timed system messages and animations
* Mission difficulty progression
* Rest system for recovering energy
* Different outcomes based on player decisions

---

## Technologies Used

* Python 3
* `random` - Generates randomized mission outcomes
* `time` - Controls typing effects and timed sequences
* ANSI escape codes - Creates colored terminal output
* Functions - Organizes reusable game systems
* Loops - Controls the main game cycle
* Conditional logic - Controls decisions and outcomes
* Variables - Stores player statistics and game state
* Lists and data structures - Used to organize game information
* User input - Allows the player to interact with the game

---

## How It Works

The player begins by creating a hacker name and entering the fictional cybersecurity simulation.

The game then tracks several player statistics:

* **Level** - Determines progression through the game
* **XP** - Earned by completing actions and missions
* **Money** - Earned from successful contracts
* **Energy** - Used when performing mission actions
* **Heat** - Represents how much attention the player has attracted

Players can investigate fictional systems, analyze security, attempt simulated access, or make other decisions during missions.

Different choices have different success rates and consequences.

---

## Game Progression

The game contains five fictional missions.

Each mission introduces new challenges and gives the player different choices.

Successful actions can provide:

* XP
* Money
* Mission progression

Failed actions can increase the player's heat and make future decisions more difficult.

The player's final heat level determines which ending they receive.

---

## Terminal Animation

The game uses a custom typing function to display important terminal messages one character at a time.

This creates a more cinematic command-line experience while demonstrating Python's `time.sleep()` function and terminal output control.

Example:

```text
> Initializing fictional scanner...
> Searching simulated services...
> Scan complete.
```

Different message types use different terminal colors to make important information easier to recognize.

---

## How to Run

Make sure Python 3 is installed.

Clone the repository:

```bash
git clone https://github.com/Tjordanart/hacker-simulator.git
```

Navigate to the project folder:

```bash
cd hacker-simulator
```

Run the game:

```bash
python hacker_simulator_v2.py
```

You can also run the Python file directly through an IDE such as PyCharm.

---

## Project Evolution

This project began as a simple fictional cybersecurity terminal simulation.

The original version focused primarily on terminal animations and simulated cybersecurity activity.

Version 2 expands the project into a complete interactive game by adding:

* Player progression
* Missions
* XP
* Money
* Energy
* Heat
* Randomized outcomes
* Multiple endings
* Player decisions
* More structured game logic
* Improved terminal presentation

The next stage of the project is to rebuild the game as a web-based application using JavaScript, HTML, and CSS.

This will allow the same game concepts to be presented through an interactive browser interface instead of a Python terminal.

---

## Purpose of This Project

This project was created to practice:

* Python programming
* Functions
* Variables
* Loops
* Conditional statements
* User input
* Random number generation
* Game state management
* Object-oriented-style organization
* Timing and animations
* Terminal interfaces
* Building larger programs from smaller systems

It also serves as a foundation for translating a Python project into JavaScript for a web-based version.

---

## Disclaimer

Hacker Simulator is a fictional cybersecurity simulation created for educational and entertainment purposes.

No real systems, networks, accounts, passwords, or devices are accessed, scanned, attacked, or compromised.

All cybersecurity activities represented in the game are simulated.

---

## Author

Created by Tyler Jordan

GitHub: https://github.com/Tjordanart
