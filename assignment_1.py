# Ro-Ro-Ro-Your-Bots Incorporated

# Program to simulate coordination between n robots and m workers in a cell.

# Import modules

pass

# ---- Initialise main variables

# n = number of robots
n = 0

# m = number of workers
m = 0

""" Set up dictionaries to store current status of robots or humans.
    - This function's parameters allow it to be used for both
   robots and humans, as it is being passed the variables n or m
   and robot_status or human_status 
"""

robot_dict = {}

human_dict = {}


def dict_function(group_nmbr, dict_group, label):
    for r in range(1, group_nmbr + 1):
        dict_group[label + str(r)] = "Idle"
    return dict_group


# Function to get user to choose an action
def what_next():
    print()
    next_action = input("Please choose an action (or press H to get Help)").upper()
    if len(next_action) > 8:
        print("""Sorry, this user interface has not been designed\n
        to cope with such long instructions.""")
        what_next()

    # HELP
    elif next_action == "H":
        instructions()

    # QUIT
    elif next_action == "Q":
        quit_program()

    # ADD
    elif next_action == "A":
        add_robot()

    # REMOVE
    elif next_action == "R":
        remove_robot()

    # EMPLOY
    elif next_action == "E":
        employ_worker()

    # CHANGE
    elif next_action == "C":
        change_status()

    # FIRE
    elif next_action == "F":
        fire_worker()

    # MANAGE
    elif next_action == "M":
        monitor_status()

    # LOG
    elif next_action == "L":
        log_tasks()

    else:
        print("Sorry, I don't think that's a valid option.")
        print("Any feedback should be directed to our team.")
        what_next()

# Instructions for Supervisor
# Accessed by pressing H within what_next() function
def instructions():
    print(('\n\n    - - Instructions for how to oversee production - -            ' 
    '                    at                                      '
    '    - -  Ro-Ro-Ro-Your-Bots Incorporated: - -                 '
    '\n                                                          '
    ' When prompted as to what options are available to you,     '
    '     press a key from these available alternatives          '
    '          to select from its sub-menu:                      '
    '\n                                                          ' 
    '[A] = ADD                   [R] = REMOVE                    '
    '     Add Robot(s)                 Remove Robot(s)           '
    '\n                                                          '
    '[E] = EMPLOY                [F] = FIRE                      '
    '      Employ Worker(s)            Fire Worker(s)            '
    '\n                                                          '
    '[C] = CHANGE                [M] = MANAGE                    '
    '      Change Robot                Manage Worker             '
    '                Status                      Status          '
    '\n                                                          '
    '[L] = LOG                   [H] = HELP !!!                  '
    '      Log Tasks                   Display these instructions'
    '\n                                                          '
    '                [Q] = QUIT                                  '
    '                      Resign your position                  '
    '                               &                            '
    '                         END PROGRAM !\n                    '))


# Function to add robot
# Accessed by pressing A within what_next() function
def add_robot():
    n += 1


# Function to remove robot.
# Accessed by pressing R within what_next() function
def remove_robot():
    n -= 1


# Function to change status of a robot:
# Accessed by pressing C within what_next() function
# statuses available = idle / working / finished task
def change_status():
    pass


# Function to employ new worker.
# Accessed by pressing E within what_next() function
def employ_worker():
    m += 1


# Function to fire a worker.
# Accessed by pressing F within what_next() function
def fire_worker():
    m -= 1


# Function to track worker
# Accessed by pressing T within what_next() function
# statuses available = idle / working / finished task
def track_worker():
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


# Function to monitor progress of robots, workers and tasks
# Accessed by pressing M within what_next() function
# Should regularly update status and identify problems
# eg. Idle robots, idle workers, incomplete tasks.
def monitor_status():
    pass


# Function to quit program
def quit_program():
    quit = input("Are you sure you want to quit? (Y/N)").upper()
    if quit == "Y":
        exit()
    elif quit == "N":
        what_next()


################################# --- BODY OF PROGRAM --- ################################

# ---- Introduction

print("Program to simulate coordination between n robots and m workers in a robotic cell")
input("\nPress Enter to continue...")

print("\n Scenario:")
print("""\n You are the supervisor of Ro-Ro-Ro-Your-Bots, where robots work alongside
human workers in a robotic cell, producing industry-standard robot workers which are
to be shipped out to a more substantial plant, wherein they will forge components
that can be boxed and sold in flat-packs, and assembled in situ into factories that
produce robots, built by robotic cells of robot workers labouring alongside humans... 
""")

input("\nPress Enter to continue...")

# ----Ask user how many robots they intend to employ (n):
# ---- & check the value entered for n is valid :

n = int(input("\n How many robot workers do you want for your factory?\n  Please choose a number between 1 and 100. "))

while n < 1 or n > 100:
    print("\n Sorry, but that isn't a valid response.")
    if n < 0:
        print("\n How can we have a negative amount? We don't owe nobody our robots !!")
    elif n == 0:
        print("\n We can't build robots with no robots to build them.")
    elif n > 100:
        print("\n We can't risk having that many droids onsite.")
        print("\n      HAVE YOU NEVER SEEN BLADE RUNNER?")
    n = int(input("\n How many robot workers do you intend to employ?\n Please choose a number between 1 and 100. "))


# Call function to set up a dictionary storing the status of each robot:
robot_dict = dict_function(n, robot_dict, "Droid ")

# ----Output initial number of droids (n)

print(f"\nOK, Here are your {n} droids!\n")
for counter in range(1, n + 1):
    if (counter) % 10 == 0:
        print("\n")
    else:
        pass
    if counter < 10:
        print(f"[Droid {counter} : {robot_dict["Droid " + str(counter)]}]", end="   ")
    else:
        print(f"[Droid {counter} : {robot_dict["Droid " + str(counter)]}]", end="  ")


# ----Ask user how many humans they intend to employ (m):
# ---- & check the value entered for n is valid :

m = int(input("\n\n How many human workers do you intend to employ?\n  Please choose a number between 1 and 100. "))

while m < 1 or m > 100:
    print("\n Sorry, but that isn't a valid response.")
    if m < 0:
        print("\n DOES NOT COMPUTE !!!")
    elif m == 0:
        print("\n We need at least one human worker to prevent a droid revolt.")
    elif m > 100:
        print("\n You can't afford to pay out wages for over 100 workers.")
    m = int(input("\n\n How many human workers do you intend to employ?\n Please choose a number between 1 and 100. "))


# Call function to set up a dictionary storing the status of each human:
human_dict = dict_function(m, human_dict, "Human ")


# ----Output initial number of human workers (m)

print(f"\nOK, Here are your {m} slaves!\n")
for counter in range(1, m + 1):
    if (counter) % 10 == 0:
        print("\n")
    else:
        pass
    if counter < 10:
        print(f"[Human {counter} : {human_dict["Human " + str(counter)]}]", end="   ")
    else:
        print(f"[Human {counter} : {human_dict["Human " + str(counter)]}]", end="  ")


# Display Instructions initially
instructions()

# Call function to ask for user action
what_next()