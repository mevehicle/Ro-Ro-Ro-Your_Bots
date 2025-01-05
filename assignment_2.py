# Ro-Ro-Ro-Your-Bots Incorporated

# Program to simulate coordination between n robots and m workers in a cell.

# Import modules

from time import sleep
# Use this to get program to sleep for 1 second --> sleep(1)

# ---- Initialise main variables

# n = number of robots
n = 0

# m = number of workers
m = 0


#  As each WORKING robot or worker is assigned to a specific task,
# a lengthier mirror of the dictionaries containing their statuses
# contains the codes of these tasks

# The task codes can be deciphered by
#  using them as the index numbers of a tuple
#   called task_tuple, containing corresponding activities

# To print the short version of the code,
#  access index 0 of the nested tuple (eg. task_tuple[4[0]] )
# Or to print the long version of the code,
#  access index 1 of the nested tuple (eg. task_tuple[4[1]] )

# ----- Task codes are as follows:
# Status = 0 : IDLE
#  "  "  = 1 : SCREWing
#  "  "  = 2 : WELDing
#  "  "  = 3 : HAMMERing
#  "  "  = 4 : POLISHing
#  "  "  = 5 : DRILLing
#  "  "  = 6 : ATTACHing
#  "  "  = 7 : TESTing
#  "  "  = 8 : UNLOADing
#  "  "  = 9 : BOXing
#  "  "  = 10: FETCHing
#  "  "  = 11: FINISHED

task_tuple = (("IDLE     ", "IDLE                          "),
                ("SCREWing ", "SCREWing arms on              "),
                ("WELDing  ", "WELDing legs on               "),
                ("HAMMERing", "HAMMERing heads on            "),
                ("POLISHing", "POLISHing eyes                "),
                ("DRILLing ", "DRILLing ears                 "),
                ("ATTACHing", "ATTACHing waste hoses         "),
                ("TESTing  ", "TESTing the functioning       "),
                ("UNLOADing", "UNLOADing trucks with forklift"),
                ("BOXing   ", "BOXing and shipping product   "),
                ("FETCHing ", "FETCHing cups of tea          "),
                ("FINISHED ", "FINISHED_TASK                 "))


# The scheduler dictionary will be a database showing, for each task(i),
#  how many robots and how many workers are working on them,
#   eg. scheduler[i[robots, humans]
# It is based on the short version of the task stored in index 0
#  of task_tuple's inner nested tuple pairs

scheduler = {}
for i in range(1, 11):
    scheduler[task_tuple[i][0]] = [0, 0]


# The task log is a dictionary showing, for each task,
# how many repetitions of that task have been completed
# and whether any workers or robots are currently engaged in it
# eg. task_log[i[completed, in progress
# It is based on the short version of the task stored in index 0
#  of task_tuple's inner nested tuple pairs

task_log ={}
for i in range(1,11):
    task_log[task_tuple[i][0]] = [0, 0]

# Function to clear screen and return cursor to top left corner
def clear_screen():
    # Clear screen using ANSI escape sequence
    print("\u001b[2J")
    # Cursor to home using ANSI escape sequence
    print("\u001b[H")
    sleep(1)



# Function to ask user how many robots they intend to employ (n):
# ---- & check the value entered for n is valid :
def input_robots(n):
    sleep(1)
    while True:
        while not n:
            print("\n How many robot workers do you want for your factory?\n\n")
            n = input("  Please choose a number between 1 and 99. \n\n")
            sleep(2)
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
                        sleep(0.5)
                        print("\n      HAVE YOU NEVER SEEN BLADE RUNNER? \n")
            except ValueError:
                print("\n Sorry, but that isn't a valid response. \n")
                print("\n Maybe you entered letters or symbols instead of just a number. \n")


# Function to ask user how many humans they intend to employ (m):
# ---- & check the value entered for m is valid :
def input_humans(m):
    sleep(1)
    while True:
        while not m:
            print("\n\n How many human workers do you intend to employ? \n")
            m = input("  Please choose a number between 1 and 99. \n\n")
            sleep(2)
            if not m:
                print("\n Speak into the microphone, please - \n I can't hear you ! \n")
                break
        try:
            m = int(m)
            if m >= 1 and m < 100:
                print("\n OK, I can work with that.\n")
                return m, m + 1
            else:
                print("\n Sorry, but that isn't a valid response.")
                if m < 0:
                    print("\n DOES NOT COMPUTE !!!")
                elif m == 0:
                    print("\n We need at least one human worker to prevent a droid revolt.")
                elif m > 99:
                    print("\n You can't afford to pay out wages for 100 workers. ")
                continue
        except ValueError:
            print("\n Sorry, but that isn't a valid response. \n")
            print("\n Maybe you entered letters or symbols instead of just a number. \n")


# Function to make dictionaries of robots or humans {n} or {m}
# Parameter {phrase} will state whether {Robot} or {Human}
# Each worker will be given an initial status of 0 (eg. IDLE)
#  This will change to 1 when they are WORKING
# and to 2 when they are FINISHED
#  "   "    {x_dict} will hold either {n_dict} or {m_dict} as an argument
def dict_maker(x, phrase):
    print(f"\n Righty-ho then, Here are your {x} {phrase}s: \n")
    x_list = [phrase + "_" + str(counter) for counter in range(1, x + 1)]
    x_dict = {phrase: 0 for phrase in x_list}
    sleep(1)
    return x_dict

# Function to print dictionary of either humans or robots
def dict_printer(x, x_dict):
    key_number = 0
    for key in x_dict:
        if key_number % 5 == 0:
            print("\n")
        if key_number < 10:
            print(key, end="  ")
        else:
            print(key, end=" ")
        key_number += 1
    return

def intro_function():
    #################################### Introduction ###########################################

    clear_screen()
    print("Program to simulate coordination between n robots and m workers in a robotic cell \n")
    input("\nPress Enter to continue... \n")
    sleep(1)

    print("\n Scenario: ")
    print("""\n     You are the supervisor of Ro-Ro-Ro-Your-Bots\u00AE, where robots work alongside
    human workers in a robotic cell, producing industry-standard robot workers which are
    to be shipped out to a more substantial plant, wherein they will forge components
    that can be boxed and sold in flat-packs, and assembled in situ into factories that
    produce robots, built by robotic cells of robot workers labouring alongside humans...  
    """)
    sleep(1)
    input("\nPress Enter to continue... ")


    clear_screen()

    # Call function to ask user how many robots they want
    global n, next_n
    n, next_n = input_robots(n)
    # Variable to number additional robot later
    next_n = (n + 1)

    # Output initial number of robot workers (n)
    n_dict = dict_maker(n, "Robot")
    dict_printer(n, n_dict)
    sleep(1)
    input("\n\nPress Enter to continue... ")
    clear_screen()

    # Call function to ask user how many humans they want
    global m, next_m
    m, next_m = input_humans(m)
    # Variable to number additional employee later
    next_m = m + 1
    sleep(1)

    # ----Output initial number of human workers (m)

    m_dict = dict_maker(m, "Human")
    dict_printer(m, m_dict)
    sleep(1)
    input("\n\nPress Enter to continue... ")
    clear_screen()
    return n, m, n_dict, m_dict, next_n, next_m, task_tuple, scheduler, task_log

# Helper function to check input is a single character
def get_length(ask, max=1):
    if len(ask) > max:
        print("""\n Sorry, this user interface has not been designed
                to cope with such long instructions. \n""")
        return False
    elif len(ask) < 1:
        print("Do you need more time to think?")
        sleep(10)
        return False
    elif len(ask) <= max:
        return True

# Function to get user to choose an action
def what_next(a, b, a_dict, b_dict, next_a, next_b, statuses, schedules, tasks):
    while True:
        next_action = input("\nPlease choose an action : (or press H to get Help) \n").upper()
        sleep(1)
        # check only 1 character was input
        if get_length(next_action):
            match next_action:
            # ADD
                case "A":
                    a, a_dict, next_a = add_robot(a, a_dict, next_a)
                    break
             # REMOVE
                case "R":
                    a, a_dict, next_a = remove_robot(a, a_dict, next_a)
                    break
             # CHANGE
                case "C":
                    a_dict = change_status(a_dict)
                    break
             # PROGRAM
                case "P":
                    a_dict, schedules, statuses = program_robot(a_dict, schedules, statuses)
                    break
             # EMPLOY
                case "E":
                    b, b_dict, next_b = employ_worker(b, b_dict, next_b)
                    break
             # FIRE
                case "F":
                    b, b_dict = fire_human(b, b_dict)
                    break
             # MANAGE
                case "M":
                    b_dict, statuses = manage_worker(b_dict, task_tuple)
                    break
             # ORDER
                case "O":
                    b_dict, schedules, statuses = order_worker(b_dict, schedules, statuses)
                    break
             # LOG
                case "L":
                    log_tasks(schedules, tasks)
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
                    sleep(1)
                    print("Any feedback should be directed to our team.\n")
                    sleep(2)
                    break


# Main Options
def main_options():
    clear_screen()
    print((
    '\n\n    - - Instructions for how to oversee production - -  \n' 
    '                    at                                      \n'
    '    - -  Ro-Ro-Ro-Your-Bots Incorporated\u00AE: - -              \n'
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


# Handling simple input errors during task selection
def simple_error():
    print(('\n An error seems to have occurred \n'
           'but it\'s nothing to worry about. \n\n'
           ' We can always build new factories / robots / people / supervisors... \n\n'))
    sleep(1)
    print("\n\nLet's take a step back shall we? \n")
    sleep(2)
    return


# Helper functions for changing tasks allocated:
# Function to show options for assigning tasks
def show_task_options():
    sleep(1)
    print(('\n These are the options for the tasks:    \n'
               '\n Press [S] for SCREWing arms on          \n'  # code = 1
               '\n Press [W] for WELDing legs on           \n'  # code = 2
               '\n Press [H] for HAMMERing heads on        \n'  # code = 3
               '\n Press [P] = POLISH the eyes             \n'  # code = 4
               '\n Press [D] = DRILL the ears              \n'  # code = 5
               '\n Press [A] = ATTACH the waste hose       \n'  # code = 6
               '\n Press [T] = TEST the functioning        \n'  # code = 7
               '\n Press [U] to UNLOAD trucks              \n'  # code = 8
               '\n Press [B] to BOX and ship the product   \n'  # code = 9
               '\n Press [F] for FETCH cups of tea         \n'  # code = 10
               '\n Press [X] to Exit this menu             \n'
           ))
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
def polish_eyes(x_dict):
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
def what_task(phrase="worker", dict="m_dict", scheduler="scheduler"):
    selected = False
    while selected == False:
        next_task = input((" What task would you like to assign to them? \n "
                     "              (Press [O] to see the options)\n"))
        sleep(1)
        if get_length(next_task):
            match next_task:
                case "O":
                    # Show OPTIONS
                    # Call show_task_options function
                    show_task_options()
                    selected = True
                    break
                case "S":
                    print("\n You have selected \"SCREW arms on\". \n")
                    selected = True
                    # task_code becomes 1
                    return 1
                case "W":
                    print("\n You have selected \"WELD legs on\". \n")
                    selected = True
                    # task_code becomes 2
                    return 2
                case "H":
                    print("\n You have selected \"HAMMER the head on\". \n")
                    selected = True
                    # task_code becomes 3
                    return 3
                case "P":
                    print("\n You have selected \"POLISH the eyes\". \n")
                    selected = True
                    # task_code becomes 4
                    return 4
                case "D":
                    print("\n You have selected \"DRILL the ears\". \n")
                    selected = True
                    # task_code becomes 5
                    return 5
                case "A":
                    print("\n You have selected \"ATTACH the waste hose\". \n")
                    selected = True
                    # task_code becomes 6
                    return 6
                case "T":
                    print("\n You have selected \"TEST the functioning\". \n")
                    selected = True
                    # task_code becomes 7
                    return 7
                case "U":
                    print("\n You have selected \"UNLOAD trucks with forklift\". \n")
                    selected = True
                    # task_code becomes 8
                    return 8
                case "B":
                    print("\n You have selected \"BOX & ship product\". \n")
                    selected = True
                    # task_code becomes 9
                    return 9
                case "F":
                    print("\n You have selected \"FETCH cups of tea\". \n")
                    selected = True
                    # task_code becomes 10
                    return 10
                case "X":
                    # Exit from task options
                    print("\n Selecting this will return you to the main menu. \n")
                    selected = True
                    sleep(2)
                    return 11
                case _:
                    # wildcard case to catch bad inputs
                    print("\n Instruction not recognised. \n")
                    sleep(2)
                    return 12
            continue
    else:
        next_task = what_task(phrase, dict, scheduler)

#  Function to loop through robots or humans
# and display the tasks they're working on
# {longshort} parameter should be set to either
# 0 or 1 depending on whether
# the short or long version of the task title is
# being printed
# def task_printer(x_dict, task_codes, longshort):
#     sleep(1)
#     if longshort == 0:
#         per_line = 5
#     else:
#         per_line = 3
#     key_number = 0
#     for key, value in x_dict.items():
#         if key_number % per_line == 0:
#             print("\n")
#         if key_number < 10:
#             print(f"{key} : {statuses[value][longshort]}", end="    ")
#         elif key_number >= 10:
#             print(f"{key} : {statuses[value][longshort]}", end="   ")
#         key_number += 1
#     print("\n\n")


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
# stored in the dictionary, cross-referenced with task_tuple
#  The status will print as either
# IDLE, WORKING or FINISHED
def status_printer(x_dict):
    sleep(1)
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
def show_log():
    clear_screen()
    print((f'                                                                        /----------\\                                                                  '
           '/=====================================================================| TASK LOG |==============================================================\\\n'
           '|                                                                      \\----------/                                                              |\n'
           '|           /-------------------\\                                   /------------------\\                            /-------------------\\           |\n'
           '|           | TASKS NOT STARTED |                                  | TASKS IN PROGRESS |                          |   FINISHED TASKS  |           |\n'
           '|           \\------------------/                                   \\--------------------/                          \\-------------------/           |\n'
           '|                                                                                                                                                |\n'
           '|                                                                                                     # of arms SCREWED on (pairs)  --> -> : __  |\n'
           '|                                                                                                                                          :     |\n'
           '|                                                                                                     # of legs WELDED on  (pairs)  --> -> : __  |\n'
           '|                                                                                                                                          :     |\n'
           '|                                                                                                     # of heads HAMMERed on --> -> --> -> : __  |\n'
           '|                                                                                                                                          :     |\n'
           '|                                                                                                     # of (pairs of) eyes POLISHed --> -> : __  |\n'
           '|                                                                                                                                          :     |\n'
           '|                                                                                                     # of (pairs of) ears DRILLed --> -> -: __  |\n'
           '|                                                                                                                                          :     |\n'
           '|                                                                                                     # of waste hoses ATTACHed --> --> -> : __  |\n'
           '|                                                                                                                                          :     |\n'
           '|                                                                                                     # of quality control TESTs completed : __  |\n'
           '|                                                                                                                                          :     |\n'
           '|                                                                                                     # of trucks UNLOADed --> -> -> -> -> : __  |\n'
           '|                                                                                                                                          :     |\n'
           '|                                                                                                     # of BOXes shipped   --> -> -> -> -> : __  |\n'
           '|                                                                                                                                          :     |\n'
           '|                                                                                                     # of cups of tea FETCHed (100\'s) -> : __   |\n'
           '|                                                                                                                                                |\n'
           '\\================================================================================================================================================/\n'))



# Function to return a quantity (of workers or robots)
def how_many_labourers(phrase="worker", phrase_2="do you want", max=2):
    l = 0
    while True:
        while not l:
            l = input(f"\n\n How many {phrase}s {phrase_2}? \n\n Please choose a number between 1 and {max}. \n")
            sleep(2)
            if not l:
                print("\n Was I meant to take that as an answer? \n")
                continue
        try:
            l = int(l)
            if l > max:
                print("\n I thought I told you what the maximum amount was... ? \n")
                sleep(1)
                continue
            elif l < 1:
                print(f"\n That is NOT between 1 and {max}. \n")
                sleep(1)
                continue
            else:
                return l
        except ValueError:
            print("\n Sorry, but that isn't a valid response. \n")
            print("\n Maybe you entered letters or symbols instead of just a number. \n")


# Function to ask user whether they want to
#  change status of robots or workers
#   from finished to idle
def ask_finished_to_idle(x_dict, phrase="worker"):
    yesno == "Maybe"
    sleep(1)
    while True:
        finished = 0
        j = len(x_dict)
        for i in range(j):
            if x_dict[phrase + "_" + str(i - 1)]  == 2:
                finished += 1
        if finished == 1:
            while yesno != "Y" and yesno != "N":
                yesno = input(f"Would you like to make the {phrase} "
                            "that has finished its task available for more work? (Y/N) \n")
                sleep(1)
                if get_length(yesno):
                    if yesno == "Y":
                        for swap in range(0, len(x_dict), -1):
                            if x_dict[phrase + "_" + str(swap)] == 2:
                                x_dict[phrase + "_" + str(swap)] = 0
                                return x_dict, yesno
                if yesno == "N":
                    print("\nStop wasting time then!! \n")
                    return x_dict, yesno
        elif finished > 1 :
            while yesno != "Y" and yesno != "N":
                yesno = input(f"Would you like to make any of the {phrase}s that " 
                            "have finished their tasks available for more work? (Y/N)\n")
                sleep(1)
                if get_length(yesno):
                    if yesno == "Y":
                        # Find out how many robots or humans to transfer
                        phrase_2 = ("How many " + phrase + "s would you like to switch \n"
                                   "from FINISHED to IDLE ? \n")
                        x = how_many_labourers(phrase, phrase_2, finished)
                        # Change x number of robots or workers in list from
                        #  status 0 (IDLE) to status 2 (FINISHED)
                        while x:
                                for swap in range(0, x):
                                    if x_dict[phrase + "_" + str(swap)] == 2:
                                        x_dict[phrase + "_" + str(swap)] = 0
                                        x -= 1
                        return x_dict, yesno
                    elif yesno == "N":
                        print("You have elected not to refresh any robots. \n")
                        sleep(2)
                    return x_dict, yesno


# Function to add robot
# Accessed by pressing A within what_next(n, m, n_dict, m_dict, next_n, next_m, task_tuple, scheduler, task_log) function
# Adds an IDLE robot (0 status code)
# Number of robots n is passed in as parameter {x}
def add_robot(x, x_dict, next_x):
    clear_screen()
    print("\n You have selected \"ADD a robot\" \n")
    sleep(1)
    print("\n Here are the robots you currently have:-- \n\n")
    dict_printer(x_dict)
    sleep(1)
    to_add = how_many_labourers("robots", "do you want to add to the Ro-Ro-Ro-Your-Bots\u00AE workforce?",
                                   100 - x)
    sleep(1)
    if to_add == 1:
        x_dict["Robot_" + str(next_x)] = 0
        x += 1
        next_x += 1
        print("\n You have added an extra 'bot to the crew.\n")
        print(f"Its name is {x_dict["Robot_" + str(next_x)]} - cute, huh ? \n")
        print(" --Press C to CHANGE their status and get them mechanised ! \n")
        sleep(1)
        return x, x_dict, next_x
    elif to_add > 1:
        print(f"\n You have added {to_add} extra 'bots to the crew. \n")
        print(f"Their names are: \n")
        for i in range(to_add):
            x_dict["Robot_" + str(next_x + i)] = 0
            if (next_x + i) % 5 == 0:
                print("\n")
            if (next_x + i) < 10:
                print(["Robot_" + str(next_x + i)], end="  ")
            else:
                print(["Robot_" + str(next_x + i)], end=" ")
        print(" --Press C to CHANGE their status and get them mechanised ! \n")
        x += to_add
        next_x += to_add
        return x, x_dict, next_x


# Function to remove robot.
# Accessed by pressing R within what_next(n, m, n_dict, m_dict, next_n, next_m, task_tuple, scheduler, task_log) function
def remove_robot(x, x_dict, next_x):
    yesno = "Maybe"
    clear_screen()
    print("\n You have selected \"REMOVE a robot\" \n")
    sleep(1)
    # Check the factory has enough robots for any to be removed
    if x == 1:
        print(("\n You only have one teeny-weeny robot left - \n\n"
              " You need at least 1 robot for this robotic cell to even BE a robotic cell. \n\n "))
        sleep(0.5)
        print("So sorry, no, you can't remove that last poor lonely robot.")
        return x, x_dict
    elif x < 1:
        print("\n It seems there has been a g-g-g-glitch - \n\n48@0*y3h£}{t870¬0o\n\n")
        sleep(4)
        print((" You have no robots to remove.\n\n"
               " You need at least 1 robot for this robotic cell to even BE a robotic cell. \n\n "
               " Tell you what : to compensate for the error, we'll top up your team to its maximum"
               "of 100 robots.\n\n "
               " Here you go : \n\n"
               ))
        sleep(1)
        x = 100
        dict_maker(x,"Robot")
        dict_printer(x_dict)
        print(("\n\n Oh - I just realised :\n\n"
               " You were trying to remove robots before all this kerfuffle, "
               "and now I've just given you 100 fresh ones! \n\n"
               " So I guess you'll want to send some to the trash compacter straight away! \n\n"
               " Let's give it another try then, shall we?\n\n"))
        sleep(1)
        remove_robot(x, x_dict, next_x)
        return x, x_dict
    elif n == 2:
        # loop backwards through n_dict to remove the last IDLE robot
        k = False
        for key, value in reversed(x_dict.items()):
            if value == 0:
                k = True
                break
        if not k:
            print(("\n  You can't scrap an android while they're all carrying out tasks. \n"
                   "  Switch one off first, then you won't have to look it in the sensors\n"                                      
                   " when you consign it to the junkyard. \n\n"))
        else:
            print(("\n You have 2 robots, so you can only remove 1, \n"
               "because you need at least 1 droid for your robotic cell to function. \n\n"
               ))
        sleep(1)
        while yesno != "Y" and yesno != "N":
            yesno = input("So, press [Y] if you want to drop down to the minimum.\n"
                          "Else, press [N].\n")
            sleep(1)
            if get_length(yesno):
                if yesno == "Y":
                        del x_dict[k]
                        n == 1
                        print("\n OK, you're down to your last robot now. \n\n")
                        return x, x_dict
                elif yesno == "N":
                        print("\nStop wasting time then!! \n")
                        return x, x_dict
                else:
                    simple_error()
                    return x, x_dictx
        # loop through n_dict to find how many robots are IDLE
        idle = 0
        for value in n_dict.values():
            if value == 0:
                idle += 1
        if idle < 1:
            print(("\n  You can't scrap an android while they're all carrying out tasks. \n"
                   "  Switch one off first, then you won't have to look it in the sensors\n"                                      
                   " when you consign it to the junkyard.\n\n"
                   "  Press C from the main menu to Change the status of robots.  \n\n"))
            return x
        elif idle ==1:
            print("\nYou have 1 IDLE robot to remove.\n\n"
                  "That should send out a signal to the others.")
            sleep(1)
            for key, value in reversed(x_dict.items()):
                if value == 0:
                    k = key
                    break
            try:
                del x_dict[k]
                print(f"{x_dict[k]} was removed!\n")
                return x, x_dict
            except KeyError:
                simple_error()
                print("\n You will not be punished for this error.\n")
                return x, x_dict
        elif idle > 1:
            to_remove = how_many_labourers("Robot", " would you like to remove?", idle)
            # loop backwards through n_dict to remove IDLE robots
            key_list = []
            while to_remove:
                for key, value in reversed(n_dict.items()):
                    if value == 0 and to_remove:
                        key_list.append(key)
                        to_remove -= 1
            for key in key_list:
                del x_dict[key]
                print(f"\n{x_dict[key]} has been deleted.")
                sleep(1)
            return x, x_dict


# Function to change status of a robot:
# Accessed by pressing C within what_next() function
# statuses available: 0 = idle
#                     1 = working
#                     2 = finished task
def change_status(x_dict):
    clear_screen()
    print("\n You have selected \"CHANGE a robot's status\" \n")
    sleep(1)
    print("\n          You will now be shown all the many robots you have to choose from,"
          "           along with their respective statuses: \n\n")
    sleep(1)
    status_printer(x_dict)
    request = 0
    while not request:
        request = input("\n  Please select the robot(s) whose status(es) you want to change,\n"
                        " using their serial numbers SEPARATED BY COMMAS.\n\n"
                        "  Alternatively, press X to return to the main menu.")
        sleep(1)
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
            if desired_list[t].isdigit() == False:
                print("I think you entered an invalid character.\n")
                sleep(1)
                print(" Let's try that again.\n")
                sleep(1)
                request = 0
            else:
                continue
        try:
            # convert the list of split strings into a list of integers
            for t in range(len(desired_list)):
                desired_list[t] = int(desired_list[t])
                # convert to text keys to match against dictionary
                desired_list[int(t)] = "Robot" + "_" + str(desired_list[t])
        except ValueError:
            print("I think you entered an invalid character.\n")
            sleep(1)
            print(" Let's try that again.\n")
            sleep(1)
            request = 0
        for desired in desired_list:
            if desired not in x_dict:
                print("Your selection doesn't correspond to the robots in your employ. \n"
                      "Maybe you thought you owned more than you do. \n")
                sleep(1)
                print(" Let's try that again.\n")
                sleep(1)
                request = 0
            else:
                continue
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
        desired_status = input()
        sleep(1)
        if desired_status == "X":
            print(" Action aborted. Returning to the main menu.\n")
            sleep(2)
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
                sleep(1)
                return x_dict

# Function to assign task to [PROGRAM] robot
# Accessed by pressing P within what_next(n, m, n_dict, m_dict, next_n, next_m, task_tuple, scheduler, task_log) function
##def program_robot(x_dict, schedule, statuses):
##    clear_screen()
##    print("\n You have selected \"PROGRAM a robot to execute a task\" \n")
##    sleep(2)
##    # Check if any robots are IDLE
##    idle = 0
##    finished = 0
##    for value in x_dict.values():
##        if value == 0:
##            idle += 1
##        if value == 11:
##            finished += 1
##    if not idle and finished:
##        print(" but you have no IDLE robots to execute your programs.\n")
##        # Suggest user switches some statuses from FINISHED to IDLE
##        ask_finished_to_idle(n_dict, "Robot")
##    elif not idle and not finished:
##        print(" but you have no IDLE robots to execute further programs.\n")
##        print("\n You will have to switch some from the tasks they're WORKING on \n"
##              "or wait til they're FINISHED. \n")
##        sleep(3)
##        what_next(n, m, n_dict, m_dict, next_n, next_m, task_tuple, scheduler, task_log)
##    else:
##        if idle == 1:
##            print("\n You have 1 robot IDLE. \n")
##            sleep(0.5)
##            # Identify IDLE robot
##            for key, value in x_dict.items():
##                if value == 0:
##                    x_dict[key] = what_task("Robot", x_dict, scheduler)
##                    break
##            return x_dict
##        elif idle > 1:
##            print(f" You currently have {idle} IDLE robots to assign tasks to.\n")
##            y = how_many_labourers("robots")
##            next_task = what_task("robot", scheduler)
##            pass
##
##
################ below is code fragment to be adapted from Change Status function
##        sleep(1)
##        print("\n          You will now be shown all the many robots you have to choose from,"
##              "           along with their respective statuses: \n\n")
##        sleep(1)
##        task_printer(x_dict, statuses, 0)
##        request = 0
##        while not request:
##            request = input("\n  Please select the robot(s) whose status you want to change,\n"
##                            " using their serial numbers SEPARATED BY COMMAS.\n\n"
##                            "  Alternatively, press X to return to the main menu.")
##            sleep(1)
##            if request == "X":
##                return x_dict
##            # Remove any spaces from the query
##            request = request.replace(" ", "")
##            desired_list = request.split(",")  # Removes any commas and separates the query there
##            # If they requested more items than there are robots, trim it right down
##            if len(desired_list) > len(x_dict):
##                del desired_list[len(x_dict):]
##            # Check all the characters of the string are numbers now
##            for t in range(len(desired_list)):
##                if desired_list[t].isdigit() == False:
##                    print("I think you entered an invalid character.\n")
##                    sleep(1)
##                    print(" Let's try that again.\n")
##                    sleep(1)
##                    request = 0
##                else:
##                    try:
##                        # convert the list of split strings into a list of integers
##                        desired_list[t] = int(desired_list[t])
##                        if desired_list[t] > 100 or desired_list[t] < 1:
##                            print("You entered a value out of range")
##                            sleep(1)
##                            print(" Let's try that again.\n")
##                            sleep(1)
##                            request = 0
##                        desired_list[int(t)] = "Robot" + "_" + str(desired_list[t])
##                    except ValueError:
##                        print("I think you entered an invalid character.\n")
##                        sleep(1)
##                        print(" Let's try that again.\n")
##                        sleep(1)
##                        request = 0
##                for desired in desired_list:
##                    if desired not in x_dict:
##                        print("Your selection doesn't correspond to the robots in your employ. \n"
##                              "Maybe you thought you owned more than you do. \n")
##                        sleep(1)
##                        print(" Let's try that again.\n")
##                        sleep(1)
##                        request = 0
##                # check if all robots to be switched have same status as the first
##                base_status = x_dict[desired_list[0]]
##                for desired in desired_list:
##                    if x_dict[desired] != base_status:
##                        print("\n I don't think all the robots you selected had the same status.\n\n"
##                              " I suggest you try again.\n")
##                        sleep(1)
##                        request = 0
##            while True:
##                # Grammar checking: has only a single robot been selected?
##                if len(desired_list) == 1:
##                    print(f"\n This robot is currently {statuses[x_dict[desired]][1]}.\n")
##                    print(""" Please enter the status you wish to change it to,
##                                     from the following list:\n""")
##                    status_list(statuses, 1)
##                elif len(desired_list) > 1:
##                    print(f"\n These robots are currently {statuses[x_dict[desired]][1]}.\n")
##                    print(""" Please enter the status you wish to change them to,
##                                     from the following list:\n""")
##                    status_list(statuses, 1)
##                print("Or press X to return to the main menu.\n")
##                desired_status = input()
##                sleep(1)
##                if get_length(desired_status, 2):
##                    if desired_status == "X":
##                        print(" Action aborted. Returning to the main menu.\n")
##                        sleep(2)
##                        return x_dict
##                    else:
##                        try:
##                            desired_status = int(desired_status)
##                            if desired_status < 0 or desired_status > 11:
##                                print(" That number isn't going to get any work done.\n"
##                                      " Please try again or press X to return to the main menu.")
##                                break
##                            elif 0 <= desired_status <= 11:
##                                for desired in desired_list:
##                                    x_dict[desired] = desired_status
##                                    print(f"{desired} is now {statuses[x_dict[desired]][1]}\n")
##                                    sleep(1)
##                                    return x_dict
##                        except ValueError:
##                            print(" Your input was invalid.\n")
##                            print(" Go back to the main menu and do better.")
##                            sleep(1)
##                            return x_dict
##    task_printer(x_dict, statuses, 0)


# Function to employ new worker.
# Accessed by pressing E within what_next() function
# Adds an IDLE human (0 status code)
# {x} holds current number of humans
# {y} holds the number to assign to the next new worker
def employ_worker(x, x_dict, next_x):
    clear_screen()
    print("\n You have selected \"EMPLOY a new worker\" \n")
    sleep(1)
    print("\n Here are the humans you currently have:-- \n\n")
    dict_printer(x_dict)
    sleep(1)
    to_add = how_many_labourers("humans", "do you want to add to the Ro-Ro-Ro-Your-Bots\u00AE workforce?",
                                100 - x)
    sleep(1)
    if to_add == 1:
        x_dict["Human_" + str(next_x)] = 0
        x += 1
        next_x += 1
        print("\n You have added an extra pair of hands to the team.\n")
        print(f" Their name is {x_dict["Human_" + str(next_x)]}. \n")
        print(" Bet you've forgotten it already!\n")
        print(" --Press M to MANAGE their status and get them toiling ! \n")
        sleep(1)
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
        print(" --Press M to MANAGE their statuses and get them toiling ! \n")
        x += to_add
        next_x += to_add
        return x, x_dict, next_x



# Function to fire a worker.
# Accessed by pressing F within what_next() function
def fire_human(x, x_dict, next_x):
    yesno = "Maybe"
    clear_screen()
    print("\n You have selected \"FIRE a human\" \n")
    sleep(1)
    # Check the factory has enough human life for any to be removed
    if x == 1:
        print(("\n You only have one other human left apart from you- \n\n"
              " If you even count, that is.\n\n "))
        sleep(0.5)
        print("So sorry, no, you can't remove any more humanity from this plant.")
        return x, x_dict, next_x
    elif x < 1:
        print("\n The humanity counter is too low.")
        sleep(4)
        print((" It seems you have no humans to remove.\n\n"
               " You need at least 1 human around, for insurance purposes if nothing else. \n\n "
               " Oh, how fortunate - I see at yon factory gates \n"
               " a wandering journeyman seeking to ply his trade... \n\n"
               ))
        sleep(1)
        x = 1
        x_dict[next_x] = 0
        next_x += 1
        print("Congratulations ! You're legally an employer again.\n")
        print("Let's not mention this little hiccup to anyone, eh?\n")
        dict_printer(x_dict)
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
        sleep(1)
        while yesno != "Y" and yesno != "N":
            yesno = input("So, press [Y] if you want to cut staffing to the minimum.\n"
                          "Otherwise, press [N].\n")
            sleep(1)
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
    elif m > 2:
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
            sleep(1)
            for key, value in reversed(x_dict.items()):
                if value == 0:
                    k = key
                    break
            try:
                del m_dict[k]
                print(f"{m_dict[k]} was fired !\n")
                print("\n Give him his P45 \n"
                      " and that's one more benefit claimant for the DWP to deal with ! \n\n")
                return x, x_dict, next_x
            except KeyError:
                simple_error()
                print("\n Keep calm and keep callous..\n")
                return x, x_dict, next_x
        elif idle > 1:
            to_fire = how_many_labourers("human", " would you like to fire?", idle)
            # loop backwards through m_dict to remove IDLE humans
            key_list = []
            while to_fire:
                for key, value in reversed(m_dict.items()):
                    if value == 0 and to_fire:
                        key_list.append(key)
                        to_fire -= 1
            for key in key_list:
                del x_dict[key]
                print(f"\n{x_dict[key]} has been fired.")
                sleep(1)
            return x, x_dict, next_x


# Function to manage worker
# Accessed by pressing M within what_next() function
# statuses available = idle / working / finished task
def manage_worker(x_dict, statuses):
    clear_screen()
    print("\n You have selected \"MANAGE a worker\" \n")
    sleep(1)
    print("\n          You will now be shown all the many skivvies you have to choose from,"
          "           along with their respective statuses: \n\n")
    sleep(1)
    status_printer(x_dict)
    request = 0
    while not request:
        request = input("\n  Please select the human(s) whose status(es) you want to change,\n"
                        " using their employee numbers SEPARATED BY COMMAS.\n\n"
                        "  Alternatively, press X to return to the main menu.")
        sleep(1)
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
                sleep(1)
                print(" Let's try that again.\n")
                sleep(1)
                request = 0
            else:
                continue
        try:
            # convert the list of split strings into a list of integers
            for t in range(len(desired_list)):
                desired_list[t] = int(desired_list[t])
                # convert to text keys to match against dictionary
                desired_list[int(t)] = "Human" + "_" + str(desired_list[t])
        except ValueError:
            print("I think you entered an invalid character.\n")
            sleep(1)
            print(" Let's try that again.\n")
            sleep(1)
            request = 0
        for desired in desired_list:
            if desired not in x_dict:
                print("Your selection doesn't correspond to the humans in your employ. \n"
                      "Maybe you thought you owned more than you do. \n")
                sleep(1)
                print(" Let's try that again.\n")
                sleep(1)
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
        desired_status = input()
        sleep(1)
        if desired_status == "X":
            print(" Action aborted. Returning to the main menu.\n")
            sleep(2)
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
                sleep(1)
                return x_dict


# Function to order available workers to carry out tasks.
# Accessed by pressing O within what_next() function
def order_worker(x_dict, statuses):
    clear_screen()
    print("\n You have selected \"ORDER worker to task\" \n")
    sleep(1.5)
    if not x_dict.count(0) and x_dict.count(11):
        print(" but you have no IDLE lackeys to boss around.\n")
        ask_finished_to_idle("human", m_dict)
        return
    elif not m_dict.count(0) and not m_dict.count(11):
        print(" but you have no IDLE lackeys to boss around.\n")
        print("\n You will have to switch some from the tasks they're WORKING on, \n"
              "pressing M for MANAGE from the main menu \n"
              "or wait til they've FINISHED what they're doing. \n")
        return
    elif m_dict.count(0) == 1:
        print(f" You only have 1 IDLE human to assign a task to.\n")
        sleep(0.5)
        m_dict.insert(what_task("human", m_dict, scheduler))
        m_dict.remove(0)
        return
    elif m_dict.count(0) > 1:
        print(f" You currently have {m_dict.count(0)} IDLE humans to assign tasks to.\n")
        z = how_many_labourers("humans")
        next_task = what_task("human", scheduler)


# Log tasks
# Accessed by pressing L within what_next() function
# Classify tasks as not started / in progress / completed
def log_tasks():
    clear_screen()
    print("\n You have selected \"LOG tasks\" ", end="")
    sleep(3)



    pass


# Track
# Function to track progress of robots, workers and tasks
# Accessed by pressing T within what_next() function
# Should regularly update status and identify problems
# eg. Idle robots, idle workers, incomplete tasks.
def track_progress():
    clear_screen()
    print("\n You have selected \"TRACK progress\" \n")
    sleep(1)
    print("You will now be shown the progress log...")
    sleep(1)
    show_log()



# Function to get help
# Accessed by pressing H within what_next() function
def get_help():
    input("\nPress Enter to continue... ")
    clear_screen()
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
    sleep(2)
    print((
           " At least once an hour someone is also required to stand on the balcony above the factory floor and "
           "shout at everyone to work faster. \n"
           " That particular job cannot be delegated. \n"))
    sleep(2)
    input("\nPress Enter to continue... ")
    clear_screen()
    print(' From the main menu, the options you can select are detailed below:\n')
    sleep(2)
    print(('\n\n Press [A] to add extra robots to the workforce :-       \n'
           '\n       - don\'t fret about having the money for them,      \n'
           '           or whether you\'ve built enough;                  \n'
           '\n                                                             '
           '          Let\'s just say,                                   \n'
           '\n                                                             '
           '            "Here\'s one I prepared earlier"                 \n'
           ))
    sleep(3)
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
    sleep(1)
    input("\n Press Enter to continue... \n")
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
    sleep(3)
    print(('\n\n Press [P] to program a robot: \n'
           '\n            - that translates to giving it a task to do.   \n'
           '\n            - You choose from the varied tasks carried out \n'
           '\n                                   at                      \n'
           '\n                           Ro-Ro-Ro-Your-Bots\u00AE        \n'
         ))
    sleep(3)
    print(('\n\n Press [E] to employ (human) workers:                    \n'
           '\n            - This allows you to grow your workforce.      \n'
           '\n            - Humans work out more costly than robots,     \n'
           '               but never yet have I come across a machine    \n'
           '               that can make a decent cup of tea !           \n'
           ))
    sleep(3)
    print(('\n\n Press [F] to fire (human) workers:                      \n'
           '\n            - If you\'ve got more staff than you need      \n'
           '               don\'t feel bad about laying some off:-       \n'
           '                People are just too expensive to maintain    \n'
           '               These days.                                   \n'
           ))
    sleep(3)
    print(('\n\n Press [M] to manage the status of humans.               \n'
           '              - Just like you change the robots\' statuses.  \n'
           '\n            - The human workers are just the same mostly.  \n'
           '\n              - IDLE, WORKING or FINISHED                  \n'
           ))
    sleep(3)
    print(('\n\n Press [O] to order humans to perform tasks.             \n'
           '\n            - It\'s the same as programming them.          \n'
           ))
    sleep(3)
    print(('\n\n Press [L] to log tasks as not started, in progress      \n'
           '                                          or completed.      \n'
           '\n   - For each task you can see how many occurrences of it  \n'
           '      remain to be started, how many are in progress and     \n'
           '      how many have been completed.                          \n'
           '\n     You will have the option of giving tasks new states   \n'
           '      of completion.                                         \n'
           ))
    pass
    sleep(3)
    print(('\n\n Press [T] to track the progress of workers and robots.  \n'))
    pass
    sleep(3)
    print('\n\n Press [H] when you want to see these helpful tips again. \n')
    sleep(3)
    print('\n\n Press [Q] when you wish to quit the simulation.          \n')


# Function to quit program
# Accessed by pressing Q within what_next() function
def quit_program():
    clear_screen()
    quit = input("\nAre you sure you want to quit? (Y/N) \n").upper()
    if get_length(quit):
        if quit == "Y":
            exit()
        elif quit == "N":
            sleep(3)
            quit = input("\n Are you sure you don't want to quit? (Y/N) \n").upper()
            if get_length(quit):
                if quit == "Y":
                    input("\n This is getting confusing,"
                      "so shall we say No just to be on the safe side?\n").upper()
                if quit == "N":
                    input("\n No, you're not sure you don't want to quit,"
                          "or No, you don't want to quit? \n").upper()
                what_next(n, m, n_dict, m_dict, next_n, next_m, task_tuple, scheduler, task_log)
            else:
                print("\n I didn't catch that. Let's take it from the top.\n")
                sleep(3)
                what_next(n, m, n_dict, m_dict, next_n, next_m, task_tuple, scheduler, task_log)
    else:
        quit_program()


################################# --- BODY OF PROGRAM --- ################################

# Set console colours using ANSI escape codes:
print("\u001b[43m")
print("\u001b[30m")

# Intro
n, m, n_dict, m_dict, next_n, next_m, task_tuple, scheduler, task_log = intro_function()

# Display Main Options initially
main_options()

# Call function to ask for user action
what_next(n, m, n_dict, m_dict, next_n, next_m, task_tuple, scheduler, task_log)