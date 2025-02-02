# Ro-Ro-Ro-Your-Bots Incorporated

# Program to simulate coordination between n robots and m workers in a cell.

# Import modules

from time import sleep
# Use this to get program to pause for 1 second --> sleep(1)

# Global variables:
total_time = 0
seconds = 0
minutes = 0
hours = 0

# Time Sim function pauses the program for {secs} seconds
# and increments the virtual clock for the simulation,
# checking if the factory day has finished.

def time_sim(secs):
    global seconds, minutes, hours, total_time
    sleep(secs)
    total_time += 15

    if total_time == 86400:
        clear_screen()
        print("\n\n\n")
        print("A whole day of factory time has ended.\n"
              "You have run out of time to complete any more tasks.\n")
        end_sequence()

    else:
        return

# Function to clear screen and return cursor to top left corner
def clear_screen():
    # Clear screen using ANSI escape sequence
    print("\u001b[2J")
    # Cursor to home using ANSI escape sequence
    print("\u001b[H")


def intro_function():
    #################################### Introduction ###########################################

    # ---- Initialise main variables ---- #

    # n = number of robots
    n = 0

    # m = number of workers
    m = 0

    clear_screen()

    print("           Program to simulate coordination between n robots and m workers in a robotic cell \n")
    input("\n  Press Enter to continue... \n")
    time_sim(secs=1)

    print("\n Scenario: ")

    print("""\n     You are the supervisor of Ro-Ro-Ro-Your-Bots\u00AE, where robots work alongside
    human workers in a robotic cell, producing industry-standard robot workers which are
    to be shipped out to a more substantial plant, wherein they will forge components
    that can be boxed and sold in flat-packs, and assembled in situ into factories that
    produce robots, built by robotic cells of robot workers labouring alongside humans...  
    """)

    time_sim(secs=1)
    input("\n  Press Enter to continue... ")

    clear_screen()

    # Call function to ask user how many robots they want
    # and create variable to label additional robot later
    n, next_n = input_robots(n)

    # Output initial number of robot workers (n)
    n_dict = dict_maker(n, "Robot")
    dict_printer(n, n_dict)
    time_sim(secs=1)
    input("\n\n  Press Enter to continue... ")
    clear_screen()

    # Call function to ask user how many humans they want
    # and create variable to number additional employee later
    m, next_m = input_humans(m)

    time_sim(secs=1)

    # ----Output initial number of human workers (m)

    m_dict = dict_maker(m, "Human")
    dict_printer(m, m_dict)
    time_sim(secs=1)
    input("\n\n  Press Enter to continue... ")
    clear_screen()

    # -------------------the Task Log ----------------------------

    # task_log is a multi-dimensional list showing, for each task,
    # how many repetitions of that task have been completed
    # and whether any workers or robots are currently engaged in it

    #  It contains:
    # -------------> at index [0] => TASK CODES
    #  As each WORKING robot or worker is assigned to a specific task,


    #   Its task codes can be deciphered by
    #  using them as the index numbers of a tuple array
    #  containing corresponding activities,
    # as well as IDLE status at task code 0
    # and FINISHED at task code 11

    #  This means that it can be used to work out the status
    # of each human or robot, as any other code (1 - 10)
    # will come under the status of WORKING

    #   To print the short version of the code,
    #  access index 0 of the nested tuple,
    #  eg. "HAMMERing" = task_log[0][4][0]
    # Or to print the long version of the code,
    #  access index 1 of the nested tuple
    #  eg. "HAMMERing heads on            " = task_log[0][4][1])

    # ----------------------------------------------------- Task codes are:
    task_log=[(("IDLE     ", "IDLE                          "), #--> 00
                   ("SCREWing ", "SCREWing arms on              "), #--> 01
                   ("WELDing  ", "WELDing legs on               "), #--> 02
                   ("HAMMERing", "HAMMERing heads on            "), #--> 03
                   ("POLISHing", "POLISHing eyes                "), #--> 04
                   ("DRILLing ", "DRILLing ears                 "), #--> 05
                   ("ATTACHing", "ATTACHing waste hoses         "), #--> 06
                   ("TESTing  ", "TESTing the functioning       "), #--> 07
                   ("UNLOADing", "UNLOADing trucks with forklift"), #--> 08
                   ("BOXing   ", "BOXing and shipping product   "), #--> 09
                   ("FETCHing ", "FETCHing cups of tea          "), #--> 10
                   ("FINISHED ", "FINISHED_TASK                 "))] #--> 11

    # a lengthier mirror of the dictionaries containing the tasks
    # being worked on by each human and robot
    # contains the codes of these tasks
    # and is itself contained within the encyclopedic task_log
    #  - - - - - [1] = a dictionary of twelve keys, one for each task code:
    #  - - - - -    each value denotes how many robots are engaged in the task
    #               (or engaged in the IDLE-ness, for task codes 0 & 11
    #  - - - - - [2] = another dictionary, a mirror of it where
    #  - - - - -    each value denotes how many humans are engaged in the task

    for i in range(1, 3):
        task_log.append({})
        for j in range(0, 12):
            task_log[i][j] = 0

    # Task log also contains:
    #  - - - - - [3] = a dictionary of 12 lists,
    #  - - - - - - - -  each list holding the IDs of the robots
    #  - - - - - - - -  engaged in that task, eg. Robot_088
    #  - - - - - [4] = another dictionary of 12 lists, each holding
    #  - - - - - - -  **SURPRISE**: the IDs of the humans
    #  - - - - - - - - - - - - - - - engaged in that task

    for i in range(3, 5):
        task_log.append({})
        for j in range(0, 12):
            task_log[i][j] = []

    #  - - - - - [5] = a dictionary of twelve keys, one for each task code:
    #  - - - - -    each value holds its own dictionary, this time of
    #  - - - - -    three keys, the values being:
    #  - - - - -    number of tasks not started / in progress / completed

    task_log.append({})
    task_log[5] = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    for i in range(0, 12):
        task_log[5][i] =  {
                           "NOT STARTED": 0,
                           "IN PROGRESS": 0,
                           " COMPLETED ": 0,
                          }

    #  - - - - - [6] = a tuple with 12 (TASK, VALUE) pairs
    #  - - - - -    containing the amount of time needed to perform it.
    #  - - - - -     As "tasks" 0 and 11 actually represent IDLE
    #  - - - - -    and finished respectively, their value is zero

    task_log.append(((task_log[0][0][0], 0),
                     (task_log[0][1][0], 4),
                     (task_log[0][2][0], 4),
                     (task_log[0][3][0], 4),
                     (task_log[0][4][0], 4),
                     (task_log[0][5][0], 2),
                     (task_log[0][6][0], 2),
                     (task_log[0][7][0], 2),
                     (task_log[0][8][0], 8),
                     (task_log[0][9][0], 4),
                     (task_log[0][10][0], 1),
                     (task_log[0][11][0], 0)))

    #  - - - - - [7] = Another 12 values for respective tasks,
    #  - - - - -    showing how many repetitions of that task are
    #  - - - - -    needed to fulfil Head Office's directives.

    task_log.append(((task_log[0][0][1], 0),
                     (task_log[0][1][1], 10),
                     (task_log[0][2][1], 10),
                     (task_log[0][3][1], 10),
                     (task_log[0][4][1], 10),
                     (task_log[0][5][1], 10),
                     (task_log[0][6][1], 10),
                     (task_log[0][7][1], 5),
                     (task_log[0][8][1], 1),
                     (task_log[0][9][1], 5),
                     (task_log[0][10][1], 50),
                     (task_log[0][11][1], 0)))

    #  - - - - - [8] = Another 12 values for respective tasks,
    #  - - - - -    in a list this time (so it's mutable),
    #  - - - - -    showing for each task in progress
    #  - - - - -    its percentage til completion

    task_log.append([[task_log[0][0][1], 0],
                    [task_log[0][1][1], 0],
                    [task_log[0][2][1], 0],
                    [task_log[0][3][1], 0],
                    [task_log[0][4][1], 0],
                    [task_log[0][5][1], 0],
                    [task_log[0][6][1], 0],
                    [task_log[0][7][1], 0],
                    [task_log[0][8][1], 0],
                    [task_log[0][9][1], 0],
                    [task_log[0][10][1],0],
                    [task_log[0][11][1],0]])

    clear_screen()

    # Add initial numbers of humans and robots to Task Log
    task_log[1][0], task_log[2][0] = n, m

    for robot in n_dict:
        task_log[3][0].append(n_dict[robot])

    for human in m_dict:
        task_log[4][0].append(n_dict[robot])

    # Return primary variables to main body of program
    return n, m, n_dict, m_dict, next_n, next_m, task_log


# Function to ask user how many robots they intend to employ (n):
# ---- & check the value entered for n is valid :
def input_robots(n):
    time_sim(secs=1)
    while True:
        while not n:

            print("\n How many robot workers do you want for your factory?\n\n")

            n = input("  Please choose a number between 1 and 99. \n\n")
            time_sim(secs=1)
            if not n:
                print("\n Excuse me, but I asked you a question! \n")
                break

            try:
                n = int(n)
                if n >= 1 and n < 100:
                    return n, n + 1

                else:
                    print("\n Sorry, but that isn't a valid response. \n")
                    if n < 0:
                        print("\n How can we have a negative amount? We don't owe nobody our robots !!\n")
                    elif n == 0:
                        print("\n We can't build robots with no robots to build them. \n")
                    elif n > 99:
                        print("\n We can't risk having that many droids onsite. \n")
                        time_sim(secs=1)
                        print("\n      HAVE YOU NEVER SEEN BLADE RUNNER? \n")
                    n = 0
                    time_sim(secs=3)
                    clear_screen()

            except ValueError:
                print("\n Sorry, but that isn't a valid response. \n")
                print("\n Maybe you entered letters or symbols instead of just a number. \n")
                n = 0
                time_sim(secs=2)
                clear_screen()


# Function to ask user how many humans they intend to employ (m):
# ---- & check the value entered for m is valid :
def input_humans(m):
    time_sim(secs=1)
    while True:
        while not m:
            print("\n\n How many human workers do you intend to employ? \n")
            m = input("  Please choose a number between 1 and 99. \n\n")
            time_sim(secs=2)
            if not m:
                print("\n Speak into the microphone, please - \n I can't hear you ! \n")
                break

        try:
            m = int(m)
            if m >= 1 and m < 100:
                print("\n OK, I can work with that.\n")
                time_sim(secs=2)
                clear_screen()
                return m, m + 1

            else:
                print("\n Sorry, but that isn't a valid response.")
                if m < 0:
                    print("\n DOES NOT COMPUTE !!!")
                elif m == 0:
                    print("\n We need at least one human worker to prevent a droid revolt.")
                elif m > 99:
                    print("\n You can't afford to pay out wages for 100 workers. ")
                m = 0
                time_sim(secs=2)
                clear_screen()

        except ValueError:
            print("\n Sorry, but that isn't a valid response. \n")
            print("\n Maybe you entered letters or symbols instead of just a number. \n")
            m = 0
            time_sim(secs=2)
            clear_screen()


# Function to make dictionaries of robots or humans {n} or {m}
# Parameter {phrase} will state whether {Robot} or {Human}
#  "   "    {x_dict} will hold either {n_dict} --> robots
#                                  or {m_dict} --> as an argument
# Each worker will be given an initial status of 0 (eg. IDLE)
#  This will change to 1 when they are WORKING
# and to 2 when they are FINISHED
def dict_maker(x, phrase):
    if x == 1:
        print(f"\n Here is your 1 solitary {phrase}: \n")
        time_sim(secs=1)

    else:
        print(f"\n As promised, here are your {x} {phrase}s: \n")
        time_sim(secs=1)

    #  .zfill(x) formats a number as x digits,
    # ie. "Robot_001" or "Human_043"
    # as long as the number is formatted as a string first
    x_list = [phrase + "_" + str(counter).zfill(3) for counter in range(1, x + 1)]
    x_dict = {phrase: 0 for phrase in x_list}

    time_sim(secs=1)
    return x_dict


# Function to print dictionary of either humans or robots
def dict_printer(x, x_dict):
    key_number = 0
    for key in x_dict:
        if key_number % 5 == 0:
            print("\n")
        print(" " + key, end=" ")
        key_number += 1
    return


# Helper function to check input is a single character
def get_length(ask, max=1):
    if len(ask) > max:
        print("""\n Sorry, this user interface has not been designed
                to cope with such long instructions. \n""")
        return False

    elif len(ask) < 1:
        print("Do you need more time to think?")
        time_sim(secs=3)
        return False

    elif len(ask) <= max:
        return True


# Function to get user to choose an action
def what_next(a, b, a_dict, b_dict, next_a, next_b, tasks):
    while True:
        next_action = input("\nPlease choose an action : (or press H to get Help) \n").upper()
        time_sim(secs=1)
        tasks = updater(tasks)

        # check only 1 character was input
        if get_length(next_action):
            match next_action:

            # ADD
                case "A":
                    a, a_dict, next_a = add_robot(a, a_dict, next_a)
                    break

             # REMOVE
                case "R":
                    a, a_dict, next_a, tasks = remove_robot(a, a_dict, next_a, tasks)
                    break

             # CHANGE
                case "C":
                    a_dict = change_status(a_dict)
                    break

             # PROGRAM
                case "P":
                    a_dict, tasks = program_robot(a_dict, tasks)
                    break

             # EMPLOY
                case "E":
                    b, b_dict, next_b = employ_worker(b, b_dict, next_b)
                    break

             # FIRE
                case "F":
                    b, b_dict, next_b= fire_human(b, b_dict, next_b)
                    break

             # MANAGE
                case "M":
                    b_dict = manage_worker(b_dict)
                    break

             # ORDER
                case "O":
                    b_dict, tasks = order_worker(b_dict, tasks)
                    break

             # LOG
                case "L":
                    log_tasks(tasks)
                    break

             # TRACK
                case "T":
                    track_progress(a_dict, b_dict, tasks)
                    break

             # HELP
                case "H":
                    get_help()
                    break

             # QUIT
                case "Q":
                    quit_program()
                    break

            # SANITISE INPUT
                case _:
                    print("Sorry, I don't think that's a valid option.\n")
                    time_sim(secs=1)
                    tasks = updater(tasks)
                    print("Any feedback should be directed to our team.\n")
                    time_sim(secs=2)
                    tasks = updater(tasks)

        return a, b, a_dict, b_dict, next_a, next_b, tasks


# Main Options
def main_options():
    clear_screen()

    print((
    '\n\n       - - Instructions for how to oversee production - -  \n' 
    '                       at                                      \n'
    '       - -  Ro-Ro-Ro-Your-Bots Incorporated\u00AE: - -              \n'
    '\n                                                             \n'
    '    When prompted as to what options are available to you,     \n'
    '        press a key from these available alternatives          \n'
    '             to select from its sub-menu:                      \n'
    '\n                                                             \n'
    '   [A] = ADD                   [E] = EMPLOY                    \n'
    '         Add Robot(s)                Employ Worker(s)          \n'
    '\n                                                             \n'
    '   [R] = REMOVE                [F] = FIRE                      \n'
    '         Remove Robot(s)             Fire Worker(s)            \n'
    '\n                                                             \n'
    '   [C] = CHANGE                [M] = MANAGE                    \n'
    '         Change Robot Status         Manage Worker Status      \n'
    '\n                                                             \n'
    '   [P] = PROGRAM               [O] = ORDER                     \n'
    '         Program Robot               Order Worker              \n'
    '          to Execute Task             to Execute Task          \n'       
    '\n                                                             \n'
    '   [L] = LOG                   [T] = TRACK                     \n'
    '         Log Tasks                   Track progress            \n'
    '\n                                                             \n'
    '   [H] = HELP !!!              [Q] = QUIT                      \n'
    '         Display further             Resign your position      \n'
    '          instructions                & END PROGRAM !          \n'))


# Handling simple input errors during task selection
def simple_error():
    print(('\n An error seems to have occurred \n'
           'but it\'s nothing to worry about. \n\n'
           ' We can always build new factories / robots / people / supervisors... \n\n'))
    time_sim(secs=1)
    print("\n\nLet's take a step back shall we? \n")
    time_sim(secs=2)
    return


# Helper functions for changing tasks allocated:
# Function to show options for assigning tasks
def show_task_options(option_keys, task):
    time_sim(secs=1)
    print('\n These are the options for the tasks:    \n')
    for o in range(1, len(option_keys)):
        print(f' - Press [{o}] for {task[o][0]}')
    return


# Function for SCREWing arms on
# Accessed by pressing S within what_task() menu
# Creates a task_code of 1
def screw_arms():
    print("You have selected SCREW arms on.\n")
    task_code = 1
    return task_code


# Function for WELDing legs on
# Accessed by pressing W within what_task() menu
# Creates a task_code of 2
def weld_legs():
    print("You have selected WELD legs on.\n")
    task_code = 2
    return task_code


# Function for HAMMERing heads on
# Accessed by pressing H within what_task() menu
# Creates a task_code of 3
def hammer_heads():
    print("You have selected HAMMER heads on\n")
    task_code = 3
    return task_code


# Function for POLISHing the eyes
# Accessed by pressing P within what_task() menu
# Creates a task_code of 4
def polish_eyes():
    task_code = 4
    return task_code


# Function for DRILLing the ears
# Accessed by pressing D within what_task() menu
# Creates a task_code of 5
def drill_ears():
    print("You have selected DRILL ears.\n")
    task_code = 5
    return task_code


# Function for ATTACHing the waste hose
# Accessed by pressing A within what_task() menu
# Creates a task_code of 6
def attach_hose():
    print("You have selected ATTACH the waste hose\n")
    task_code = 6
    return task_code


# Function for TESTing the functioning
# Accessed by pressing T within what_task() menu
# Creates a task_code of 7
def test_functioning():
    print("You have selected TEST the functioning\n")
    task_code = 7
    return task_code


# Function for UNLOADing trucks
# Accessed by pressing U within what_task() menu
# Creates a task_code of 8
def unload_trucks():
    print("You have selected UNLOAD trucks\n")
    task_code = 8
    return task_code


# Function for BOXing and shipping the product
# Accessed by pressing B within what_task() menu
# Creates a task_code of 9
def box_product():
    print("You have selected BOX and ship the product\n")
    task_code = 9
    return task_code


# Function for FETCHing cups of tea
# Accessed by pressing F within what_task() menu
# Creates a task_code of 10
def fetch_tea():
    print("You have selected FETCH cups of tea\n")
    task_code = 10
    return task_code


# Helper function to determine what task
def what_task(tasks):
    options = ("O", "S", "W", "H", "P", "D", "A", "T", "U", "B", "F", "X")
    selected = False
    while selected == False:

        next_task = input((" What task would you like to assign to them? \n "
                           "              (Press [O] to see the options)\n")).upper()
        time_sim(secs=1)
        tasks = updater(tasks)
        if get_length(next_task):
            if next_task in options:
                selected = True
                next_task = options.index(next_task)

                #  Show how many staff are already engaged in the task
                # {tasks[1][_]} for robots, {tasks[2][_]} for humans
                # And adjust the task code for what_task(tasks) function

                if next_task == "O":
                    # Show OPTIONS
                    # Call show_task_options function
                    show_task_options(options, tasks[0])
                    selected = False

                else:
                    print(f"\n You have selected \"{tasks[0][next_task][0]}\". \n")
                    # Adjust for semantics of sentence

                    if tasks[1][next_task] or tasks[2][next_task]:
                        print(f" You already have {tasks[1][next_task]} robots", end="")
                        print(f"and {tasks[2][next_task]} humans {tasks[0][next_task][1]}")

                    else:
                        print(" You don't currently have any employees engaged in this task.")
                    # task_code changes
                    return next_task


#  Function to loop through robots or humans
# and display the tasks they're working on
#  {longshort} parameter should be set to either
# 0 or 1 depending on whether
# the short or long version of the task title is
# being printed
def task_printer(x_dict, task_codes, longshort):
    time_sim(secs=1)
    task_codes = updater(task_codes)
    if longshort == 0:
        per_line = 5
    else:
        per_line = 3
    key_number = 0

    for key, value in x_dict.items():
        if key_number % per_line == 0:
            print("\n")
        if key_number < 10:
            print(f"{key} : {task_codes[0][value][longshort]}", end="    ")
        elif key_number >= 10:
            print(f"{key} : {task_codes[0][value][longshort]}", end="   ")
        key_number += 1

    print("\n\n")


def return_status(drone):
    match drone:
        case 0:
            status = "  IDLE  "
        case 1:
            status = "WORKING "
        case 2:
            status = "FINISHED"
    return status


#  Function to loop through robots or humans
# and display their status, based on the value
# stored in the dictionary, cross-referenced with task_log[0]
#  The status will print as either
# IDLE, WORKING or FINISHED
def status_printer(x_dict):
    time_sim(secs=1)
    key_number = 0
    for key, value in x_dict.items():
        if key_number % 5 == 0:
            print("\n")
        print(f"{key} : " , end="")

        match value:
            case 0:
                print("  IDLE  ", end="   ")
            case 1:
                print("WORKING ", end="   ")
            case 2:
                print("FINISHED", end="   ")
        key_number += 1

    print("\n\n")


# Task log screen display
def show_log(task_log):
    global hours, minutes, seconds
    clear_screen()
    print((f'                                               ------------                                              \n'
           '===============================================| TASK LOG |==============================================\n'
           '| TIME :                       |               ------------                    ||         WORKERS       |\n'
           '|------------------------------|-----------------------------------------------||-----------------------|\n'
           '|------------: TASK : ---------| # NOT STARTED | # IN PROGRESS | # COMPLETED   ||   BOTS    ||  HUMANS  |\n'
           '|------------------------------|---------------|---------------|---------------||-----------||----------|\n'
           '| SCREWing on arms (pairs)     |               |               |               ||           ||          |\n'
           '|------------------------------|---------------|---------------|---------------||-----------||----------|\n'
           '| WELDing on legs (pairs)      |               |               |               ||           ||          |\n'
           '|------------------------------|---------------|---------------|---------------||-----------||----------|\n'
           '| HAMMERing on heads           |               |               |               ||           ||          |\n'
           '|------------------------------|---------------|---------------|---------------||-----------||----------|\n' 
           '| POLISHed eyes                |               |               |               ||           ||          |\n'
           '|------------------------------|---------------|---------------|---------------||-----------||----------|\n'
           '| DRILLed ears                 |               |               |               ||           ||          |\n'
           '|------------------------------|---------------|---------------|---------------||-----------||----------|\n'
           '| ATTACHed waste hoses         |               |               |               ||           ||          |\n'
           '|------------------------------|---------------|---------------|---------------||-----------||----------|\n'
           '| TESTed products              |               |               |               ||           ||          |\n'
           '|------------------------------|---------------|---------------|---------------||-----------||----------|\n'
           '| UNLOADed trucks              |               |               |               ||           ||          |\n'
           '|------------------------------|---------------|---------------|---------------||-----------||----------|\n'
           '| BOXes shipped                |               |               |               ||           ||          |\n'
           '|------------------------------|---------------|---------------|---------------||-----------||----------|\n'
           '| FETCHed cups of tea (100s)   |               |               |               ||           ||          |\n'
           '=========================================================================================================\n'
           ))

    # Use escape codes to send cursor to different screen positions
    #       \u001b[{line};{column}H
    #  OR   \u001b[{line};{column}f
    # Use \r and end="" to prevent new lines being added
    hours = total_time // 3600
    minutes = (total_time // 60) - (hours * 60)

    seconds = total_time - (hours * 3600) - (minutes * 60)
    # Print clock on line 4
    print(f"\u001b[4;12H{str(hours).zfill(2)} : {str(minutes).zfill(2)} : {str(seconds).zfill(2)} ")

    # Print number of tasks at each stage of completion for each particular job
    # : start cursor at 7, 41, eg. \u001b[7;41H
    for i in range(41, 74, 16):
        for j in range(8, 27, 2):
            match i:
                case 41:
                    stage = "NOT STARTED"
                case 57:
                    stage = "IN PROGRESS"
                case 73:
                    stage = " COMPLETED "
            print(f"\u001b[{j};{i}H{task_log[5][(j-5)//2][stage]}", end="")

    # Print how many robots are working on each task at column 86
    #   - Access the list of robots per task at task_log[1]
    # Print how many humans are working on each task at column 99
    #   - Access the list of humans per task at task_log[2]
    for i in range(86, 100, 13):
            match i:
                case 86:
                    body_type = 1
                case 99:
                    body_type = 2
                case _:
                    body_type = 1

#  If you don't know if it's a robot or a human, it's probably a robot !!

            for j in range(8, 27, 2):
                print(f"\u001b[{j};{i}H{task_log[body_type][(j-5)//2]}", end="")

    # Bring cursor beneath table
    print(f"\u001b[30;2H", end="")
    return


def show_tracker(n, m, n_dict, m_dict, task_log):

    # Helper function to print out data in columns:
    def column_printer(data, column):
        for row in range(9, 28, 2):
            print(f"\u001b[{row};{column}H{data}", end="")

    print(
        (f'                                              ----------------                                            \n'
         '==============================================| TASK TRACKER |============================================\n'
         '| TIME :                  | TOTAL    | BOTS  ----------------  || TOTAL      | HUMANS   |  HUMANS       |\n'
         '|-------------------------| BOTS:    | IDLE:    | FINISHED:    || HUMANS:    | IDLE:    | FINISHED:     |\n'
         '| % OF DAY REMAINING :    |-----------------------------------------------------------------------------|\n'
         '|-------------------------|  # NOT  ||  # IN    |  PROGRESS: || # TIMES   | % OF ||   BOTS   ||  HUMANS |\n'
         '|----------: TASK : ------| STARTED || PROGRESS | % COMPLETE || COMPLETED | GOAL || ON TASK  || ON TASK |\n'
         '|-------------------------|---------||----------|------------||-----------|------||----------||---------|\n'
         '| SCREWing on arms (pairs)|         ||          |            ||           |      ||          ||         |\n'
         '|-------------------------|---------||----------|------------||-----------|------||----------||---------|\n'
         '| WELDing on legs (pairs) |         ||          |            ||           |      ||          ||         |\n'
         '|-------------------------|---------||----------|------------||-----------|------||----------||---------|\n'
         '| HAMMERing on heads      |         ||          |            ||           |      ||          ||         |\n'
         '|-------------------------|---------||----------|------------||-----------|------||----------||---------|\n'
         '| POLISHed eyes           |         ||          |            ||           |      ||          ||         |\n'
         '|-------------------------|---------||----------|------------||-----------|------||----------||---------|\n'
         '| DRILLed ears            |         ||          |            ||           |      ||          ||         |\n'
         '|-------------------------|---------||----------|------------||-----------|------||----------||---------|\n'
         '| ATTACHed waste hoses    |         ||          |            ||           |      ||          ||         |\n'
         '|-------------------------|---------||----------|------------||-----------|------||----------||---------|\n'
         '| TESTed products         |         ||          |            ||           |      ||          ||         |\n'
         '|-------------------------|---------||----------|------------||-----------|------||----------||---------|\n'
         '| UNLOADed trucks         |         ||          |            ||           |      ||          ||         |\n'
         '|-------------------------|---------||----------|------------||-----------|------||----------||---------|\n'
         '| BOXes shipped           |         ||          |            ||           |      ||          ||         |\n'
         '|-------------------------|---------||----------|------------||-----------|------||----------||---------|\n'
         '| FETCHed 100s cups of tea|         ||          |            ||           |      ||          ||         |\n'
         '==========================================================================================================\n'
         ))

    # Use escape codes to send cursor to different screen positions
    #       \u001b[{line};{column}H
    #  OR   \u001b[{line};{column}f
    # Use \r and end="" to prevent new lines being added

    hours = total_time // 3600
    minutes = (total_time // 60) - (hours * 60)
    seconds = total_time - (hours * 3600) - (minutes * 60)

    # Print clock on row 3, column 12
    print(f"\u001b[3;12H{str(hours).zfill(2)} / {str(minutes).zfill(2)} / {str(seconds).zfill(2)} ")

    # Print % of the working day this represents
    percent_of_day = total_time / 100
    print(f"\u001b[5;24H{str(percent_of_day).zfill(2)}% ")

    # Print total number of robots
    # at row 4, column 35
    print(f"\u001b[4;35H{n}")

    # Use column_printer helper function to

    #   10 rows, spaced 2 apart, starting on row 9

    # print number of tasks at each stage of completion for each particular job:
    # IN PROGRESS in column 21
    #  "     "    ( + % of completion this represents) -> column 35
    # COMPLETED in column 48
    #     "       (+  % OF GOAL in column 58
    # BOTS ON TASK in column 68
    # HUMANS ON TASK in column 79

    # NOT STARTED in column 9
    column_printer(task_log[5][(j - 5) // 2]["NOT STARTED"], column=9)

    column_printer(task_log[5][(j - 5) // 2]["IN PROGRESS"], column=21)

    column_printer(task_log[5][(j - 5) // 2]["NOT STARTED"], column=48)

    print("\u001b[30;2H{n} Unfortunately, this function has not yet been completed.")
    input("Press any key to return to main menu,"
          "or press [C] to lodge a formal complaint about the software.").upper()
    return n, m, n_dict, m_dict, task_log


#  Function to call from time_sim.
# This function updates the percentage towards completion
# of each task in progress
def updater(log_update):
    for i in range(1, 11):
        if log_update[5][i]["IN PROGRESS"] != 0:
            log_update[8][i][1] += (25 // log_update[[6][i][1], i])
        #  Check if task is complete, and if so,
        # add a repetition of it to task_log[7]
        if log_update[8][i][1] >= 100:
            log_update[7][i][1] += 1
            log_update[8][i][1] = 0
    return log_update


# Function to return the choice between 2 options
def binary_choice(choice_a="increase", choice_b="decrease"):
    while True:
        outcome = input(f"Would you like to choose {choice_a}[press 1] or {choice_b}[press 2] ?\n")
        if outcome.isdigit():
            if outcome == 1 or outcome == 2:
                return outcome


# Function to return a quantity (of workers or robots)
def how_many_labourers(phrase="worker", phrase_2="do you want", max=2):
    l = 0
    while not l:
        l = input(f"\n\n How many {phrase}s {phrase_2}?"
                  f" \n\n Please choose a number between 1 and {max}. \n")
        time_sim(secs=1)
        if not l:
            print("\n Was I meant to take that as an answer? \n")
            time_sim(secs=1)
        else:
            if get_length(l, max=2):
                try:
                    l = int(l)
                    if l > max:
                        print("\n I thought I told you what the maximum amount was... ? \n")
                        time_sim(secs=2)
                        l = 0
                    elif l < 1:
                        print(f"\n That is NOT between 1 and {max}. \n")
                        time_sim(secs=2)
                        l = 0
                    else:
                        return l
                except ValueError:
                    print("\n Sorry, but that isn't a valid response. \n")
                    time_sim(secs=1)
                    print("\n Maybe you entered letters or symbols instead of just a number. \n")
                    time_sim(secs=2)
                    l = 0


# Function to ask user whether they want to
#  change status of robots or workers
#   from finished to idle

################################
################################

# NOTE NEED TO UPDATE TASK_LOG !!!!!!!!!!!!!!!!!!!!!!!

################################
################################

def ask_finished_to_idle(x_dict, phrase="worker"):
    yesno == "Maybe"
    time_sim(secs=1)

    while True:
        finished = 0
        j = len(x_dict)
        for i in range(j):
            if x_dict[phrase + "_" + str(i - 1).zfill(3)]  == 2:
                finished += 1

        if finished == 1:
            while yesno != "Y" and yesno != "N":
                yesno = input(f"Would you like to make the {phrase} "
                            "that has finished its task available "
                              "for more work? (Y/N) \n").upper()

                time_sim(secs=1)
                if get_length(yesno):
                    if yesno == "Y":
                        # Find the one that's finished
                        for swap in range(0, len(x_dict), -1):
                            if x_dict[phrase + "_" + str(swap).zfill(3)] == 2:
                                x_dict[phrase + "_" + str(swap).zfill(3)] = 0

                                # Update task_log
                                if phrase == "Robot":
                                    task_log[1][11] -= 1
                                    task_log[1][0] += 1
                                    try:
                                        task_log[3][0] = task_log[3][11].pop(phrase + "_" + str(swap).zfill(3))
                                    except IndexError:
                                        print(" Some kind of book-keeping error occurred,"
                                              " But if you don't mention it, neither will I.\n")
                                        pass

                                elif phrase == "Human":
                                    task_log[2][11] -= 1
                                    task_log[2][0] += 1
                                    try:
                                        task_log[4][0] = task_log[4][11].pop(phrase + "_" + str(swap).zfill(3))
                                    except IndexError:
                                        print(" I couldn't find that person in the records,"
                                              " But if we fired them by mistake, well,\n"
                                              "      Nothing we can do about it now.\n")
                                        pass

                                return x_dict, yesno

                if yesno == "N":
                    print("\nStop wasting time then!! \n")
                    return x_dict, yesno

        elif finished > 1 :
            while yesno != "Y" and yesno != "N":
                yesno = input(f"Would you like to make any of the {phrase}s that " 
                            "have finished their tasks available "
                              "for more work? (Y/N)\n").upper()

                time_sim(secs=1)
                if get_length(yesno):
                    if yesno == "Y":
                        # Find out how many robots or humans to transfer
                        phrase_2 = ("s would you like to switch \n"
                                   "from FINISHED to IDLE ? \n")

                        x = how_many_labourers(phrase, phrase_2, finished)
                        # Change x number of robots or workers in list from
                        #  status 0 (IDLE) to status 2 (FINISHED)
                        while x:
                                for swap in range(0, x):
                                    if x_dict[phrase + "_" + str(swap).zfill(3)] == 2:
                                        x_dict[phrase + "_" + str(swap).zfill(3)] = 0
                                        x -= 1

                                        # Update task_log
                                        if phrase == "Robot":
                                            task_log[1][11] -= 1
                                            task_log[1][0] += 1
                                            try:
                                                task_log[3][0] = task_log[3][11].pop(phrase + "_" + str(swap).zfill(3))
                                            except IndexError:
                                                print(" This is an error message.\n"
                                                      " If you see many of these, I'm embarrassed.\n")
                                                pass

                                        elif phrase == "Human":
                                            task_log[2][11] -= 1
                                            task_log[2][0] += 1
                                            try:
                                                task_log[4][0] = task_log[4][11].pop(phrase + "_" + str(swap).zfill(3))

                                            except IndexError:
                                                print(" There's an entry missing in the personnel records.\n"
                                                      " Press F to fire the Human Resources manager."
                                                      "        <Joke : That's you !> \n")
                                                pass

                        return x_dict, yesno

                    elif yesno == "N":
                        print("You have elected not to refresh any robots. \n")
                        time_sim(secs=2)
                    return x_dict, yesno


# Function to add robot
# Accessed by pressing A within what_next() function
# Adds an IDLE robot (0 status code)
# Number of robots n is passed in as parameter {x}
def add_robot(x, x_dict, next_x):
    clear_screen()
    print("\n You have selected \"ADD a robot\" \n")
    time_sim(secs=1)
    print("\n Here are the robots you currently have:-- \n\n")
    dict_printer(x, x_dict)
    time_sim(secs=1)
    additional = how_many_labourers(phrase="robot", phrase_2="do you want to add to the Ro-Ro-Ro-Your-Bots\u00AE workforce?",
                                   max=99 - x)
    time_sim(secs=1)

    if additional == 1:
        x_dict["Robot_" + str(next_x)] = 0

        x += 1
        next_x += 1

        # Update Task Log
        task_log[1][0] += 1
        task_log[3][0].append("Robot_" + str(x))

        print("\n You have added an extra 'bot to the crew.\n")
        print(f" Its name is {x_dict["Robot_" + str(next_x)]} - cute, huh ? \n")
        time_sim(secs=1)
        print(" Go back to the main menu,\n"
              " Do not pass \"GO\"\n"
              " --Press C to CHANGE its status and get it mechanised ! \n")
        time_sim(secs=1)
        input(" Press ENTER to get backl to the grind !\n")
        return x, x_dict, next_x

    elif additional > 1:
        print(f"\n You have added {additional} extra 'bots to the crew. \n")
        print(f"Their names are: \n")
        time_sim(secs=1)
        for i in range(additional):
            x_dict["Robot_" + str(next_x + i)] = 0
            if (next_x + i) % 5 == 0:
                print("\n")
            if (next_x + i) < 10:
                print(["Robot_" + str(next_x + i)], end="  ")
            else:
                print(["Robot_" + str(next_x + i)], end=" ")
        time_sim(secs=2)
        print("\n")

        x += additional
        next_x += additional
        time_sim(secs=1)

        print(" But there's no time to congratulate yourself:\n"
              " Go back to the main menu;\n"
              " --Press C to CHANGE their status and get them mechanised ! \n")
        input("Press ENTER to continue production !\n")

        return x, x_dict, next_x


# Function to remove robot.
# Accessed by pressing R within what_next() function
def remove_robot(x, x_dict, next_x, tasks):
    yesno = "Maybe"
    clear_screen()
    print("\n You have selected \"REMOVE robot\" \n")
    time_sim(secs=1)
    tasks = updater(tasks)

    # Check the factory has enough robots for any to be removed
    if x == 1:
        print(("\n You only have one teeny-weeny robot left - \n\n"
               " You need at least 1 robot for this robotic cell to even BE a robotic cell. \n\n "))
        time_sim(secs=1)
        tasks = updater(tasks)
        print("So sorry, no, you can't remove that last poor lonely robot.")
        return x, x_dict, next_x, tasks

    elif x < 1:
        print("\n It seems there has been a g-g-g-glitch - \n\n48@0*y3h£}{t870¬0o\n\n")
        print((" You have no robots to remove.\n\n"
               " You need at least 1 robot for this robotic cell to even BE a robotic cell. \n\n "
               " Tell you what : to compensate for the error, we'll top up your team to its maximum"
               "of 99 robots.\n\n "
               " Here you go : \n\n"
               ))

        time_sim(secs=1)
        tasks = updater(tasks)
        x = 99

        # Update Task Log and print robot names
        x_data[1][0] = 99
        print(f"Their names are: \n")
        time_sim(secs=1)
        for i in range(next_x, next_x + 99):
            x_dict["Robot_" + str(next_x + i).zfill(3)] = 0
            x_data[3][0].append("Robot_" + str(next_r + i)).zfill(3)

            if (next_x + i) % 5 == 0:
                print("\n")
            if (next_x + i) < 10:
                print(["Robot_" + str(next_x + i).zfill(3)], end="  ")
            else:
                print(["Robot_" + str(next_x + i).zfill(3)], end=" ")
        time_sim(secs=2)
        tasks = updater(tasks)

        print(("\n\n Oh - I just realised :\n\n"
               " You were trying to remove robots before all this kerfuffle, "
               "and now I've just given you 99 fresh ones! \n\n"
               " So I guess you'll want to send some to the trash compacter straight away! \n\n"
               " Let's give it another try then, shall we?\n\n"))

        time_sim(secs=1)
        tasks = updater(tasks)
        return x, x_dict, next_x, tasks

    elif x == 2:
        # find whether there's an IDLE robot
        if tasks[1][0] == 0:
            time_sim(secs=1)
            tasks = updater(tasks)
            # check whether a robot has FINISHED its task and can be re-classified as IDLE
            if tasks[1][11]  == 0:
                 print(("\n  Both your bots are busy. \n"
                        "  If you want to remove one from the robotic cell,\n"
                        " at the very least, unplug it from the wall first. \n\n"
                        "   Try pressing [C] for CHANGE status from the main menu.\n"))
                 time_sim(secs=1)

            else:
                ask_finished_to_idle(x_dict, "Robot")
                if tasks[1][0] == 0:
                    print(" You can't dismantle your droids until they stop moving.\n"
                          " Choose another option.\n")
                    return x, x_dict, next_x, tasks

                elif tasks[1][0] == 1:
                    print(("\n You have 2 robots, so you can only remove 1, \n"
                           "because you need at least 1 droid for your robotic cell to function. \n\n"
                           ))
                    time_sim(secs=1)
                    tasks = updater(tasks)

                    while yesno != "Y" and yesno != "N":
                        yesno = input("So, press [Y] if you want to drop down to the minimum.\n"
                                      "Else, press [N].\n")

                        time_sim(secs=1)
                        tasks = updater(tasks)

                        if get_length(yesno):
                            if yesno == "Y":
                                # Find which robot is IDLE
                                for k in x_dict:
                                    if x_dict[k] == 0:
                                        del x_dict[k]
                                        x == 1
                                        tasks[1][0] -= 0
                                        tasks[3].pop("Robot_" + str(k).zfill(3))
                                        print("\n OK, you're down to your last robot now. \n\n")
                                        return x, x_dict, next_x, tasks
                                    # If this section of code is reached, something has malfunctioned
                                    simple_error()
                                    return x, x_dict, next_x, tasks
                            elif yesno == "N":
                                   print("\nStop wasting time then!! \n")
                                   return x, x_dict, next_x, tasks
                            else:
                                   simple_error()
                                   return x, x_dict, next_x, tasks

    elif x > 2:

        #  find how many robots are IDLE
        idle = tasks[1][0]

        if idle < 1:
            # Check if any robots have FINISHED their tasks:
            finished = tasks[1][11]

            if not finished:
                print("\n You will have to switch some from the tasks they're WORKING on \n"
                      "or wait til they're FINISHED. \n")
                time_sim(secs=3)
                tasks = updater(tasks)
                return x_dict, x_dict, next_x, tasks

            # Suggest user switches some statuses from FINISHED to IDLE
            ask_finished_to_idle(a_dict, "Robot")
            if tasks[1][0] == 0:
                print(" You can't delete droids while they're doing stuff.\n"
                      " Choose another option.\n")
                return x, x_dict, next_x, tasks

            elif tasks[1][0] == 1:
                print("\n You have 1 IDLE robot now,")
                input(" so do you want to melt it down for its raw metals?\n").upper()
                time_sim(secs=1)
                tasks = updater(tasks)

                while yesno != "Y" and yesno != "N":
                    yesno = input("Press [Y] if you want to drop down to the minimum.\n"
                                  "Else, press [N].\n").upper()

                    time_sim(secs=1)
                    tasks = updater(tasks)

                if get_length(yesno):
                    if yesno == "Y":
                        # Find which robot is IDLE
                        for k in x_dict:
                            if x_dict[k] == 0:
                                del x_dict[k]
                                x == 1
                                tasks[1][0] -= 0
                                tasks[3].pop("Robot_" + str(k).zfill(3))
                                print("\n You've only got one robot left now. \n"
                                      "That's still plenty enough to cause you bother, mind.")
                                return x, x_dict, next_x, tasks

                            # This code section should not execute
                            simple_error()
                            return x, x_dict, next_x, tasks

                    elif yesno == "N":
                        print("\n OK, I can deal with it.\n"
                              " Back to the main menu, then...\n")
                        return x, x_dict, next_x, tasks
                    else:
                        simple_error()
                        return x, x_dict, next_x, tasks

        if idle == 1:
            print("\nYou have 1 IDLE robot to remove.\n\n"
                  "That should send out a signal to the others.")
            while yesno != "Y" and yesno != "N":
                yesno = input("So, press [Y] if you want to drop down to the minimum.\n"
                              "Else, press [N].\n").upper()

                time_sim(secs=1)
                tasks = updater(tasks)
                if get_length(yesno):
                    if yesno == "Y":
                        # Find which robot is IDLE
                        for k in x_dict:
                            if x_dict[k] == 0:
                                del x_dict[k]
                                x == 1
                                tasks[1][0] -= 0
                                tasks[3].pop("Robot_" + str(k).zfill(3))
                                print("\n You've only got one robot left now. \n"
                                      "That's still plenty enough to cause you bother, mind.")
                                return x, x_dict, next_x, tasks

                            # This code section should not execute
                            simple_error()
                            return x, x_dict, next_x, tasks

                    elif yesno == "N":
                        print("\n Try another option then,"
                              " or just keep wasting time."
                              " It's not my life that's precious. \n")
                        return x, x_dict, next_x, tasks
                    else:
                        simple_error()
                        return x, x_dict, next_x, tasks

        elif idle > 1:
            to_remove = how_many_labourers("Robot", " would you like to remove?", idle)

            # checksum against task_log
            if to_remove > tasks[1][0]:
                print(" This number is a bit too high.\n"            
                      " Perhaps you need to check the inventory.\n")

                time_sim(secs=1)
                tasks = updater(tasks)

                return x, x_dict, next_x, tasks

            else:
                 # loop backwards through n_dict to remove IDLE robots

                key_list = []
                while to_remove:
                    for key, value in reversed(x_dict.items()):
                        if value == 0 and to_remove:
                            key_list.append(key)
                            to_remove -= 1

                for key in key_list:
                    del x_dict[key]
                    # Update Task Log
                    tasks[1][0] -= 1
                    if key in tasks[3][0]:
                        tasks[3][0].remove(key)

                    print(f"\n{key} has been deleted.")

                    time_sim(secs=1)
                    tasks = updater(tasks)

                return x, x_dict, next_x, tasks


def change_status(x_dict):
    clear_screen()
    print("\n You have selected \"CHANGE a robot's status\" \n")
    time_sim(secs=1)
    print("\n          You will now be shown all the many robots you have to choose from,"
          "           along with their respective statuses: \n\n")
    time_sim(secs=1)
    status_printer(x_dict)


    request = 0
    while not request:
        request = input("\n  Please select the robot(s) whose status(es) you want to change,\n"
                        " using their serial numbers SEPARATED BY COMMAS.\n\n"
                        "  Alternatively, press X to return to the main menu.").upper()

        time_sim(secs=1)
        if request == "X":
            return x_dict
        # Remove any spaces from the query
        request = request.replace(" ", "")
        desired_list = request.split(",") # Removes any commas and separates the query there

        # If they requested more items than there are robots, trim it right down
        if len(desired_list) > len(x_dict):
            del desired_list[len(x_dict):]

        # Check all the characters of the string are numbers now
        for t in range(len(desired_list)):
            if not desired_list[t].isdigit():
                print("I think you entered an invalid character.\n")
                time_sim(secs=1)
                print(" Let's try that again.\n")
                time_sim(secs=1)
                request = 0
            else:
                continue

        try:
            # convert the list of split strings into a list of integers
            for t in range(len(desired_list)):
                desired_list[t] = int(desired_list[t])
                # convert to text keys to match against dictionary
                #  .zfill(3) formats a number as three digits,
                # adding leading zeroes, as in robot_dict
                desired_list[int(t)] = "Robot" + "_" + str(desired_list[t]).zfill(3)

        except ValueError:
            print("I think you entered an invalid character.\n")
            time_sim(secs=1)
            print(" Let's try that again.\n")
            time_sim(secs=1)
            request = 0

        for desired in desired_list:
            if desired not in x_dict:
                print("Your selection doesn't correspond to the robots in your employ. \n"
                      "Maybe you thought you owned more than you do. \n")

                time_sim(secs=1)
                print(" Let's try that again.\n")
                time_sim(secs=1)
                request = 0


        # check if all robots to be switched have same status as the first
        base_status = x_dict[desired_list[0]]
        for desired in desired_list:
            try:
                if x_dict[desired] != base_status:
                    print("\n I don't think all the robots you selected had the same status.\n\n")
                    print("I suggest you try again.\n")
                    request = 0

            except KeyError:
                print("Error: one of those numbers smelled a a bit off.\n")
                print("Please try again. Or don't. Either way.\n")
                request = 0

    # Grammar checking: has only a single robot been selected?
    if len(desired_list) == 1:
        print(f" This robot is currently {return_status(x_dict[desired_list[0]])}", end="")
        print("Please enter the status you wish to change it to:\n")

    elif len(desired_list) > 1:
        print(f"\n These robots are currently {return_status(x_dict[desired_list[0]])}.\n")
        print("Please enter the status you wish to change them to:\n")
    print("     0 = IDLE      1 = WORKING     2 = FINISHED       \n")
    print("Or press X to return to the main menu.\n")

    desired_status = 0
    while not desired_status:
        desired_status = input().upper()
        time_sim(secs=1)
        if desired_status == "X":
            print(" Action aborted. Returning to the main menu.\n")
            time_sim(secs=2)
            return x_dict

        if get_length(desired_status, 1):
            try:
                desired_status = int(desired_status)
                if desired_status < 0 or desired_status > 2:
                    print(" That number isn't going to work.\n"
                          " Please try again or press X to return to the main menu.")
                    desired_status = 0
                elif 0 <= desired_status <= 1:
                    print(f" You have opted to switch them from {return_status(desired_status)}"
                          f" to {return_status(base_status)}.\n")
                    if desired_status == base_status:
                        print("That doesn't make sense, even to me.\n")
                        print("Please try again.")
                        desired_status = 0
                    else:
                        for desired in desired_list:
                            x_dict[desired] = desired_status
                            print(f"{desired} has been switched to {return_status(desired_status)}.\n")

            except ValueError:
                print(" Your input was invalid.\n")
                print(" Go back to the main menu and do better.")
                time_sim(secs=1)
                return x_dict


# Function to assign task to [PROGRAM] robot
# Accessed by pressing P within what_next() function
def program_robot(a_dict, tasks):
    clear_screen()
    print("\n You have selected \"PROGRAM a robot to execute a task\" \n")
    time_sim(secs=1)
    tasks = updater(tasks)

    # Check if any robots are IDLE
    # IDLE robots are numbered at task_log[1][0]
    idle = tasks[1][0]
    while not idle:
        print(" but you have no IDLE robots to execute your programs.\n")
        #  Check if any robots have FINISHED their tasks
        # and could be re-labelled as IDLE
        # FINISHED robots are numbered at tasks[1][11]
        finished = tasks[1][11]

        if not finished:
            print("\n You will have to switch some from the tasks they're WORKING on \n"
                  "or wait til they're FINISHED. \n")
            time_sim(secs=3)
            tasks = updater(tasks)
            return a_dict, tasks
        # Suggest user switches some statuses from FINISHED to IDLE
        ask_finished_to_idle(a_dict, "Robot")

    if idle == 1:
        print("\n You have 1 robot IDLE. \n")
        idle_list = []
        time_sim(secs=1)
        tasks = updater(tasks)
        # Identify IDLE robot
        print("Here's the IDLE robot -->", end="")
        for key, value in a_dict.items():
            if value == 0:
                if value == 0:
                    print("\r", key, "\n")
                    print(" Shame on it !! \n")

    elif idle > 1:
        print(f" You currently have {idle} IDLE robots to assign tasks to.\n")
        time_sim(secs=1)
        tasks = updater(tasks)
        # Identify IDLE robots
        print(f" These are the {idle} IDLE robots :\n")
        a = 1  # Create a counter to print the robots' names
               # in lines of 5

        for key, value in a_dict.items():
            while a <= 5:
                if value == 0:
                    print(f" {key}  ", end="")
            a = 1
            print("\n")
        print("  If you ask me, they should be lined up against the wall"
              " and shut down.")
        time_sim(secs=1)
        tasks = updater(tasks)
        request = 0

        while not request:
            request = input("\n  Please select the robot(s) who you wish to re-program,\n"
                            " using their serial numbers SEPARATED BY COMMAS.\n\n"
                            "  Alternatively, press X to return to the main menu.").upper()

            time_sim(secs=1)
            tasks = updater(tasks)
            if request == "X":
                return a_dict, tasks
            # Remove any spaces from the query
            request = request.replace(" ", "")
            chosen_list = request.split(",")  # Removes any commas and separates the query there
            # If they requested more items than there are robots, trim it right down
            if len(chosen_list) > len(a_dict):
                del chosen_list[len(a_dict):]

            # Check all the characters of the string are numbers now
            for t in range(len(chosen_list)):
                if chosen_list[t].isdigit() == False:
                    print("I think you entered an invalid character.\n")

                    time_sim(secs=1)
                    tasks = updater(tasks)
                    print(" Let's try that again.\n")

                    time_sim(secs=1)
                    tasks = updater(tasks)
                    request = 0

                else:
                    try:
                        # convert the list of split strings into a list of integers
                        chosen_list[t] = int(chosen_list[t])
                        if chosen_list[t] > 100 or chosen_list[t] < 1:
                            print("You entered a value out of range")

                            time_sim(secs=1)
                            tasks = updater(tasks)

                            print(" Let's try that again.\n")

                            time_sim(secs=1)
                            tasks = updater(tasks)
                            request = 0
                        # Build the robot's ID
                        chosen_list[int(t)] = "Robot" + "_" + str(chosen_list[t]).zfill(3)

                    except ValueError:
                        print("I think you entered an invalid character.\n")
                        time_sim(secs=1)
                        tasks = updater(tasks)
                        print(" Let's try that again.\n")
                        time_sim(secs=1)
                        request = 0

            # Check that each robot selected is actually working in the robotic cell
            for chosen in chosen_list:
                if chosen not in a_dict:
                    print("Your selection doesn't correspond to the robots in your employ. \n"
                          "Maybe you thought you owned more than you do. \n")

                    time_sim(secs=1)
                    tasks = updater(tasks)
                    print(" Let's try that again.\n")
                    time_sim(secs=1)
                    tasks = updater(tasks)
                    request = 0

            # check if all robots to be switched have same status as the first
            base_status = a_dict[chosen_list[0]]
            for chosen in chosen_list:
                if a_dict[chosen] != base_status:
                    print("\n I don't think all the robots you selected had the same status.\n\n"
                          " I suggest you try again.\n")
                    time_sim(secs=1)
                    tasks = updater(tasks)
                    request = 0

            # Grammar checking: has only a single robot been selected?
            if len(chosen_list) == 1:
                print(""" Please enter the task you wish to condemn it to,
                                 from the following list:\n""")
                print(f"    {tasks[0][task][1]:task in tasks if task != 0 and task != 11}", end="")
                print(f" -- --> {task:task in tasks if task != 0 and task != 11} \n")
            elif len(chosen_list) > 1:
                print(""" Please enter the task you wish to consign them to,
                                                     from the following list:\n""")
            print(f"          {tasks[0][task][1]:task in tasks if task != 0 and task != 11}", end="")
            print(f" -- --> {task:task in tasks if task != 0 and task != 11} \n")
            print("Or press X to return to the main menu.\n")
            chosen_task = 0
            while not chosen_task:
                chosen_task = input().upper()
            time_sim(secs=1)
            tasks = updater(tasks)

            if chosen_task == "X":
                print(" Action aborted. Returning to the main menu.\n")
                time_sim(secs=2)
                tasks = updater(tasks)
                return a_dict, tasks

            # Check whether input was one character long
            if get_length(chosen_task, 1):
                try:
                    # Check whether input was an integer
                    chosen_task = int(chosen_task)
                    if chosen_task < 1 or chosen_task > 10:
                        print(" That number isn't going to work.\n"
                              " Please try again or press X to return to the main menu.")
                        time_sim(secs=2)
                        tasks = updater(tasks)
                        request = 0
                    elif 1 <= chosen_task <= 10:
                        print(f" You have opted to switch them from IDLE"
                              f" to {tasks[0][chosen_task][1]}.\n")
                        for chosen in chosen_list:
                            x_dict[chosen] = chosen_task
                            print(f"{chosen} has been switched to {tasks[0][chosen_task][1]}.\n")
                            break

                except ValueError:
                    print(" Your input was invalid.\n")
                    print(" Go back to the main menu and do better.")
                    time_sim(secs=2)
                    tasks = updater(tasks)
                    return a_dict, tasks, log

        # while not loop has been ended by break statement
        #  Update tasks:
        for chosen in chosen_list:
            # Increment list of robots working on this task
            tasks[1][chosen_task] += 1
            # Decrement list of IDLE robots
            tasks[1][0] -= 1

            # Remove robot's ID from IDLE list kept at tasks[3][0]
            try:
                tasks[3][0].pop(chosen)
            except:
                print(" Your Robot Resources manager just noticed a discrepancy "
                  "in your RR inventory.\n"
                  " You might want to check the LOG next (L from main menu)\n"
                  "           or TRACK progress of tasks (T from main menu)\n")
                input("Press ENTER to continue.\n")
                time_sim(secs=2)
                tasks = updater(tasks)
                # Find robot's ID in Task Log
                pass

            # Add robot's ID to list for that task at tasks[3][_]
            # But check first it isn't already there
            for i in range(12):
                search_list = len(tasks[3][i])
                for robot in search_list:
                    if robot == chosen:
                        tasks[3][task].remove(robot)
            tasks[3][chosen_task].append(chosen)
            return a_dict, tasks


# Function to employ new worker.
# Accessed by pressing E within what_next() function
# Adds an IDLE human (0 status code)
# {x} holds current number of humans
# {y} holds the number to assign to the next new worker
def employ_worker(x, x_dict, next_x):
    clear_screen()
    print("\n You have selected \"EMPLOY a new worker\" \n")
    time_sim(secs=1)
    print("\n Here are the humans you currently have:-- \n\n")
    dict_printer(x, x_dict)
    time_sim(secs=1)
    to_add = how_many_labourers(phrase="human", phrase_2="do you want to add to the Ro-Ro-Ro-Your-Bots\u00AE workforce?",
                                max=99 - x)
    time_sim(secs=1)

    if to_add == 1:
        x_dict["Human_" + str(next_x)] = 0
        x += 1
        next_x += 1
        print("\n You have added an extra pair of hands to the team.\n")
        print(f" Their name is {x_dict["Human_" + str(next_x)]}. \n")
        print(" Bet you've forgotten it already!\n")
        print(" --Press M to MANAGE their status and get them toiling ! \n")
        time_sim(secs=1)
        input(" Press ENTER to get backl to the grind !\n")
        return x, x_dict, next_x

    elif to_add > 1:
        print(f"\n You have added {to_add} extra bodies to the workforce. \n")
        print(f"Their names are: \n")
        for i in range(to_add):
            x_dict["Human_" + str(next_x + i)] = 0
            if (next_x + i) % 5 == 0:
                print("\n")
            if (next_x + i) < 10:
                print(["Human_" + str(next_x + i)], end="  ")
            else:
                print(["Human_" + str(next_x + i)], end=" ")
            print("\n")

        time_sim(secs=2)

        x += to_add
        next_x += to_add
        print(" Now it's back to the main menu:"
              " --Press M to MANAGE their statuses and get them toiling ! \n")
        input("Press ENTER to continue production !\n")

        return x, x_dict, next_x



# Function to fire a worker.
# Accessed by pressing F within what_next() function
def fire_human(x, x_dict, next_x):
    yesno = "Maybe"
    clear_screen()
    print("\n You have selected \"FIRE a human\" \n")
    time_sim(secs=1)

    # Check the factory has enough human life for any to be removed
    if x == 1:
        print(("\n You only have one other human left apart from you- \n\n"
              " If you even count, that is.\n\n "))
        time_sim(secs=1)
        print("So sorry, no, you can't remove any more humanity from this plant.")
        return x, x_dict, next_x

    elif x < 1:
        print("\n The humanity counter is too low.")
        time_sim(secs=1)
        print((" It seems you have no humans to remove.\n\n"
               " You need at least 1 human around, for insurance purposes if nothing else. \n\n "
               " Oh, how fortunate - I see at yon factory gates \n"
               " a wandering journeyman seeking to ply his trade... \n\n"
               ))

        time_sim(secs=1)
        x = 1
        x_dict[next_x] = 0

        # Update Task Log

        next_x += 1

        print("Congratulations ! You're legally an employer again.\n")
        print("Let's not mention this little hiccup to anyone, eh?\n")
        dict_printer(x, x_dict)
        return x, x_dict, next_x

    elif x == 2:
        # loop backwards through m_dict to remove the last IDLE human
        k = False
        for key, value in reversed(x_dict.items()):
            if value == 0:
                k = True
        if not k:
            print(("\n  You can't sack a man while he's got his back turned, grafting like a gravedigger.\n"
                   " Tell him he can go on a break, and give him the news over a cuppa."
                   " Press M to Manage the jobs the gang are working on. \n\n"))
        else:
            print(("\n You have 2 human workers, so you can only fire 1"
                   "because you need at least 1 other human to reduce the risk of you getting cabin fever. \n\n"
                  ))

        time_sim(secs=1)
        while yesno != "Y" and yesno != "N":
            yesno = input("So, press [Y] if you want to cut staffing to the minimum.\n"
                          "Otherwise, press [N].\n").upper()

            time_sim(secs=1)
            if get_length(yesno):
                if yesno == "Y":
                        del x_dict[k]
                        x == 1
                        print("\n OK, only one human left now. \n"
                              " And it isn't you ! \n")
                        return x, x_dict, next_x

                elif yesno == "N":
                        print("\nStop wasting time then!! \n")
                        return x
                else:
                    simple_error()
                    return x, x_dict, next_x

    elif x > 2:
        idle = 0
        # loop through m_dict to find how many slackers are IDLE
        for value in x_dict.values():
            if value == 0:
                idle += 1
        if idle < 1:
            print(("\n  You can't sack a man while he's got his back turned, grafting like a gravedigger.\n"
                   " Tell him he can go on a break, and give him the news over a cuppa."
                   " Press M to Manage the jobs the gang are working on. \n\n"))
            return x, x_dict, next_x
        elif idle ==1:
            print("\nYou have 1 IDLE human you can sack.\n\n"
                  "Do it now, before you grow a heart.")

            time_sim(secs=1)
            for key, value in reversed(x_dict.items()):
                if value == 0:
                    k = key
                    break
            try:
                del x_dict[k]
                print(f"{x_dict[k]} was fired !\n")
                print("\n Give him his P45 \n"
                      " and that's one more benefit claimant for the DWP to deal with ! \n\n")
                return x, x_dict, next_x
            except KeyError:
                simple_error()
                print("\n Keep calm and keep callous...\n")
                return x, x_dict, next_x

        elif idle > 1:
            to_fire = how_many_labourers(phrase="human", phrase_2=" would you like to fire?", max=idle)
            # loop backwards through m_dict to remove IDLE humans
            key_list = []
            while to_fire:
                for key, value in reversed(x_dict.items()):
                    if value == 0 and to_fire:
                        key_list.append(key)
                        to_fire -= 1
            for key in key_list:
                del x_dict[key]
                print(f"\n{key} has been fired.")

                time_sim(secs=1)
            return x, x_dict, next_x


# Function to manage worker
# Accessed by pressing M within what_next() function
# statuses available = idle / working / finished task
def manage_worker(x_dict):
    clear_screen()
    print("\n You have selected \"MANAGE a worker\" \n")
    time_sim(secs=1)
    print("\n          You will now be shown all the many skivvies you have to choose from,"
          "           along with their respective statuses: \n\n")
    time_sim(secs=1)
    status_printer(x_dict)
    request = 0
    while not request:
        request = input("\n  Please select the human(s) whose status(es) you want to change,\n"
                        " using their employee numbers SEPARATED BY COMMAS.\n\n"
                        "  Alternatively, press X to return to the main menu.").upper()

        time_sim(secs=1)
        if request == "X":
            return x_dict
        # Remove any spaces from the query
        request = request.replace(" ", "")
        desired_list = request.split(",") # Removes any commas and separates the query there
        # If they requested more items than there are humans, trim it right down
        if len(desired_list) > len(x_dict):
            del desired_list[len(x_dict):]
        # Check all the characters of the string are numbers now
        for t in range(len(desired_list)):
            if desired_list[t].isdigit() == False:
                print("I think you entered an invalid character.\n")

                time_sim(secs=1)
                print(" Let's try that again.\n")
                time_sim(secs=1)
                request = 0
            else:
                continue
        try:
            # convert the list of split strings into a list of integers
            for t in range(len(desired_list)):
                desired_list[t] = int(desired_list[t])
                # convert to text keys to match against dictionary
                desired_list[int(t)] = "Human" + "_" + str(desired_list[t]).zfill(3)

        except ValueError:
            print("I think you entered an invalid character.\n")

            time_sim(secs=1)
            print(" Let's try that again.\n")

            time_sim(secs=1)
            request = 0

        for desired in desired_list:
            if desired not in x_dict:
                print("Your selection doesn't correspond to the humans in your employ. \n"
                      "Maybe you thought you owned more than you do. \n")

                time_sim(secs=1)
                print(" Let's try that again.\n")

                time_sim(secs=1)
                request = 0
            else:
                continue

        # check if all humans to be switched have same status as the first
        base_status = x_dict[desired_list[0]]
        for desired in desired_list:
            try:
                if x_dict[desired] != base_status:
                    print("\n I don't think all the humans you selected had the same status.\n\n")
                    print("I suggest you try again.\n")
                    request = 0
            except KeyError:
                print(" Something isn't working out somewhere.\n")
                print(" Please give it another try.\n")
                request = 0

    # Grammar checking: has only a single human been selected?
    if len(desired_list) == 1:
        print(f" This human is currently {return_status(x_dict[desired_list[0]])}", end="")
        print("Please enter the status you wish to change it to:\n")

    elif len(desired_list) > 1:
        print(f"\n These humans are currently {return_status(x_dict[desired_list[0]])}.\n")
        print("Please enter the status you wish to change them to:\n")
    print("     0 = IDLE      1 = WORKING     2 = FINISHED       \n")
    print("Or press X to return to the main menu.\n")
    desired_status = 0
    while not desired_status:
        desired_status = input().upper()

        time_sim(secs=1)
        if desired_status == "X":
            print(" Action aborted. Returning to the main menu.\n")
            time_sim(secs=2)
            return x_dict
        if get_length(desired_status, 1):
            try:
                desired_status = int(desired_status)
                if desired_status < 0 or desired_status > 2:
                    print(" That number isn't going to work.\n"
                          " Please try again or press X to return to the main menu.")
                    desired_status = 0

                elif 0 <= desired_status <= 1:
                    print(f" You have opted to switch them from {return_status(desired_status)}"
                          f" to {return_status(base_status)}.\n")
                    if desired_status == base_status:
                        print("That doesn't make sense, even to me.\n")
                        print("Please try again.")
                        desired_status = 0
                    else:
                        for desired in desired_list:
                            x_dict[desired] = desired_status
                            print(f"{desired} has been switched to {return_status(desired_status)}.\n")

            except ValueError:
                print(" Your input was invalid.\n")
                print(" Go back to the main menu and do better.")

                time_sim(secs=1)
                return x_dict


# Function to order available workers to carry out tasks.
# Accessed by pressing O within what_next() function
def order_worker(b_dict, tasks):
    clear_screen()
    print("\n You have selected \"ORDER\" a human to perform a task. \n")
    time_sim(secs=1)
    tasks = updater(tasks)

    # Check if any humans are IDLE
    # IDLE humans are numbered at task_log[2][0]
    idle = tasks[2][0]
    while not idle:
        print(" but you have no IDLE lackeys to boss around.\n")
        #  Check if any humans have FINISHED their tasks
        # and could be re-labelled as IDLE
        # FINISHED humans are numbered at tasks[2][11]
        finished = tasks[2][11]

        if not finished:
            print("\n You will have to switch some from the tasks they're WORKING on, \n"
                  "or wait til they've FINISHED what they're doing. \n")
            time_sim(secs=3)
            tasks = updater(tasks)
            return b_dict, tasks, log
        # Suggest user switches some statuses from FINISHED to IDLE
        ask_finished_to_idle(b_dict, "Human")

    if idle == 1:
        print("\n You have 1 human IDLE. \n")
        idle_list = []
        time_sim(secs=1)
        tasks = updater(tasks)
        # Identify IDLE human
        print("Here's the IDLE human -->", end="")
        for key, value in b_dict.items():
            if value == 0:
                print("\r", key, "\n")
                print(" Shame on them !! \n")

    elif idle > 1:
        print(f" You currently have {idle} IDLE humans to order to do tasks.\n")
        time_sim(secs=1)
        tasks = updater(tasks)

        # Identify IDLE humans
        print(f" These are the {idle} IDLE humans :\n")
        a = 1  # Create a counter to print the humans' names
        # in lines of 5
        for key, value in b_dict.items():
            while a <= 5:
                if value == 0:
                    print(f" {key}  ", end="")
            a = 1
            print("\n")
        print("  If you ask me, they should be lined up against the wall"
              " and shut down.")
        time_sim(secs=1)
        tasks = updater(tasks)
        request = 0

        while not request:
            request = input("\n  Please select the human(s) who you wish to boss around,\n"
                            " using their employee numbers SEPARATED BY COMMAS.\n\n"
                            "  Alternatively, press X to return to the main menu.").upper()

            time_sim(secs=1)
            tasks = updater(tasks)
            if request == "X":
                return b_dict, tasks, log
            # Remove any spaces from the query
            request = request.replace(" ", "")
            chosen_list = request.split(",")  # Removes any commas and separates the query there
            # If they requested more items than there are humans, trim it right down
            if len(chosen_list) > len(b_dict):
                del chosen_list[len(b_dict):]

            # Check all the characters of the string are numbers now
            for t in range(len(chosen_list)):
                if chosen_list[t].isdigit() == False:
                    print("I think you entered a dodgy character.\n")

                    time_sim(secs=1)
                    tasks = updater(tasks)
                    print(" Let's try that again.\n")

                    time_sim(secs=1)
                    tasks = updater(tasks)
                    request = 0

                else:
                    try:
                        # convert the list of split strings into a list of integers
                        chosen_list[t] = int(chosen_list[t])
                        if chosen_list[t] > 100 or chosen_list[t] < 1:
                            print("You entered a number out of range")

                            time_sim(secs=1)
                            tasks = updater(tasks)
                            print(" Let's try it again.\n")

                            time_sim(secs=1)
                            tasks = updater(tasks)
                            request = 0
                        # Build the human's ID
                        chosen_list[int(t)] = "Human" + "_" + str(chosen_list[t]).zfill(3)

                    except ValueError:
                        print("I think you entered a fishy character.\n")
                        time_sim(secs=1)
                        tasks = updater(tasks)
                        print(" Let's try that again.\n")
                        time_sim(secs=1)
                        tasks = updater(tasks)
                        request = 0

            # Check that each human selected is actually employed in the facility
            for chosen in chosen_list:
                if chosen not in b_dict:
                    print("Your selection doesn't correspond to the peons you employ. \n"
                          "Maybe you didn't hire as many as you thought you did. \n")

                    time_sim(secs=1)
                    tasks = updater(tasks)
                    print(" Who do you think you are: - Sir Alan Sugar ?!\n")

                    time_sim(secs=1)
                    tasks = updater(tasks)
                    request = 0

            # check if all humans to be shifted across have same status as the first
            base_status = b_dict[chosen_list[0]]
            for chosen in chosen_list:
                if x_dict[chosen] != base_status:
                    print("\n I don't think all the humans you selected had the same status.\n\n"
                          " I suggest you have another pop at it.\n")
                    time_sim(secs=1)
                    tasks = updater(tasks)
                    request = 0

            # Grammar checking: has only a single human been selected?
            if len(chosen_list) == 1:
                print(""" Please enter the task you wish to direct them to,
                                 from the following list:\n""")
                print(f"    {tasks[0][task][1]:task in tasks if task != 0 and task != 11}", end="")
                print(f" -- --> {task:task in tasks if task != 0 and task != 11} \n")
            elif len(chosen_list) > 1:
                print(""" Please enter the task you wish to direct them to,
                                                     from the following list:\n""")
            print(f"          {tasks[0][task][1]:task in tasks if task != 0 and task != 11}", end="")
            print(f" -- --> {task:task in tasks if task != 0 and task != 11} \n")
            print("Or press X to return to the main menu.\n")

            chosen_task = 0
            while not chosen_task:
                chosen_task = input().upper()
            time_sim(secs=1)
            tasks = updater(tasks)
            if chosen_task == "X":
                print(" Re-assignmnent abandoned. Returning to the main menu.\n")
                time_sim(secs=2)
                tasks = updater(tasks)
                return b_dict, tasks

            # Check whether input was one character long
            if get_length(chosen_task, 1):
                try:
                    # Check whether input was an integer
                    chosen_task = int(chosen_task)
                    if chosen_task < 1 or chosen_task > 10:
                        print(" That number isn't going to work.\n"
                              " Please try again or press X to return to the main menu.")
                        time_sim(secs=2)
                        tasks = updater(tasks)
                        request = 0
                    elif 1 <= chosen_task <= 10:
                        print(f" You have opted to change them from IDLE"
                              f" to {tasks[0][chosen_task][1]}.\n")
                        for chosen in chosen_list:
                            x_dict[chosen] = chosen_task
                            print(f"{chosen} has been changed to {tasks[0][chosen_task][1]}.\n")
                            break

                except ValueError:
                    print(" Your input was sour.\n")
                    print(" Try again from the main menu. \n")
                    time_sim(secs=2)
                    tasks = updater(tasks)
                    return b_dict, tasks

        # while not loop has been ended by break statement
        #  Update tasks:
        for chosen in chosen_list:
            # Increment list of humans working on this task
            tasks[2][chosen_task] += 1
            # Decrement list of IDLE humans
            tasks[2][0] -= 1

            # Remove human's ID from IDLE list kept at tasks[4][0]
            try:
                tasks[4][0].pop(chosen)
            except:
                print(" Your Human Resources manager just noticed a discrepancy "
                      "in your Personnel Records.\n"
                      " You may want to check the LOG next (L from main menu)\n"
                      "           or TRACK progress of tasks (T from main menu)\n")
                input("Press ENTER to continue.\n")
                time_sim(secs=2)
                tasks = updater(tasks)
                # Find human's ID in Task Log
                pass

            # Add human's ID to list for that task at tasks[3][_]
            # But check first it isn't already there
            for i in range(12):
                search_list = len(tasks[4][i])
                for human in search_list:
                    if human == chosen:
                        tasks[4][task].remove(human)
            tasks[4][chosen_task].append(chosen)
            return b_dict, tasks, log


# Log tasks
# Accessed by pressing L within what_next() function
# Classify tasks as not started / in progress / completed
def log_tasks(tasks):
    clear_screen()
    print("\n You have selected \"LOG tasks\" \n")
    time_sim(secs=3)
    tasks = updater(tasks)

    # Show Progress Log
    print("You will now be shown the progress log...")
    time_sim(secs=2)
    tasks = updater(tasks)
    show_log(tasks)

    go_on = False
    while go_on == False:
        alter = input("\rDo you need to make any alterations?\n").upper()
        if get_length(alter):
            if alter == "Y":
                go_on = True
                break
            if alter == "N":
                print(f"\u001b[30;2H")
                print(f"\u001b[0J")
                input("\n OK. When you\'re ready to return to the main menu, just press Enter\n")
                return
        else:
            print("\n I didn't catch that. Let's take it from the top.\n")
            print(f"\u001b[30;2H")
            print(f"\u001b[0J")

    go_on = False
    while go_on == False:
        print(f"\u001b[30;2H")
        print(f"\u001b[0J)")

        options = range(1, 11)
        amend = input("\n Which task would you like to amend ?"
                      "(or press [O] to see the options)\n").upper()
        time_sim(secs=2)
        tasks = updater(tasks)
        if not get_length(amend):
            continue
        if amend == "O":
            print(f"\u001b[30;2H")
            print(f"\u001b[0J")
            show_task_options(options, tasks[0])
            input("Press ENTER to continue.\n")
            continue
        else:
            try:
                amend = int(amend)
                go_on = True
            except:
                print("There's something wrong here...\n"
                      "Try again:")

    # Adjust numbers in Progress Log
    print(f"\u001b[30;2H")
    print(f"\u001b[0J")
    print(f" You have selected to amend {tasks[0][amend][0]}")
    time_sim(secs=3)
    tasks = updater(tasks)

    go_on = False
    while go_on == False:
        print(("\u001b[32;2H\u001b[0J"
               " You can choose to:"
               "                - alter the numbers of jobs NOT STARTED, IN PROGRESS or FINISHED  --> [P]\n"
               "                - increase / decrease the amount of robots carrying it out --> [R]\n"
               "                - increase / decrease the amount of humans carrying it out --> [H]\n"))
        time_sim(secs=1)
        tasks = updater(tasks)
        amend = input(" Which would you like to do? \n").upper()
        time_sim(secs=1)
        tasks = updater(tasks)

        if not get_length(amend):
            print(" You pressed too many keys.\n")
            continue
        elif get_length(amend) == 1 and amend != "P" and amend != "R" and amend != "H":
            print(" That was not one of the options.\n")
            continue
        else:
            match amend:
                case "P":
                    print("\u001b[32;2H\u001b[0J")
                    which = 0
                    while not which:
                        clear_screen()
                        which = input((f" Is it the NOT STARTED {tasks[0][amend][0]} jobs [N],"
                            f"the {tasks[0][amend][0]} jobs IN PROGRESS [P], or the "
                            f"COMPLETED {tasks[0][amend][0]} jobs [C] you wish "
                            f"to alter the number of? \n"
                                       f"Or press [X] to go back to the main menu.\n"
                            )).upper()
                        time_sim(secs=1)
                        if get_length(which):
                            match which:
                                case "N":
                                    which = "NOT STARTED"
                                case "P":
                                    which = "IN PROGRESS"
                                case "C":
                                    which = "COMPLETED"
                                case "X":
                                    return tasks
                                case _:
                                    which = 0
                    direction = binary_choice()
                    print(f" You have chosen to {direction} the {tasks[5][which]} {tasks[amend][0]} jobs.\n")
                case "R":
                    print(f" You have chosen to increase / decrease the amount of robots {tasks[0][amend][0]}.\n")
                    direction = binary_choice()
                case "H":
                    print(f" You have chosen to increase / decrease the amount of humans {tasks[0][amend][0]}.\n")
                    direction = binary_choice()


# Track
# Function to track progress of robots, workers and tasks
# Accessed by pressing T within what_next() function
# Should regularly update status and identify problems
# eg. Idle robots, idle workers, incomplete tasks.
def track_progress(x_dict, y_dict, tasks):
    clear_screen()
    print("\n You have selected \"TRACK progress\" \n")
    time_sim(secs=1)
    initials = ("O", "S", "W", "H", "P", "D", "A", "T", "U", "B", "F", "X")
    show_task_options(initials, tasks[0])
    selected = False
    while not selected:
        tracked_task = input((" What task would you like to track? \n "
                           "              (Press [O] to see the options)\n")).upper()
        time_sim(secs=1)
        tasks = updater(tasks)
        if get_length(next_task):
            if tracked_task in options:
                selected = True

                if tracked_task == "O":
                    # Show OPTIONS
                    # Call show_task_options function
                    show_task_options(options, tasks[0])
                    selected = False
                    # Will return to beginning of while not loop
            else:
                print(" Not a valid selection!\n")
                selected = False
                if input("Press X to return to main menu, or try again.\n").upper() == "X":
                    return x_dict, y_dict, tasks

    # Otherwise, selected = True has broken while not loop
    print(f"\n You have selected \"{tasks[0][tracked_task][1]}\". \n")
    time_sim(secs=1)
    tasks = updater(tasks)
    print(f" You have {tasks[5]["IN PROGRESS"]} instances of "
          f"{tasks[0][tracked_task][1]} in progress.\n\n")
    print(" Soon you will be able to see the percentage which each individual job"
          "has made towards completion, but unfortunately in this beta version"
          "that functionality has not yet been implemented.\n")
    time_sim(secs=1)
    tasks = updater(tasks)

    pass

    selected = False
    while not selected:
        question = input(" Would you like to see which tasks your robots and your humans"
              "are currently engaged in?\n").upper()
        time_sim(secs=1)
        tasks = updater(tasks)
        if get_length(question):
            if question == "Y":
                print(" You will now be shown a list of your robots, along with the"
                      "tasks they are engaged in.\n")
                input("Press ENTER to continue.\n")
                clear_screen()
                task_printer(x_dict, task_codes, longshort)
                input("\n Press Enter to continue,\n")
                clear_screen()
                task_printer(y_dict, task_codes, longshort)



# Function to get help
# Accessed by pressing H within what_next() function
def get_help():
    input("\n  Press Enter to continue... ")
    clear_screen()
    print(("\n As supervisor at Ro-Ro-Ro-Your-Bots Incorporated\u00AE, you are charged with "
           "ensuring the production of premium-quality robots. \n"
           " You need to manage operations, including assigning tasks, monitoring the status "
           "of robots and work-ers, and tracking the progress of assembly. \n"))

    time_sim(secs=2)
    print((" Please memorise the following list of the tasks involved in manufacturing a Z-57-PrimBot: \n\n"
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

    time_sim(secs=2)
    print((
           " At least once an hour someone is also required to stand on the balcony above the factory floor and "
           "shout at everyone to work faster. \n"
           " That particular job cannot be delegated. \n"))

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()
            pass

    print(' From the main menu, the options you can select are detailed below:\n')
    time_sim(secs=2)
    print(('\n\n Press [A] to add extra robots to the workforce :-       \n'
           '\n       - don\'t fret about having the money for them,      \n'
           '           or whether you\'ve built enough;                  \n'
           '\n                                                             '
           '          Let\'s just say,                                   \n'
           '\n                                                             '
           '            "Here\'s one I prepared earlier"                 \n'
           ))
    time_sim(secs=3)

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
    else:
        clear_screen()

    print(('\n\n Press [R] to remove robots from the workforce :-        \n'
           '         - you can always replace them later.                \n'
           '\n                                                             '
           '\n         Uh,why are these instructions sounding so creepy?!\n'
           '\n                                                             '
           '\n         Please note, you will only be able to remove IDLE \n'
           '          robots, so if all your robots are busy or have fin-\n'
           '          ished their tasks, you will need to press [C] to   \n'
           '          change their status first.                         \n'
           ))

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()

    print(('\n\n Press [C] to change the status of a robot.              \n'
           '\n            - In the beginning they will all be [IDLE]     \n'
           '\n                                                             '
           '\n            - You can change their status to [WORKING], at \n'
           '          which point you should assign them a task by press-\n'
           '          ing [P] to program them.                           \n'
           '\n                                                             '
           '           When they have finished a task, you will see that \n'
           '          their status has been changed to FINISHED.'
           '\n                                                             '
           '           You will then need to switch them back to IDLE    \n'
           '          before they can be re-activated.'
           '\n                                                             '
           '           Select from the robots by entering their serial   \n'
           '          number when prompted.                              \n'
           '\n                                                             '
           '           You can select several robots whose statuses to   \n'
           '          change in a single batch, as long as they all have \n'
           '          the same current status."                          \n'
           '           To do so, enter the numbers separated by commas.  \n'
           ))

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()
            pass

    print(('\n\n Press [P] to program a robot: \n'
           '\n            - that translates to giving it a task to do.   \n'
           '\n            - You choose from the varied tasks carried out \n'
           '\n                                   at                      \n'
           '\n                           Ro-Ro-Ro-Your-Bots\u00AE        \n'
         ))

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()
            pass

    print(('\n\n Press [E] to employ (human) workers:                    \n'
           '\n            - This allows you to grow your workforce.      \n'
           '\n            - Humans work out more costly than robots,     \n'
           '               but never yet have I come across a machine    \n'
           '               that can make a decent cup of tea !           \n'
           ))

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()
            pass

    print(('\n\n Press [F] to fire (human) workers:                      \n'
           '\n            - If you\'ve got more staff than you need      \n'
           '               don\'t feel bad about laying some off:-       \n'
           '                People are just too expensive to maintain    \n'
           '               These days.                                   \n'
           ))

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()
            pass

    print(('\n\n Press [M] to manage the status of humans.               \n'
           '              - Just like you change the robots\' statuses.  \n'
           '\n            - The human workers are just the same mostly.  \n'
           '\n              - IDLE, WORKING or FINISHED                  \n'
           ))

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()
            pass

    print(('\n\n Press [O] to order humans to perform tasks.             \n'
           '\n            - It\'s the same as programming them.          \n'
           ))

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()
            pass

    print(('\n\n Press [L] to log tasks as not started, in progress      \n'
           '                                          or completed.      \n'
           '\n   - For each task you can see how many occurrences of it  \n'
           '      remain to be started, how many are in progress and     \n'
           '      how many have been completed.                        \n\n'
           '     - Each task is shown with the amount of humans slaving  \n'
           '      away at it, and how many robots are leisurely breezing \n'
           '      by them, demonstrating our superior capabilities.'
           '\n     You will have the option of giving tasks new states   \n'
           '      of completion, and updating the number of bodies who   \n'
           '      are working on the current tasks.                      \n'
           ))
    pass

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()


    print(('\n\n Press [T] to track the progress of workers and robots.  \n'))
    pass

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()
            pass

    print('\n\n Press [H] when you want to see these helpful tips again. \n')

    carry_on = input("\n  Press Enter to continue, or type X to exit the manual\n").upper()
    if get_length(carry_on):
        if carry_on == "X":
            clear_screen()
            time_sim(secs=1)
            return
        else:
            clear_screen()
            pass

    print(('\n\n Press [Q] when you wish to quit the simulation.          \n'
           '     This is an option not to be taken lightly.               \n'
           '     In the world of work, there is no saving the game,         '
           '    and when you mess up, you can\'t just go back to as though it'
           '    never happened to begin with.                             \n'))

    input("\n  Press Enter to Exit the manual\n")


# Function to quit program
# Accessed by pressing Q within what_next() function
def quit_program():
    clear_screen()
    quit = input("\nAre you sure you want to quit? (Y/N) \n").upper()
    if get_length(quit):
        if quit == "Y":
            exit()
        elif quit == "N":
            time_sim(secs=3)

            quit = input("\n Are you sure you don't want to quit? (Y/N) \n").upper()
            if get_length(quit):
                if quit == "Y":
                    input("\n This is getting confusing,"
                      "so shall we say No just to be on the safe side?\n").upper()
                if quit == "N":
                    input("\n No, you're not sure you don't want to quit,"
                          "or No, you don't want to quit? \n").upper()
                what_next(n, m, n_dict, m_dict, next_n, next_m, task_log, task_log)

            else:
                print("\n I didn't catch that. Let's take it from the top.\n")
                time_sim(secs=3)
                return
    else:
        quit_program()

def end_sequence():
    clear_screen()
    print("\n Wow ! You finished all your tasks !\n"
          "I don't know how, but you did it.\n\n"
          " You certainly earned your promotion;\n"
          " You're now an honourary robot !")
    exit(0)
################################# --- BODY OF PROGRAM --- ################################

def main():
    # Set console colours using ANSI escape codes:
    print("\u001b[43;30m")

    # Intro
    n, m, n_dict, m_dict, next_n, next_m, task_log = intro_function()

    while True:
        # Display Main Options initially
        main_options()

        # Call function to ask for user action
        what_next(n, m, n_dict, m_dict, next_n, next_m, task_log)

###########################################################################################

# RUN THE CODE !!

main()