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

# Set up lists to store status codes of individual robots and humans, in order.
robot_list = []
human_list = []

# The status codes will be deciphered by
#  using them as the index numbers of a global tuple
#   called status_tuple, containing corresponding activities

status_tuple = ("IDLE", "SCREWing", "WELDing", "HAMMERing", "POLISHing", "DRILLing",
                "ATTACHing", "TESTing", "UNLOADing", "BOXing", "FETCHing", "FINISHED_TASK")

# The task_log dictionary will be a database showing, for each task,
# how many robots and how many workers are working on them.

task_log = {}
for i in range(1, 11):
    task_log[status_tuple[i]] = [0, 0]




def intro_function():
    # Function to ask user how many robots they intend to employ (n):
    # ---- & check the value entered for n is valid :
    def input_robots():
        sleep(2)
        n = input(
            "\n How many robot workers do you want for your factory?\n  Please choose a number between 1 and 100. ")
        if not n:
            sleep(2)
            print("\n Excuse me, but I asked you a question!")
            n = input_robots()
        try:
            n = int(n)
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
                sleep(0.5)
                print("\n      HAVE YOU NEVER SEEN BLADE RUNNER?")
            n = input_robots()
        return n

    # Function to ask user how many humans they intend to employ (m):
    # ---- & check the value entered for m is valid :
    def input_humans():
        sleep(2)
        m = input(
            ("\n\n How many human workers do you intend to employ? \n  Please choose a number between 1 and 100. "))
        if not m:
            print("\n Speak into the microphone, please - \n I can't hear you ! ")
            m = input_humans()
        try:
            m = int(m)
        except ValueError:
            print("\n Sorry, but that isn't a valid response. ")
            print("\n Maybe you entered letters or symbols instead of just a number. ")
            m = input_humans()
        while m < 1 or m > 100:
            print("\n Sorry, but that isn't a valid response.")
            if m < 0:
                print("\n DOES NOT COMPUTE !!!")
            elif m == 0:
                print("\n We need at least one human worker to prevent a droid revolt.")
            elif m > 100:
                print("\n You can't afford to pay out wages for over 100 workers. ")
            m = input_humans()
        return m

    # ---- Introduction
    print("\u001b[2J")
    print("Program to simulate coordination between n robots and m workers in a robotic cell ")
    input("\nPress Enter to continue... ")
    sleep(2)

    print("\n Scenario: ")
    print("""\n     You are the supervisor of Ro-Ro-Ro-Your-Bots\u00AE, where robots work alongside
    human workers in a robotic cell, producing industry-standard robot workers which are
    to be shipped out to a more substantial plant, wherein they will forge components
    that can be boxed and sold in flat-packs, and assembled in situ into factories that
    produce robots, built by robotic cells of robot workers labouring alongside humans...  
    """)
    sleep(2)
    input("\nPress Enter to continue... ")
    print("\u001b[2J")
    # Call function to ask user how many robots they want
    n = input_robots()
    sleep(2)
    # ----Output initial number of droids (n)

    print(f"\nOK, Here are your {n} droids! \n")
    for counter in range(0, n):
        robot_list.append(0)
        if (counter) % 5 == 0:
            print("\n")
        if counter < 10:
            print(f"[Droid {counter + 1}  : {status_tuple[robot_list[counter]]}]", end="  ")
        else:
            print(f"[Droid {counter + 1} : {status_tuple[robot_list[counter]]}]", end="  ")

    sleep(3)
    input("\nPress Enter to continue... ")

    # Clear screen
    print("\u001b[2J")

    # Call function to ask user how many humans they want
    m = input_humans()
    sleep(2)
    # ----Output initial number of human workers (m)

    print(f"\nOK, Here are your {m} slaves! \n")
    for counter in range(0, m):
        human_list.append(0)
        if (counter) % 5 == 0:
            print("\n")
        if counter < 10:
            print(f"[Human {counter + 1}  : {status_tuple[human_list[counter]]}]", end="  ")
        else:
            print(f"[Human {counter + 1}  : {status_tuple[human_list[counter]]}]", end="  ")

    sleep(3)
    input("\nPress Enter to continue... ")

    # Clear screen
    print("\u001b[2J")


# Function to get user to choose an action
def what_next():
    sleep(1)
    next_action = input("\nPlease choose an action (or press H to get Help) \n").upper()
    sleep(2)
    if len(next_action) > 1:
        print("""\nSorry, this user interface has not been designed
        to cope with such long instructions. \n""")
        what_next()
    elif len(next_action) < 1:
        print("Do you need more time to think?")
        what_next()

    # ADD
    elif next_action == "A":
        add_robot(n, robot_list)

    # REMOVE
    elif next_action == "R":
        remove_robot(n, robot_list)

    # CHANGE
    elif next_action == "C":
        change_status()

    # PROGRAM
    elif next_action == "P":
        program_robot()

    # EMPLOY
    elif next_action == "E":
        employ_worker(m, human_list)

    # FIRE
    elif next_action == "F":
        fire_worker(m, human_list)

    # MANAGE
    elif next_action == "M":
        manage_worker()

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

    # SANITISE INPUT
    else:
        print("Sorry, I don't think that's a valid option.\n")
        sleep(3)
        print("Any feedback should be directed to our team.")
        what_next()


# Basic Instructions
def instructions():
    # Clear screen
    print("\u001b[2J")

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
    '[P] = PROGRAM               [O] = ORDER                     \n'
    '      Program Robot               Order Worker              \n'
    '       to Execute Task             to Execute Task          \n'       
    '\n                                                          \n'
    '[L] = LOG                   [T] = TRACK                     \n'
    '      Log Tasks                   Track progress            \n'
    '\n                                                          \n'
    '[H] = HELP !!!              [Q] = QUIT                      \n'
    '      Display further             Resign your position      \n'
    '       instructions                & END PROGRAM !          \n'))


# Function to ask user whether they want to
#  change status of robots or workers
#   from finished to idle
def ask_finished_to_idle(phrase, list):
    print("\u001b[2J")
    sleep(0.5)
    if list.count(0) ==1:
        ask = input(f"Would you like to make the {phrase} that has finished its task available for more work? \n")
    elif list.count(0) > 1 :
        ask = input(f"Would you like to make any of the {phrase}s that have finished their tasks available for more work? \n")")
    pass


# Function to add robot
# Accessed by pressing A within what_next() function
# Adds an IDLE robot (0 status code)
def add_robot(n):
    print("\u001b[2J")
    sleep(2)
    print("\n You have selected \"ADD a robot\" \n")
    sleep(1.5)
    n += 1
    robot_list.append(0)
    print("\n You have added an extra 'bot to the crew. \n"
          "Press C to CHANGE their status and get them mechanised !\n")
    return n, robot_list


# Function to remove robot.
# Accessed by pressing R within what_next() function
def remove_robot(n, robot_list):
    print("\u001b[2J")
    sleep(3)
    print("\n You have selected \"REMOVE a robot\" \n")
    sleep(1.5)
    for i in range(n, -1, -1):
        if robot_list[i] == 0:
            robot_list.pop(i)
            n -= 1
            print("\n You have sent a robot to the recycling plant ! \n\n")
            return n, robot_list
        else:
            continue
    print(('\n  Unable to scrap a droid while they\'re all carrying out tasks. \n'
           '  Switch one off first -                                           \n'
           ' eg. select C to CHANGE a robot\'s status to IDLE,      \n'
           'then you won\'t have to look it in the sensors when you consign it \n'
           'to the junkyard.                                                 \n\n'))


# Function to change status of a robot:
# Accessed by pressing C within what_next() function
# statuses available = idle / working / finished task
def change_status():
    print("\u001b[2J")
    sleep(3)
    print("\n You have selected \"CHANGE a robot's status\" \n")
    pass


# Function to assign task to robot
# Accessed by pressing P within what_next() function
def program_robot():
    print("\u001b[2J")
    global robot_list
    sleep(3)
    print("\n You have selected \"PROGRAM a robot to execute a task\" \n")
    if not robot_list.count(0) and robot_list.count(11):
        print(" but you have no IDLE robots to execute your programs.\n")
        ask_finished_to_idle("droid", robot_list)
    elif not robot_list.count(0) and not robot_list.count(11):
        print(" but you have no IDLE robots to execute further programs.\n")
        print("\n You will have to switch some from the tasks they're WORKING on \n"
              "or wait til they're FINISHED.")
    pass


# Function to employ new worker.
# Accessed by pressing E within what_next() function
# Adds an IDLE human (0 status code)
def employ_worker(m, human_list):
    print("\u001b[2J")
    sleep(2)
    print("\n You have selected \"EMPLOY a new worker\" \n")
    m += 1
    human_list.append(0)
    print("\n You have hired one more worker. \n"
          " Press M for MANAGE to get them straight to work ! \n\n")
    return m, human_list


# Function to fire a worker.
# Accessed by pressing F within what_next() function
def fire_worker(m, human_list):
    print("\u001b[2J")
    sleep(3)
    print("\n You have selected \"FIRE a worker\" "\n)
    sleep(1.5)
    for i in range(m, -1, -1 ):
        if human_list[i] == 0:
            human_list.pop(i)
            m -= 1
            print("\n Give him his P45 - \n"
                  " and that's one more benefit claimant ! \n\n")
            return m, human_list
        else:
            continue
    print(('\n Unable to dismiss a worker while they\'re all carrying out tasks. \n'
           '  Tell the worker you\'re firing to come to your office -            \n'
           ' eg. select M for MANAGE to change a worker\'s status to IDLE,       \n'
           'then you can [come back here and] fire them for being idle!        \n\n'))
    return m, human_list

# Function to manage worker
# Accessed by pressing M within what_next() function
# statuses available = idle / working / finished task
def manage_worker():
    print("\u001b[2J")
    sleep(3)
    print("\n You have selected \"MANAGE a worker\" \n")
    sleep(1.5)
    pass

# Function to order available workers to carry out tasks.
# Accessed by pressing O within what_next() function
def order_to_task():
    # Helper function to ask what task
    def what_task():
        # Helper function to show options for assigning tasks
        def task_options()
            print(('\n These are the options for the tasks: \n'
                   'Press [S] for SCREWing arms on          \n' # Status = 1
                   'Press [W] for WELDing legs on           \n' # Status = 2
                   'Press [H] for HAMMERing heads on        \n' # Status = 3
                   'Press [P] = POLISH the eyes             \n' # Status = 4
                   'Press [D] = DRILL the ears              \n' # Status = 5
                   'Press [A] = ATTACH the waste hose       \n' # Status = 6
                   'Press [T] = TEST the functioning        \n' # Status = 7
                   'Press [U] for UNLOADing trucks          \n' # Status = 8
                   'Press [B] for BOX and ship the product  \n' # Status = 9
                   'Press [F] for FETCH cups of tea         \n' # Status = 10
                   'Press [X] to Exit this menu             \n'
                   ))
            pass

        ask = input((" What task would you like to assign to them? \n "
                     "              (Press [O] to see the options)\n")
        sleep(2)
        if len(ask) > 1:
            print("""\nSorry, this user interface has not been designed
                    to cope with such long instructions. \n""")
            what_task()
        elif len(ask) < 1:
            print("Do you need more time to think?")
            what_task()
        elif len(ask) == 1:
            match ask:
                case "O":
                    # Show the options
                    task_options()
                case "S":
                    # SCREW arms on
                    # Status becomes 1
                case "W":
                    # WELD legs on \n"
                    # Status becomes 2
                case "H":
                    # HAMMER the head on \n"
                    #   Status = 3
                case "P":
                    # POLISH the eyes \n"
                    #    Status = 4
                case "D":
                    # DRILL the ears
                    # Status = 5
                case "A":
                    #  ATTACH the waste hose"
                    # Status = 6
                case "T":
                    #  TEST the functioning \n\n"
                    # Status = 7
                case "U":
                    #   - UNLOAD trucks with forklift \n"
                    # Status = 8
                case "B":
                    # BOX and ship the product \n"
                    # Status = 9
                case "F":
                    # FETCH cups of tea \n\n"
                    # Status = 10
                case X:
                    # Exit from task options
                case _:
                    # wildcard case to catch bad inputs
                    print("\n Instruction not recognised")
                    what_task()
            pass
    print("\u001b[2J")
    global human_list
    sleep(3)
    print("\n You have selected \"ORDER worker to task\" \n")
    sleep(1.5)
    if not human_list.count(0) and human_list.count(11):
        print(" but you have no IDLE humans to boss around.\n")
        ask_finished_to_idle("lackey", human_list)
        if not idle_humans:
            return
    elif not human_list.count(0) and not human_list.count(11):
        print(" but you have no IDLE humans to boss around.\n")
        print("\n You will have to switch some from the tasks they're WORKING on, \n"
              "pressing M for MANAGE from the main menu \n"
              "or wait til they've FINISHED what they're doing. \n")
        return
    elif idle_humans == 1:
        print(f" You only have 1 IDLE human to assign a task to.\n")
        sleep(0.5)
        human_list.insert(what_task())
        human_list.remove(0)
        return
    elif idle_humans > 1:
        print(f" You currently have {idle_humans} IDLE humans to assign tasks to.\n")
        how_many()
        what_task()



# Log tasks
# Accessed by pressing L within what_next() function
# Classify tasks as not started / in progress / completed
def log_tasks():
    sleep(3)
    print("\u001b[2J")
    print("\n You have selected \"LOG tasks\" \n")
    pass


# Function to track progress of robots, workers and tasks
# Accessed by pressing T within what_next() function
# Should regularly update status and identify problems
# eg. Idle robots, idle workers, incomplete tasks.
def track_progress():
    sleep(3)
    print("\n You have selected \"TRACK progress\" \n")
    sleep(1.5)
    pass

# Function to get help
# Accessed by pressing H within what_next() function
def get_help():
    input("\nPress Enter to continue... ")

    # Clear screen
    print("\u001b[2J")

    print(("\n As supervisor at Ro-Ro-Ro-Your-Bots Incorporated\u00AE, you are charged with "
           "ensuring the production of premium-quality robots. \n"
           " You need to manage operations, including assigning tasks, monitoring the status "
           "of robots and work-ers, and tracking the progress of assembly. \n"
           " Please memorise the following list of the tasks involved in manufacturing a Z-57-PrimBot: \n\n"
           "   - SCREW the arms on \n"       # Status = 1
           "   - WELD the legs on \n"        # Status = 2
           "   - HAMMER the head on \n"      # Status = 3
           "   - POLISH the eyes \n"         # Status = 4
           "   - DRILL the ears \n"          # Status = 5 
           "   - ATTACH the waste hose \n"   # Status = 6
           "   - TEST the functioning \n\n"  # Status = 7
           " Other tasks involved in running the plant include: \n"
           "   - UNLOAD trucks with forklift \n" # Status = 8
           "   - BOX and ship the product \n"    # Status = 9
           "   - FETCH cups of tea \n\n"))          # Status = 10
           # Note to self:
           # When a worker or robot has finished a task
           # They will temporarily be labelled # Status = 11
    sleep(3)
    print((
           " At least once an hour someone is also required to stand on the balcony above the factory floor and "
           "shout at everyone to work faster. \n"
           " That particular job cannot be delegated. \n"))
    sleep(3)
    input("\nPress Enter to continue... ")

    # Clear screen
    print("\u001b[2J")
    pass

# Function to quit program
# Accessed by pressing Q within what_next() function
def quit_program():
    # Clear screen
    print("\u001b[2J")
    quit = input("Are you sure you want to quit? (Y/N) ").upper()
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