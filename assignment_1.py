# Ro-Ro-Ro-Your-Bots Incorporated

# Program to simulate coordination between n robots and m workers in a cell.

# Import modules

from time import sleep

# Use this to get program to sleep for 10 milliseconds:
# sleep(0.01)


# ---- Initialise main variables

# n = number of robots
n = 0

# m = number of workers
m = 0

# Set up lists to store status codes of robots and humans:
robot_list = []
human_list = []

def intro_function():
    # Function to ask user how many robots they intend to employ (n):
    # ---- & check the value entered for n is valid :
    def input_robots():
        try:
            n = int(input(
                "\n How many robot workers do you want for your factory?\n  Please choose a number between 1 and 100. "))
        except ValueError:
            print("\n Sorry, but that isn't a valid response.")
            print("\n Maybe you entered letters or symbols instead of just a number.")
            n = input_robots()
        while n < 1 or n > 100:
            print("\n Sorry, but that isn't a valid response.")
            if n < 0:
                print("\n How can we have a negative amount? We don't owe nobody our robots !!")
            elif n == 0:
                print("\n We can't build robots with no robots to build them.")
            elif n > 100:
                print("\n We can't risk having that many droids onsite.")
                print("\n      HAVE YOU NEVER SEEN BLADE RUNNER?")
            n = input_robots()
        return n

    # Function to ask user how many humans they intend to employ (m):
    # ---- & check the value entered for m is valid :
    def input_humans():
        try:
            m = int(
            input("\n\n How many human workers do you intend to employ?\n  Please choose a number between 1 and 100. "))
        except ValueError:
            print("\n Sorry, but that isn't a valid response.")
            print("\n Maybe you entered letters or symbols instead of just a number.")
            m = input_humans()
        while m < 1 or m > 100:
            print("\n Sorry, but that isn't a valid response.")
            if m < 0:
                print("\n DOES NOT COMPUTE !!!")
            elif m == 0:
                print("\n We need at least one human worker to prevent a droid revolt.")
            elif m > 100:
                print("\n You can't afford to pay out wages for over 100 workers.")
            m = input_humans()
        return m

    # Helper function to print out status of a robot or human
    def get_status(stat_code):
        if stat_code == 0:
            status = "Idle"
        elif stat_code == 1:
            status = "SCREWing"
        elif stat_code == 2:
            status = "WELDing"
        elif stat_code == 3:
            status = "HAMMERing"
        elif stat_code == 4:
            status = "POLISHing"
        elif stat_code == 5:
            status = "DRILLing"
        elif stat_code == 6:
            status = "ATTACHing"
        elif stat_code == 7:
            status = "TESTing"
        elif stat_code == 8:
            status = "UNLOADing"
        elif stat_code == 9:
            status = "BOXing"
        elif stat_code == 10:
            status = "MAKing"
        return status

    # ---- Introduction

    print("Program to simulate coordination between n robots and m workers in a robotic cell")
    input("\nPress Enter to continue...")

    print("\n Scenario:")
    print("""\n     You are the supervisor of Ro-Ro-Ro-Your-Bots\u00AE, where robots work alongside
    human workers in a robotic cell, producing industry-standard robot workers which are
    to be shipped out to a more substantial plant, wherein they will forge components
    that can be boxed and sold in flat-packs, and assembled in situ into factories that
    produce robots, built by robotic cells of robot workers labouring alongside humans... 
    """)

    input("\nPress Enter to continue...")

    # Call function to ask user how many robots they want
    n = input_robots()

    # ----Output initial number of droids (n)

    print(f"\nOK, Here are your {n} droids!\n")
    for counter in range(0, n):
        robot_list.append(0)
        if (counter) % 5 == 0:
            print("\n")
        if counter < 10:
            print(f"[Droid {counter + 1}  : {get_status(robot_list[counter])}]", end="  ")
        else:
            print(f"[Droid {counter + 1} : {get_status(robot_list[counter])}]", end="  ")

    # Call function to ask user how many humans they want
    m = input_humans()

    # ----Output initial number of human workers (m)

    print(f"\nOK, Here are your {m} slaves!\n")
    for counter in range(0, m):
        human_list.append(0)
        if (counter) % 5 == 0:
            print("\n")
        if counter < 10:
            print(f"[Human {counter + 1}  : {get_status(human_list[counter])}]", end="  ")
        else:
            print(f"[Human {counter + 1} : {get_status(human_list[counter])}]", end="  ")

    input("\n\nPress Enter to continue...")


# Function to get user to choose an action
def what_next():
    print()
    next_action = input("Please choose an action (or press H to get Help)").upper()
    sleep(5)
    if len(next_action) > 8:
        print("""Sorry, this user interface has not been designed
        to cope with such long instructions.""")
        what_next()

    # ADD
    elif next_action == "A":
        add_robot(n)

    # REMOVE
    elif next_action == "R":
        remove_robot(n)

    # CHANGE
    elif next_action == "C":
        change_status()

    # EMPLOY
    elif next_action == "E":
        employ_worker(m)

    # FIRE
    elif next_action == "F":
        fire_worker(m)

    # MANAGE
    elif next_action == "M":
        monitor_status()

    # ORDER
    elif next_action == "O":
        order()

    # LOG
    elif next_action == "L":
        log_tasks()

    # TRACK
    elif next_action == "T":
        track_progress()

    # HELP
    elif next_action == "H":
        get_help()

    # QUIT
    elif next_action == "Q":
        quit_program()

    else:
        print("Sorry, I don't think that's a valid option.")
        print("Any feedback should be directed to our team.")
        what_next()

# Instructions for Supervisor
# Accessed by pressing H within what_next() function
def instructions():
    print((
    '\n\n    - - Instructions for how to oversee production - -  \n' 
    '                    at                                      \n'
    '    - -  Ro-Ro-Ro-Your-Bots Incorporated: - -               \n'
    '\n                                                          \n'
    ' When prompted as to what options are available to you,     \n'
    '     press a key from these available alternatives          \n'
    '          to select from its sub-menu:                      \n'
    '\n                                                          \n'
    '[A] = ADD                   [E] = EMPLOY                    \n'
    '      Add Robot(s)                Employ Worker(s)          \n'
    '\n                                                          \n'
    '[R] = REMOVE                [F] = FIRE                      \n'
    '      Remove Robot(s)             Fire Worker(s)            \n'
    '\n                                                          \n'
    '[C] = CHANGE                [M] = MANAGE                    \n'
    '      Change Robot Status         Manage Worker Status      \n'
    '\n                                                          \n'
    '[O] = ORDER                                                 \n'
    '      Order To Carry Out Task                               \n'
    '\n                                                          \n'
    '[L] = LOG                   [T] = TRACK                     \n'
    '      Log Tasks                   Track progress            \n'
    '\n                                                          \n'
    '[H] = HELP !!!              [Q] = QUIT                      \n'
    '      Display further             Resign your position      \n'
    '       instructions                & END PROGRAM !          \n'))


# Function to add robot
# Accessed by pressing A within what_next() function
def add_robot(n):
    n += 1


# Function to remove robot.
# Accessed by pressing R within what_next() function
def remove_robot(n):
    n -= 1


# Function to change status of a robot:
# Accessed by pressing C within what_next() function
# statuses available = idle / working / finished task
def change_status():
    pass


# Function to employ new worker.
# Accessed by pressing E within what_next() function
def employ_worker(m):
    m += 1


# Function to fire a worker.
# Accessed by pressing F within what_next() function
def fire_worker(m):
    m -= 1


# Function to manage worker
# Accessed by pressing M within what_next() function
# statuses available = idle / working / finished task
def manage_worker():
    pass

# Function to order available robots and workers to carry out tasks.
# Accessed by pressing O within what_next() function
def order_to_task():
    pass


# Log tasks
# Accessed by pressing L within what_next() function
# Classify tasks as not started / in progress / completed
def log_tasks():
    pass


# Function to track progress of robots, workers and tasks
# Accessed by pressing T within what_next() function
# Should regularly update status and identify problems
# eg. Idle robots, idle workers, incomplete tasks.
def monitor_status():
    pass

# Function to get help
# Accessed by pressing H within what_next() function
def get_help():
    print(("\n As supervisor at Ro-Ro-Ro-Your-Bots Incorporated\u00AE, you are charged with ensuring the production"
           " of premium-quality robots.\n"
           " You need to manage operations, including assigning tasks, monitoring the status of robots and work-ers,"
           " and to track the progress of assembly.\n"
           " Please memorise the following list of the tasks involved in manufacturing a Z-57-PrimBot:\n\n"
           "   - SCREW the arms on\n"       # Status = 1
           "   - WELD the legs on\n"        # Status = 2
           "   - HAMMER the head on\n"      # Status = 3
           "   - POLISH the eyes\n"         # Status = 4
           "   - DRILL the ears\n"          # Status = 5 
           "   - ATTACH the waste hose\n"   # Status = 6
           "   - TEST the functioning\n\n"  # Status = 7
           " Other tasks involved in running the plant include:\n"
           "   - UNLOAD trucks with forklift\n" # Status = 8
           "   - BOX and ship the product\n"    # Status = 9
           "   - MAKE cups of tea\n\n"          # Status = 10
           " At least once an hour someone is also required to stand on the balcony above the factory floor and"
           " shout at everyone to work faster.\n"
           " That particular job cannot be delegated.\n"))


# Function to quit program
# Accessed by pressing Q within what_next() function
def quit_program():
    quit = input("Are you sure you want to quit? (Y/N)").upper()
    if quit == "Y":
        exit()
    elif quit == "N":
        what_next()


################################# --- BODY OF PROGRAM --- ################################

# Set console colours using ANSI escape codes:
print("\u001b[43m")
print("\u001b[30m")

# Intro
intro_function()

# Display Instructions initially
instructions()

# Call function to ask for user action
what_next()