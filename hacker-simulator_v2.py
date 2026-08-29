# Hacker Simulator
# A fictional cybersecurity simulation game.
# This game does not connect to or interact with real systems.

import random
import time


# Terminal colors.

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"


def color(text, text_color):
    """Applies a terminal color to text."""
    return text_color + text + RESET


def line():
    print("-" * 60)


def show_header():
    print()
    print(color("=" * 60, CYAN))
    print(color("                    HACKER SIMULATOR", CYAN))
    print(color("=" * 60, CYAN))


def show_stats():
    line()

    print("PLAYER:", player_name)
    print("LEVEL:", level)
    print("XP:", xp)
    print("MONEY:", color("$" + str(money), GREEN))
    print("HEAT:", color(str(heat) + "%", get_heat_color()))
    print("ENERGY:", color(str(energy) + "%", get_energy_color()))

    line()


def get_heat_color():
    """Changes the heat color depending on the current danger level."""

    if heat >= 75:
        return RED

    elif heat >= 40:
        return YELLOW

    else:
        return GREEN


def get_energy_color():
    """Changes the energy color depending on how much remains."""

    if energy <= 25:
        return RED

    elif energy <= 50:
        return YELLOW

    else:
        return GREEN


def pause():
    input("\nPress Enter to continue...")


def type_text(text, speed=0.03, text_color=""):
    """
    Types text one character at a time.

    flush=True forces each character to appear immediately
    in the terminal instead of waiting for the entire line.
    """

    for character in text:

        print(
            text_color + character + RESET,
            end="",
            flush=True
        )

        time.sleep(speed)

    print()


def system_message(text):
    """Displays a cyan terminal message."""

    type_text(
        "> " + text,
        0.03,
        CYAN
    )


def success_message(text):
    """Displays a successful action in green."""

    type_text(
        "> " + text,
        0.03,
        GREEN
    )


def warning_message(text):
    """Displays a warning in yellow."""

    type_text(
        "> " + text,
        0.03,
        YELLOW
    )


def error_message(text):
    """Displays an error or failed action in red."""

    type_text(
        "> " + text,
        0.03,
        RED
    )


def add_heat(amount):
    global heat

    heat += amount

    if heat > 100:
        heat = 100


def remove_heat(amount):
    global heat

    heat -= amount

    if heat < 0:
        heat = 0


def add_xp(amount):
    global xp
    global level

    xp += amount

    print(
        color(
            "\n+" + str(amount) + " XP",
            MAGENTA
        )
    )

    # Players level up every time they reach 100 XP.

    while xp >= 100:

        xp -= 100
        level += 1

        print()
        print(color("************************************", MAGENTA))
        print(color("             LEVEL UP!", MAGENTA))
        print(color("************************************", MAGENTA))
        print(
            color(
                "You are now level " + str(level),
                MAGENTA
            )
        )


def add_money(amount):
    global money

    money += amount

    print(
        color(
            "\n+$" + str(amount),
            GREEN
        )
    )


def check_energy(amount):

    if energy >= amount:
        return True

    error_message("Not enough energy.")

    return False


def use_energy(amount):
    global energy

    energy -= amount

    if energy < 0:
        energy = 0


def restore_energy():
    global energy

    energy = 100

    success_message("Energy restored to 100%.")


# Player setup.

player_name = input("Enter your hacker name: ").strip()

if player_name == "":
    player_name = "Unknown"


# Starting player stats.

level = 1
xp = 0
money = 500
heat = 0
energy = 100

current_mission = 1
total_missions = 5

game_running = True


# Introduction.

show_header()

print()
print(
    "Welcome,",
    color(player_name + "!", CYAN)
)

print()

print(
    "You have entered a fictional cybersecurity simulation."
)

print(
    "Complete contracts, earn money, gain experience,"
)

print(
    "and keep your heat under control."
)

print()

print(
    "All systems and targets in this game are fictional."
)

pause()


# Main game loop.

while game_running:

    if current_mission > total_missions:
        break

    show_header()

    show_stats()

    print()

    print(
        "CURRENT MISSION:",
        current_mission,
        "OF",
        total_missions
    )

    print()

    print("1. View Mission")
    print("2. View Stats")
    print("3. Rest")
    print("4. Quit Game")

    choice = input("\nChoose an option: ").strip()


    # View the current mission.

    if choice == "1":

        print()

        line()


        # Mission 1.

        if current_mission == 1:

            print(
                color(
                    "MISSION 1: FIRST CONNECTION",
                    CYAN
                )
            )

            line()

            print()

            print("TARGET: NOVA SYSTEMS")
            print("DIFFICULTY: EASY")
            print("REWARD: $300")

            print()

            print("OBJECTIVE:")

            print(
                "Perform a fictional security assessment."
            )

            print(
                "Gather information about the target system."
            )

            print()

            print("1. Run System Scan")
            print("2. Attempt Direct Access")
            print("3. Abort Mission")

            mission_choice = input(
                "\nChoose an action: "
            ).strip()


            if mission_choice == "1":

                if check_energy(10):

                    use_energy(10)

                    print()

                    system_message(
                        "Initializing fictional scanner..."
                    )

                    time.sleep(0.4)

                    system_message(
                        "Searching simulated services..."
                    )

                    time.sleep(0.5)

                    success_message(
                        "Scan complete."
                    )

                    print()

                    print(
                        "3 fictional services detected."
                    )

                    print(
                        "Security Level:",
                        color("LOW", GREEN)
                    )

                    add_xp(30)
                    add_money(300)
                    add_heat(5)

                    print()

                    success_message(
                        "You successfully gathered intelligence."
                    )

                    current_mission += 1

                    pause()


            elif mission_choice == "2":

                if check_energy(20):

                    use_energy(20)

                    print()

                    system_message(
                        "Attempting direct access..."
                    )

                    time.sleep(0.5)

                    warning_message(
                        "Security system detected!"
                    )

                    time.sleep(0.4)

                    roll = random.randint(1, 100)

                    if roll <= 35:

                        success_message(
                            "Access successful!"
                        )

                        add_xp(40)
                        add_money(300)
                        add_heat(20)

                        print()

                        success_message(
                            "You completed the mission quickly."
                        )

                        current_mission += 1

                    else:

                        error_message(
                            "Access denied."
                        )

                        warning_message(
                            "Your attempt attracted attention."
                        )

                        add_heat(25)

                    pause()


            elif mission_choice == "3":

                print()

                print("Mission aborted.")

                pause()


            else:

                error_message(
                    "Invalid choice."
                )

                pause()


        # Mission 2.

        elif current_mission == 2:

            print(
                color(
                    "MISSION 2: THE ARCHIVE",
                    CYAN
                )
            )

            line()

            print()

            print("TARGET: BLACKSTONE ARCHIVE")
            print("DIFFICULTY: EASY")
            print("REWARD: $450")

            print()

            print("OBJECTIVE:")

            print(
                "Locate a fictional database containing encrypted"
            )

            print(
                "research files."
            )

            print()

            print("1. Analyze Security")
            print("2. Attempt Access")
            print("3. Abort Mission")

            mission_choice = input(
                "\nChoose an action: "
            ).strip()


            if mission_choice == "1":

                if check_energy(15):

                    use_energy(15)

                    print()

                    system_message(
                        "Analyzing simulated security system..."
                    )

                    time.sleep(0.5)

                    system_message(
                        "Encryption detected."
                    )

                    time.sleep(0.4)

                    success_message(
                        "Weakness identified."
                    )

                    add_xp(40)
                    add_heat(10)

                    print()

                    print(
                        "Your analysis revealed a potential opening."
                    )

                    pause()


            elif mission_choice == "2":

                if check_energy(25):

                    use_energy(25)

                    print()

                    system_message(
                        "Attempting simulated access..."
                    )

                    time.sleep(0.5)

                    roll = random.randint(1, 100)

                    success_chance = 40 + (level * 5)

                    if roll <= success_chance:

                        success_message(
                            "Access successful!"
                        )

                        add_xp(50)
                        add_money(450)
                        add_heat(20)

                        print()

                        print(
                            "The fictional archive has been accessed."
                        )

                        current_mission += 1

                    else:

                        error_message(
                            "Access failed."
                        )

                        warning_message(
                            "Security systems have been alerted."
                        )

                        add_heat(30)

                    pause()


            elif mission_choice == "3":

                print()

                print("Mission aborted.")

                pause()


            else:

                error_message(
                    "Invalid choice."
                )

                pause()


        # Mission 3.

        elif current_mission == 3:

            print(
                color(
                    "MISSION 3: THE CORPORATION",
                    CYAN
                )
            )

            line()

            print()

            print("TARGET: OMEGA DYNAMICS")
            print("DIFFICULTY: MEDIUM")
            print("REWARD: $750")

            print()

            print("OBJECTIVE:")

            print(
                "Investigate a fictional corporate network."
            )

            print()

            print("1. Reconnaissance")
            print("2. Security Analysis")
            print("3. Attempt Access")
            print("4. Abort Mission")

            mission_choice = input(
                "\nChoose an action: "
            ).strip()


            if mission_choice == "1":

                if check_energy(15):

                    use_energy(15)

                    print()

                    system_message(
                        "Running reconnaissance..."
                    )

                    time.sleep(0.5)

                    system_message(
                        "Mapping fictional infrastructure..."
                    )

                    time.sleep(0.5)

                    success_message(
                        "Several systems discovered."
                    )

                    add_xp(35)
                    add_heat(10)

                    pause()


            elif mission_choice == "2":

                if check_energy(20):

                    use_energy(20)

                    print()

                    system_message(
                        "Analyzing security architecture..."
                    )

                    time.sleep(0.5)

                    print(
                        "Security level:",
                        color("MEDIUM", YELLOW)
                    )

                    success_message(
                        "Potential weakness detected."
                    )

                    add_xp(45)
                    add_heat(15)

                    pause()


            elif mission_choice == "3":

                if check_energy(30):

                    use_energy(30)

                    print()

                    system_message(
                        "Attempting simulated access..."
                    )

                    time.sleep(0.5)

                    roll = random.randint(1, 100)

                    success_chance = 30 + (level * 7)

                    if roll <= success_chance:

                        success_message(
                            "Access successful!"
                        )

                        add_xp(70)
                        add_money(750)
                        add_heat(25)

                        print()

                        success_message(
                            "You successfully completed the contract."
                        )

                        current_mission += 1

                    else:

                        error_message(
                            "Access denied."
                        )

                        add_heat(35)

                    pause()


            elif mission_choice == "4":

                print()

                print("Mission aborted.")

                pause()


            else:

                error_message(
                    "Invalid choice."
                )

                pause()


        # Mission 4.

        elif current_mission == 4:

            print(
                color(
                    "MISSION 4: THE DOUBLE CROSS",
                    CYAN
                )
            )

            line()

            print()

            print("TARGET: UNKNOWN")
            print("DIFFICULTY: HARD")
            print("REWARD: $1,000")

            print()

            print(
                "Something about this contract feels wrong."
            )

            print(
                "The client has provided incomplete information."
            )

            print()

            print("1. Investigate the Client")
            print("2. Continue the Mission")
            print("3. Walk Away")

            mission_choice = input(
                "\nChoose an action: "
            ).strip()


            if mission_choice == "1":

                if check_energy(20):

                    use_energy(20)

                    print()

                    system_message(
                        "Investigating client records..."
                    )

                    time.sleep(0.5)

                    system_message(
                        "Searching fictional databases..."
                    )

                    time.sleep(0.5)

                    warning_message(
                        "Client identity appears suspicious."
                    )

                    add_xp(60)
                    add_heat(15)

                    print()

                    print(
                        "You discovered evidence of a double cross."
                    )

                    pause()


            elif mission_choice == "2":

                if check_energy(35):

                    use_energy(35)

                    print()

                    system_message(
                        "Continuing operation..."
                    )

                    time.sleep(0.5)

                    warning_message(
                        "Unusual activity detected."
                    )

                    time.sleep(0.4)

                    roll = random.randint(1, 100)

                    success_chance = 25 + (level * 8)

                    if roll <= success_chance:

                        success_message(
                            "Operation successful!"
                        )

                        add_xp(80)
                        add_money(1000)
                        add_heat(30)

                        print()

                        print(
                            "You completed the operation."
                        )

                        current_mission += 1

                    else:

                        error_message(
                            "The operation failed."
                        )

                        add_heat(45)

                    pause()


            elif mission_choice == "3":

                print()

                print(
                    "You walked away from the contract."
                )

                remove_heat(15)

                current_mission += 1

                pause()


            else:

                error_message(
                    "Invalid choice."
                )

                pause()


        # Mission 5.

        elif current_mission == 5:

            print(
                color(
                    "MISSION 5: FINAL OPERATION",
                    CYAN
                )
            )

            line()

            print()

            print("TARGET: CLASSIFIED")
            print("DIFFICULTY: EXTREME")
            print("REWARD: $2,000")

            print()

            print(
                "This is your final contract."
            )

            print(
                "Everything you've learned has led to this moment."
            )

            print()

            print("1. Proceed Carefully")
            print("2. Take the Risk")

            mission_choice = input(
                "\nChoose an action: "
            ).strip()


            if mission_choice == "1":

                if check_energy(40):

                    use_energy(40)

                    print()

                    system_message(
                        "Running final analysis..."
                    )

                    time.sleep(0.5)

                    system_message(
                        "Reviewing security architecture..."
                    )

                    time.sleep(0.5)

                    system_message(
                        "Planning operation..."
                    )

                    time.sleep(0.5)

                    roll = random.randint(1, 100)

                    success_chance = 45 + (level * 6)

                    if roll <= success_chance:

                        success_message(
                            "Operation successful!"
                        )

                        add_xp(100)
                        add_money(2000)
                        add_heat(25)

                        current_mission += 1

                    else:

                        error_message(
                            "Operation failed."
                        )

                        add_heat(35)

                    pause()


            elif mission_choice == "2":

                if check_energy(50):

                    use_energy(50)

                    print()

                    warning_message(
                        "Initiating high-risk operation..."
                    )

                    time.sleep(0.5)

                    warning_message(
                        "Maximum security response detected!"
                    )

                    time.sleep(0.5)

                    roll = random.randint(1, 100)

                    success_chance = 25 + (level * 8)

                    if roll <= success_chance:

                        success_message(
                            "Incredible! Operation successful!"
                        )

                        add_xp(150)
                        add_money(2000)
                        add_heat(50)

                        current_mission += 1

                    else:

                        error_message(
                            "Operation failed."
                        )

                        warning_message(
                            "Emergency shutdown initiated."
                        )

                        add_heat(50)

                    pause()


            else:

                error_message(
                    "Invalid choice."
                )

                pause()


    # View stats.

    elif choice == "2":

        show_header()

        show_stats()

        pause()


    # Rest.

    elif choice == "3":

        print()

        system_message(
            "Returning to safe house..."
        )

        time.sleep(0.5)

        system_message(
            "Resting..."
        )

        time.sleep(0.8)

        restore_energy()

        remove_heat(5)

        success_message(
            "Heat reduced slightly."
        )

        pause()


    # Quit.

    elif choice == "4":

        print()

        system_message(
            "Disconnecting from simulation..."
        )

        time.sleep(0.5)

        print(
            "Thanks for playing."
        )

        game_running = False

        pause()


    else:

        error_message(
            "Invalid choice. Please select 1, 2, 3, or 4."
        )

        pause()


# Final results.

if current_mission > total_missions:

    print()

    show_header()

    print()

    print(
        color(
            "             ALL MISSIONS COMPLETE",
            MAGENTA
        )
    )

    print()

    print(
        "Congratulations,",
        color(player_name + "!", CYAN)
    )

    print()

    print(
        "You completed the Hacker Simulator campaign."
    )

    print()

    print("FINAL STATS")

    line()

    print("LEVEL:", level)

    print("XP:", xp)

    print(
        "MONEY:",
        color("$" + str(money), GREEN)
    )

    print(
        "HEAT:",
        color(str(heat) + "%", get_heat_color())
    )

    print(
        "ENERGY:",
        color(str(energy) + "%", get_energy_color())
    )

    line()


    # The player's final heat determines the ending.

    if heat <= 25:

        print()

        print(
            color(
                "ENDING: THE GHOST",
                GREEN
            )
        )

        print()

        print(
            "You completed the campaign while keeping"
        )

        print(
            "your activity almost completely undetected."
        )


    elif heat <= 60:

        print()

        print(
            color(
                "ENDING: THE OPERATOR",
                CYAN
            )
        )

        print()

        print(
            "You took risks, but successfully completed"
        )

        print(
            "your contracts and built a reputation."
        )


    elif heat <= 85:

        print()

        print(
            color(
                "ENDING: HIGH PROFILE",
                YELLOW
            )
        )

        print()

        print(
            "Your success came with a price."
        )

        print(
            "Your activity attracted significant attention."
        )


    else:

        print()

        print(
            color(
                "ENDING: BURNED",
                RED
            )
        )

        print()

        print(
            "You completed the campaign, but your heat"
        )

        print(
            "level became extremely high."
        )


    print()

    line()

    print(
        color(
            "SIMULATION COMPLETE",
            MAGENTA
        )
    )

    line()

    input("\nPress Enter to exit...")
