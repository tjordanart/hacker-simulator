# Hacker Simulator

A fictional cybersecurity-themed terminal game built with Python.

**Play the game:** [tjordanart.com/hacker-sim](https://www.tjordanart.com/hacker-sim)

## Overview

Hacker Simulator is an interactive command-line game where the player takes on fictional cybersecurity contracts, makes decisions, completes missions, earns money and experience, and manages their **energy** and **heat** levels.

The project started as a programming exercise focused on Python fundamentals and evolved into a larger game system with progression, randomized outcomes, terminal animations, multiple mission paths, and multiple endings.

> **Note:** This is a fictional simulation. It does not perform real hacking, network scanning, password cracking, or unauthorized access.

## Features

- Five-mission campaign
- Interactive player setup
- Multiple choices and mission paths
- Player level and XP progression
- Money and reward system
- Energy management
- Heat and detection system
- Randomized mission outcomes
- Multiple possible endings
- Mission difficulty progression
- Rest system for recovering energy
- Colorized terminal interface
- Character-by-character terminal typing
- Timed system messages and animations
- Decisions that affect mission outcomes

## Technologies & Concepts

- **Python 3**
- `random` for randomized mission outcomes
- `time` for timing and terminal animations
- ANSI escape codes for colored terminal output
- Functions and reusable game systems
- Loops and game-state management
- Conditional logic
- Lists and data structures
- User input and validation

## How the Game Works

The player begins by creating a hacker name and entering the fictional cybersecurity simulation.

Throughout the game, several statistics are tracked:

| Statistic | Purpose |
|---|---|
| **Level** | Tracks player progression |
| **XP** | Earned through successful actions and missions |
| **Money** | Earned through completed contracts |
| **Energy** | Used when performing mission actions |
| **Heat** | Represents how much attention the player has attracted |

Players make decisions during each mission, with different choices producing different success rates and consequences.

Successful actions can provide XP, money, and mission progression. Failed actions can increase heat and affect future decisions.

The player's final heat level determines the ending of the game.

## Terminal Interface

The game uses a custom typing function to display important terminal messages one character at a time.

This creates a more cinematic command-line experience while demonstrating Python's `time.sleep()` functionality and terminal output control.

Example:

```text
> Initializing fictional scanner...
> Searching simulated services...
> Scan complete.
```

Different message types use terminal colors to help distinguish important information during gameplay.

## Running the Game

### Requirements

- Python 3

### Clone the Repository

```bash
git clone https://github.com/Tjordanart/hacker-simulator.git
```

### Navigate to the Project

```bash
cd hacker-simulator
```

### Run the Game

```bash
python hacker_simulator_v2.py
```

The project can also be opened and run through an IDE such as PyCharm.

## Project Evolution

Hacker Simulator began as a simple fictional cybersecurity terminal simulation focused primarily on terminal animations and simulated cybersecurity activity.

The current version expands the concept into a complete interactive game with:

- Player progression
- Missions
- XP and money
- Energy management
- Heat and detection
- Randomized outcomes
- Player decisions
- Multiple endings
- More structured game logic
- Improved terminal presentation

### What's Next

The next planned version is a **web-based implementation using HTML, CSS, and JavaScript**.

The goal is to bring the game's systems and progression into an interactive browser experience while expanding the visual and user-interface elements beyond the terminal.

## What I Practiced

This project gave me hands-on practice with:

- Python fundamentals
- Functions
- Variables
- Loops
- Conditional statements
- User input
- Random number generation
- Game-state management
- Structuring larger programs
- Terminal interfaces
- Timing and animation effects
- Building multiple systems into a single application

It also serves as a foundation for exploring how the same application can be rebuilt in another programming language and environment.

## Disclaimer

Hacker Simulator is a fictional cybersecurity simulation created for educational and entertainment purposes.

No real systems, networks, accounts, passwords, or devices are accessed, scanned, attacked, or compromised.

All cybersecurity activities represented in the game are simulated.

## Author

**Tyler Jordan**

[GitHub](https://github.com/Tjordanart)  
[Portfolio](https://www.tjordanart.com)
