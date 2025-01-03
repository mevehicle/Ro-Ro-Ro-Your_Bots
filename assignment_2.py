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

# The status codes can be deciphered by
#  using them as the index numbers of a tuple
#   called status_tuple, containing corresponding activities

# ----- Status codes are as follows:
# Status = 0 : IDLE
#  "  "  = 1 : SCREWing the arms on
#  "  "  = 2 : WELDing the legs on
#  "  "  = 3 : HAMMERing the head on
#  "  "  = 4 : POLISHing the eyes
#  "  "  = 5 : DRILLing the ears
#  "  "  = 6 : ATTACHing the waste hose
#  "  "  = 7 : TESTing the functioning
#  "  "  = 8 : UNLOADing trucks with forklift
#  "  "  = 9 : BOXing and shipping product
#  "  "  = 10: FETCHing cups of tea
#  "  "  = 11: FINISHED task & ready for reassignment

status_tuple = ("IDLE", "SCREWing", "WELDing", "HAMMERing", "POLISHing", "DRILLing",
                "ATTACHing", "TESTing", "UNLOADing", "BOXing", "FETCHing", "FINISHED_TASK")

# The scheduler dictionary will be a database showing, for each task(i),
# how many robots and how many workers are working on them,
# eg. scheduler[i[robots, humans]

scheduler = {}
for i in range(1, 11):
    scheduler[status_tuple[i]] = [0, 0]

# The task log is a dictionary showing, for each task,
# how many repetitions of that task have been completed
# and whether any workers or robots are currently engaged in it
# eg. task_log[i[completed, in progress
task_log ={}
for i in range(1,11):
    task_log[status_tuple[i]] = [0, 0]

# Function to clear screen and return cursor to top left corner
def clear_screen():
    # Clear screen using ANSI escape sequence
    print("\u001b[2J")
    # Cursor to home using ANSI escape sequence
    print("\u001b[H")
    sleep(1)



# Function to ask user how many robots they intend to employ (n):
# ---- & check the value entered for n is valid :
def input_robots():
    sleep(2)
    n = 0
    while True:
        print("\n How many robot workers do you want for your factory?\n\n")
        n = input("  Please choose a number between 1 and 100. \n\n")
        sleep(3)
        if not n:
            print("\n Excuse me, but I asked you a question! \n")
        try:
            n = int(n)
            if n >= 1 and n <= 100:
                return n
            else:
                print("\n Sorry, but that isn't a valid response. \n")
                if n < 0:
                    print("\n How can we have a negative amount? We don't owe nobody our robots !!\n")
                elif n == 0:
                    print("\n We can't build robots with no robots to build them. \n")
                elif n > 100:
                    print("\n We can't risk having that many droids onsite. \n")
                    sleep(0.5)
                    print("\n      HAVE YOU NEVER SEEN BLADE RUNNER? \n")
        except ValueError:
            print("\n Sorry, but that isn't a valid response. \n")
            print("\n Maybe you entered letters or symbols instead of just a number. \n")


# Function to ask user how many humans they intend to employ (m):
# ---- & check the value entered for m is valid :
def input_humans():
    sleep(2)
    while True:
        m = 0
        while not m:
            m = input(("\n\n How many human workers do you intend to employ? \n"
                       "  Please choose a number between 1 and 100. \n\n"))
            sleep(3)
            if not m:
                print("\n Speak into the microphone, please - \n I can't hear you ! \n")
        try:
            m = int(m)
            if m >= 1 and m <= 100:
                print("\n OK, I can work with that.\n")
                return m
            else:
                print("\n Sorry, but that isn't a valid response.")
                if m < 0:
                    print("\n DOES NOT COMPUTE !!!")
                elif m == 0:
                    print("\n We need at least one human worker to prevent a droid revolt.")
                elif m > 100:
                    print("\n You can't afford to pay out wages for over 100 workers. ")
                continue
        except ValueError:
            print("\n Sorry, but that isn't a valid response. \n")
            print("\n Maybe you entered letters or symbols instead of just a number. \n")


# Function to make dictionaries of robots or humans {n} or {m}
# Parameter {phrase} will state whether {Robot} or {Human}
# Each worker will be given an initial status of 0 (eg. IDLE)
#  "   "    {x_dict} will hold either {robot_dict} or {human_dict} as an argument
def dict_maker(x, phrase):
    print(f"\nOK, Here are your {x} {phrase}s: \n")
    x_list = [phrase + "_" + str(counter) for counter in range(1, x + 1)]
    x_dict = {phrase: 0 for phrase in x_list}
    sleep(5)
    return x_dict

# Function to print dictionary of either humans or robots
def dict_printer(x_dict):
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


    clear_screen()

    # Call function to ask user how many robots they want
    n = input_robots()
    sleep(2)

    # Output initial number of robot workers (n)
    global robot_dict
    robot_dict = dict_maker(n, "Robot")
    dict_printer(robot_dict)
    sleep(3)
    input("\n\nPress Enter to continue... ")
    clear_screen()

    # Call function to ask user how many humans they want
    m = input_humans()
    sleep(2)

    # ----Output initial number of human workers (m)
    global human_dict
    human_dict = {}
    human_dict = dict_maker(m, "Human")
    dict_printer(human_dict)
    sleep(3)
    input("\n\nPress Enter to continue... ")
    clear_screen()

# Helper function to check input is a single character
def get_length(ask):
    if len(ask) > 1:
        print("""\n Sorry, this user interface has not been designed
                to cope with such long instructions. \n""")
        return False
    elif len(ask) < 1:
        print("Do you need more time to think?")
        sleep(10)
        return False
    elif len(ask) == 1:
        return True

# Function to get user to choose an action
def what_next():
    global robot_dict
    global human_dict
    sleep(1)
    next_action = input("\nPlease choose an action (or press H to get Help) \n").upper()
    sleep(2)
    # check only 1 character was input
    if get_length(next_action):
        match next_action:
        # ADD
            case "A":
                add_robot(n)
         # REMOVE
            case "R":
                remove_robot(n)
         # CHANGE
            case "C":
                change_status()
         # PROGRAM
            case "P":
                program_robot(scheduler, status_tuple)
         # EMPLOY
            case "E":
                employ_worker(m)
         # FIRE
            case "F":
                fire_worker(m)
         # MANAGE
            case "M":
                manage_worker()
         # ORDER
            case "O":
                order_worker(scheduler, status_tuple)
         # LOG
            case "L":
                log_tasks(scheduler)
         # TRACK
            case "T":
                track_progress(status_tuple, scheduler)
         # HELP
            case "H":
                get_help()
         # QUIT
            case "Q":
                quit_program()
        # SANITISE INPUT
            case _:
                print("Sorry, I don't think that's a valid option.\n")
                sleep(3)
                print("Any feedback should be directed to our team.")
                sleep(5)
                what_next()
    else:
        what_next()


# Basic Instructions
def instructions():
    clear_screen()
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


# Helper function to determine what task
def what_task(phrase="worker", dict="human_dict", scheduler="scheduler"):
    next_task = input((" What task would you like to assign to them? \n "
                 "              (Press [O] to see the options)\n"))
    sleep(2)
    if get_length(next_task):
        match next_task:
            case "O":
                # Show OPTIONS
                # Call show_task_options function
                show_task_options()
                next_task = what_task(phrase, list, scheduler)
            case "S":
                print("\n You have selected \"SCREW arms on\". \n")
                # Status becomes 1
                return 1
            case "W":
                print("\n You have selected \"WELD legs on\". \n")
                # Status becomes 2
                return 2
            case "H":
                print("\n You have selected \"HAMMER the head on\". \n")
                # Status becomes 3
                return 3
            case "P":
                print("\n You have selected \"POLISH the eyes\". \n")
                # Status becomes 4
                return 4
            case "D":
                print("\n You have selected \"DRILL the ears\". \n")
                # Status becomes 5
                return 5
            case "A":
                print("\n You have selected \"ATTACH the waste hose\". \n")
                # Status becomes 6
                return 6
            case "T":
                print("\n You have selected \"TEST the functioning\". \n")
                # Status becomes 7
                return 7
            case "U":
                print("\n You have selected \"UNLOAD trucks with forklift\". \n")
                # Status becomes8
                return 8
            case "B":
                print("\n You have selected \"BOX & ship product\". \n")
                # Status becomes 9
                return 9
            case "F":
                print("\n You have selected \"FETCH cups of tea\". \n")
                # Status becomes 10
                return 10
            case "X":
                # Exit from task options
                print("\n Selecting this will return you to the main menu. \n")
                sleep(6)
                what_next()
            case _:
                # wildcard case to catch bad inputs
                print("\n Instruction not recognised. \n")
                sleep(4)
                next_task = what_task(phrase, list, scheduler)
    else:
        next_task = what_task(phrase, list, scheduler)

# Helper function to show options for assigning tasks
def show_task_options():
    sleep(2)

    print(('\n These are the options for the tasks: \n'
           '\n Press [S] for SCREWing arms on          \n' # Status = 1
           '\n Press [W] for WELDing legs on           \n' # Status = 2
           '\n Press [H] for HAMMERing heads on        \n' # Status = 3
           '\n Press [P] = POLISH the eyes             \n' # Status = 4
           '\n Press [D] = DRILL the ears              \n' # Status = 5
           '\n Press [A] = ATTACH the waste hose       \n' # Status = 6
           '\n Press [T] = TEST the functioning        \n' # Status = 7
           '\n Press [U] for UNLOADing trucks          \n' # Status = 8
           '\n Press [B] for BOX and ship the product  \n' # Status = 9
           '\n Press [F] for FETCH cups of tea         \n' # Status = 10
           '\n Press [X] to Exit this menu             \n'
           ))
    return

# Function to return a quantity (of workers or robots)
def how_many_labourers(phrase="worker", phrase_2="do you want", max=2):
    while True:
        while not l:
            l = input(f"\n\n How many {phrase}s {phrase_2}? \n\n Please choose a number between 1 and {max}. \n")
            sleep(3)
            if not l:
                print("\n Was I meant to take that as an answer? \n")
                continue
        try:
            l = int(l)
            if l > max:
                print("\n I thought I told you what the maximum amount was... ? \n")
                continue
            elif l < 1:
                print(f"\n That is NOT between 1 and {max}. \n")
            else:
                return l
        except ValueError:
            print("\n Sorry, but that isn't a valid response. \n")
            print("\n Maybe you entered letters or symbols instead of just a number. \n")


# Function to ask user whether they want to
#  change status of robots or workers
#   from finished to idle
def ask_finished_to_idle(x_dict, phrase="worker"):
    sleep(1)
    while True:
        finished = 0
        j = len(x_dict)
        for i in j:
            if x_dict[phrase + "_" + str(i - 1)]  == 11:
                finished += 1
        if finished == 1:
                reassign = input(f"Would you like to make the {phrase} "
                            "that has finished its task available for more work? (Y/N) \n")
                if get_length(reassign):
                    match reassign:
                        case "Y":
                            switch_range = len(x_dict)
                            for switch in switch_range:
                                if x_dict[phrase + "_" + i] == 0:
                                    x_dict[phrase + "_" + i] = 11
                                    return x_dict
                        case "N":
                            print("\nStop wasting time then!! \n")
                            return x_dict
                        case _:
                            pass
        elif finished > 1 :
            reassign = input(f"Would you like to make any of the {phrase}s that " 
                        "have finished their tasks available for more work? (Y/N)\n")
            if get_length(reassign):
                match reassign:
                    case "Y":
                        # Find out how many to robots or humans to transfer
                        phrase_2 = ("How many " + phrase + "s would you like to switch \n"
                                   "from FINISHED to IDLE ? \n")
                        x = how_many_labourers(phrase, phrase_2, finished)
                        # Change x number of robots or workers in list from
                        #  status 0 (IDLE) to status 11 (FINISHED)
                        while x:
                                for i in range(0, x):
                                    if x_dict[phrase + "_" + i] == 0:
                                        x_dict[phrase + "_" + i] = 11
                                        x -= 1
                        return x_dict
                    case "N":
                        print("\n Selecting this will return you to the main menu. \n")
                        sleep(6)
                        pass
                    case _:
                        print(('\n An error seems to have occurred \n'
                              'but it\'s nothing to worry about. \n\n'
                              ' We can always build new factories / robots / people / supervisors... \n\n'))
                        sleep(10)
                        what_next()


# Function to add robot
# Accessed by pressing A within what_next() function
# Adds an IDLE robot (0 status code)
def add_robot(n):
    clear_screen()
    print("\n You have selected \"ADD a robot\" \n")
    sleep(1.5)
    robot_dict[n] = 0
    n += 1
    print("\n You have added an extra 'bot to the crew. \n"
          "Press C to CHANGE their status and get them mechanised !\n")
    return n

# Function to remove robot.
# Accessed by pressing R within what_next() function
def remove_robot(n):
    clear_screen()
    print("\n You have selected \"REMOVE a robot\" \n")
    sleep(1.5)
    for i in range(n, -1, -1):
        if robot_dict[i] == 0:
            robot_dict.pop(i)
            n -= 1
            print("\n You have sent a robot to the recycling plant ! \n\n")
            return n
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
    clear_screen()
    print("\n You have selected \"CHANGE a robot's status\" \n")
    sleep(3)
    print("\n          You will now be shown all the many robots you have to choose from: \n\n")
    sleep(3)
    dict_printer(robot_dict)
    sleep(2)
    pass


# Function to assign task to robot
# Accessed by pressing P within what_next() function
def program_robot(n, status_tuple):
    clear_screen()
    print("\n You have selected \"PROGRAM a robot to execute a task\" \n")
    sleep(3)

    # Check if any robots are IDLE
    if not robot_dict.count(0) and robot_dict.count(11):
        print(" but you have no IDLE robots to execute your programs.\n")
        # Suggest user switches some statuses from FINISHED to IDLE
        ask_finished_to_idle("droid", robot_dict)
    elif not robot_dict.count(0) and not robot_dict.count(11):
        print(" but you have no IDLE robots to execute further programs.\n")
        print("\n You will have to switch some from the tasks they're WORKING on \n"
              "or wait til they're FINISHED. \n")
        sleep(5)
        what_next()
    else:
        if robot_dict.count(0) == 1:
            print("\n You have 1 robot IDLE. \n")
            sleep(0.5)
            robot_dict.insert(what_task("robot", robot_dict, scheduler))
            robot_dict.remove(0)
            return
        elif robot_dict.count(0) > 1:
            print(f" You currently have {robot_dict.count(0)} IDLE robots to assign tasks to.\n")
            y = how_many_labourers("robots")
            next_task = what_task("robot", scheduler)
        pass


# Function to employ new worker.
# Accessed by pressing E within what_next() function
# Adds an IDLE human (0 status code)
def employ_worker(m):
    clear_screen()
    print("\n You have selected \"EMPLOY a new worker\" \n")
    human_dict[m] = 0
    m += 1
    print("\n You have hired one more worker. \n"
          " Press M for MANAGE to get them straight to work. \n"
          "\n Before they try'n join the union already ! \n\n")
    return m


# Function to fire a worker.
# Accessed by pressing F within what_next() function
def fire_worker(m):
    clear_screen()
    print("\n You have selected \"FIRE a worker\" \n")
    sleep(1.5)
    for i in range(m, -1, -1 ):
        if human_dict[i] == 0:
            human_dict.pop(i)
            m -= 1
            print("\n Give him his P45 - \n"
                  " and that's one more benefit claimant ! \n\n")
            return m
        else:
            continue
    print(('\n Unable to dismiss a worker while they\'re all carrying out tasks. \n'
           '  Tell the worker you\'re firing to come to your office -            \n'
           ' eg. select M for MANAGE to change a worker\'s status to IDLE,       \n'
           'then you can [come back here and] fire them for being idle!        \n\n'))
    return m

# Function to manage worker
# Accessed by pressing M within what_next() function
# statuses available = idle / working / finished task
def manage_worker():
    clear_screen()
    print("\n You have selected \"MANAGE a worker\" \n")
    sleep(3)
    print("\n          You will now be shown the wide range of skivvies you have to choose from: \n\n")
    sleep(3)
    dict_printer(human_dict)
    sleep(2)
    pass

# Function to order available workers to carry out tasks.
# Accessed by pressing O within what_next() function
def order_worker(m, status_tuple):
    clear_screen()
    print("\n You have selected \"ORDER worker to task\" \n")
    sleep(1.5)
    if not human_dict.count(0) and human_dict.count(11):
        print(" but you have no IDLE lackeys to boss around.\n")
        ask_finished_to_idle("human", human_dict)
        return
    elif not human_dict.count(0) and not human_dict.count(11):
        print(" but you have no IDLE lackeys to boss around.\n")
        print("\n You will have to switch some from the tasks they're WORKING on, \n"
              "pressing M for MANAGE from the main menu \n"
              "or wait til they've FINISHED what they're doing. \n")
        return
    elif human_dict.count(0) == 1:
        print(f" You only have 1 IDLE human to assign a task to.\n")
        sleep(0.5)
        human_dict.insert(what_task("human", human_dict, scheduler))
        human_dict.remove(0)
        return
    elif human_dict.count(0) > 1:
        print(f" You currently have {human_dict.count(0)} IDLE humans to assign tasks to.\n")
        z = how_many_labourers("humans")
        next_task = what_task("human", scheduler)


# Log tasks
# Accessed by pressing L within what_next() function
# Classify tasks as not started / in progress / completed
def log_tasks(task_log):
    clear_screen()
    print("\n You have selected \"LOG tasks\" ", end="")
    sleep(5)

    # Task log screen display

    print('\r                      ------------                          ')
    print((f'======================| TASK LOG |===========================\n'
           '|                   ------------                          |\n'
           '|                                                         |\n'
           '|               -- FINISHED tasks --                      |\n'
           '|                                                         |\n'
           '|   # of arms SCREWED on (pairs)  --> -> -->              |\n'
           '|                                                         |\n'
           '|   # of legs WELDED on  (pairs)  --> -> -->              |\n'
           '|                                                         |\n'
           '|   # of heads HAMMERed on --> -> --> -> -->              |\n'
           '|                                                         |\n'
           '|   # of (pairs of) eyes POLISHed --> -> -->              |\n'
           '|                                                         |\n'
           '|   # of (pairs of) ears DRILLed --> -> --->              |\n'
           '|                                                         |\n'
           '|   # of waste hoses ATTACHed --> --> -> -->              |\n'
           '|                                                         |\n'
           '|   # of quality control TESTs completed -->              |\n'
           '|                                                         |\n'
           '|   # of trucks UNLOADed --> -> -> -> -> -->              |\n'
           '|                                                         |\n'
           '|   # of BOXes shipped   --> -> -> -> -> -->              |\n'
           '|                                                         |\n'
           '|   # of cups of tea FETCHed (100\'s) -> -->               |\n'
           '|                                                         |\n'
           '===========================================================\n'
           ))
    pass


# Function to track progress of robots, workers and tasks
# Accessed by pressing T within what_next() function
# Should regularly update status and identify problems
# eg. Idle robots, idle workers, incomplete tasks.
def track_progress(scheduler):
    clear_screen()
    print("\n You have selected \"TRACK progress\" \n")
    sleep(2)
    pass

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
    sleep(3)
    print((
           " At least once an hour someone is also required to stand on the balcony above the factory floor and "
           "shout at everyone to work faster. \n"
           " That particular job cannot be delegated. \n"))
    sleep(3)
    input("\nPress Enter to continue... ")
    clear_screen()
    print(' From the main menu, the options you can select are detailed below:\n')
    sleep(3)
    print(('\n\n Press [A] to add extra robots to the workforce :-       \n'
           '\n            - don\'t fret about having the money for them, \n'
           '                or whether you\'ve built enough;             \n'
           '                let\'s just say,                             \n'
           '                 "Here\'s one I prepared earlier"            \n'
           ))
    sleep(5)
    print(('\n\n Press [R] to remove robots from the workforce :-        \n'
           '              - you can always replace them later.           \n'
           '\n               Uh,why are these instructions sounding      \n'
           '                so creepy?!                                  \n'
           ))
    sleep(5)
    print(('\n\n Press [C] to change the status of a robot.              \n'
           '\n            - In the beginning they will all be [IDLE]     \n'
           '\n            - You can change their status to [WORKING],    \n'
           ))
    sleep(5)
    print(('\n\n Press [P] to program a robot: \n'
           '\n            - that translates to giving it a task to do.   \n'
           '\n            - You choose from the varied tasks carried out \n'
           '\n                                   at                      \n'
           '\n                           Ro-Ro-Ro-Your-Bots\u00AE        \n'
         ))
    sleep(5)
    print(('\n\n Press [E] to employ (human) workers:                    \n'
           '\n            - This allows you to grow your workforce.      \n'
           '\n            - Humans work out more costly than robots,     \n'
           '               but never yet have I come across a machine    \n'
           '               that can make a decent cup of tea !           \n'
           ))
    sleep(5)
    print(('\n\n Press [F] to fire (human) workers:                      \n'
           '\n            - If you\'ve got more staff than you need      \n'
           '               don\'t feel bad about laying some off:-       \n'
           '                People are just too expensive to maintain    \n'
           '               These days.                                   \n'
           ))
    sleep(5)
    print(('\n\n Press [M] to manage the status of humans.               \n'
           '              - Just like you change the robots\' statuses.  \n'
           '\n            - The human workers are just the same mostly.  \n'
           '\n              - IDLE, WORKING or FINISHED                  \n'
           ))
    sleep(5)
    print(('\n\n Press [O] to order humans to perform tasks.             \n'
           '\n            - It\'s the same as programming them.          \n'
           ))
    sleep(5)
    print(('\n\n Press [L] to log tasks as not started, in progress      \n'
           '                                          or completed.      \n'
           '\n   - For each task you can see how many occurrences of it  \n'
           '      remain to be started, how many are in progress and     \n'
           '      how many have been completed.                          \n'
           '\n     You will have the option of giving tasks new states   \n'
           '      of completion.                                         \n'
           ))
    pass
    sleep(5)
    print(('\n\n Press [T] to track the progress of workers and robots.  \n'))
    pass
    sleep(5)
    print('\n\n Press [H] when you want to see these helpful tips again. \n')
    sleep(5)
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
            sleep(5)
            quit = input("\n Are you sure you don't want to quit? (Y/N) \n").upper()
            if get_length(quit):
                if quit == "Y":
                    input("\n This is getting confusing,"
                      "so shall we say No just to be on the safe side?\n").upper()
                if quit == "N":
                    input("\n No, you're not sure you don't want to quit,"
                          "or No, you don't want to quit? \n").upper()
                what_next()
            else:
                print("\n I didn't catch that. Let's take it from the top.\n")
                sleep(5)
                what_next()
    else:
        quit_program()


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