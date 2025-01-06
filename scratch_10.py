# ------------------------------------------------------------ Task codes are:
def show_log():
    task_tuple = (("IDLE     ", "IDLE                          "), #--> 00
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
                  ("FINISHED ", "FINISHED_TASK                 ")) #--> 11

    # -------------------the Task Log ----------------------------

    # task_log is a multi-dimensional list showing, for each task,
    # how many repetitions of that task have been completed
    # and whether any workers or robots are currently engaged in it
    #  It contains:
    #  - - - - - [0] = a dictionary of twelve keys, one for each task code:
    #  - - - - -    each value denotes how many robots are engaged in the task
    #               (or engaged in the IDLE-ness, for task codes 0 & 11
    #  - - - - - [1] = another dictionary, a mirror of it where
    #  - - - - -    each value denotes how many humans are engaged in the task

    task_log = []
    for i in range(0, 2):
        task_log.append({})
        for j in range(0, 12):
            task_log[i][j] = 0

    # Task log also contains:
    #  - - - - - [2] = a dictionary of 12 lists,
    #  - - - - - - - -  each list holding the IDs of the
    #  - - - - - - -  individual robots engaged in each task
    #  - - - - - [3] = another dictionary of 12 lists, each holding
    #  - - - - - - -  **SURPRISE**: the IDs of the humans
    #  - - - - - - - - - - - - - - - engaged in that task

    for i in range(2, 4):
        task_log.append({})
        for j in range(0, 12):
            task_log[i][j] = []

    #  - - - - - [4] = a dictionary of twelve keys, one for each task code:
    #  - - - - -    each value holds its own dictionary, this time of
    #  - - - - -    three keys, the values being:
    #  - - - - -    number of tasks not started / in progress / completed

    task_log.append({})
    task_log[4] = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    for i in range(0, 12):
        task_log[4][i] =  {
                           "NOT STARTED": 0,
                           "IN PROGRESS": 0,
                           " COMPLETED ": 0,
                          }
    #  - - - - - [5] = a tuple with 12 values, matched to tasks
    #  - - - - -    containing the amount of time needed to perform it.
    #  - - - - -     As "tasks" 0 and 11 actually represent IDLE
    #  - - - - -    and finished respectively, their value is zero

    task_log.append((("IDLE     ", 0),
                     ("SCREWing ", 3),
                     ("WELDing  ", 3),
                     ("HAMMERing", 3),
                     ("POLISHing", 2),
                     ("DRILLing ", 2),
                     ("ATTACHing", 2),
                     ("TESTing  ", 2),
                     ("UNLOADing", 10),
                     ("BOXing   ", 1),
                     ("FETCHing ", 1),
                     ("FINISHED ", 0)))

    #  - - - - - [6] = finally another 12 values paired to tasks,
    #  - - - - -    showing how many repetitions of that task are
    #  - - - - -    needed to fulfil Head Office's directives

    task_log.append((("IDLE     ", 0),
                     ("SCREWing ", 10),
                     ("WELDing  ", 10),
                     ("HAMMERing", 10),
                     ("POLISHing", 10),
                     ("DRILLing ", 10),
                     ("ATTACHing", 10),
                     ("TESTing  ", 5),
                     ("UNLOADing", 1),
                     ("BOXing   ", 5),
                     ("FETCHing ", 50),
                     ("FINISHED ", 0)))

    #########################################################################################################
    # Clear screen using ANSI escape sequence
    print("\u001b[2J")
    # Cursor to home using ANSI escape sequence
    print("\u001b[H")
    total_time = 48726
    ##########################################################################################################


    print((f'                                              ------------                                               \n'
           '==============================================| TASK LOG |===============================================\n'
           '| TIME :                       |              ------------                     ||         WORKERS       |\n'
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
           '========================================================================================================|\n'
           ))
    # Use escape codes to send cursor to different screen positions
    #       \u001b[{line};{column}H
    #  OR   \u001b[{line};{column}f
    # Use \r and end="" to prevent new lines being added
    hours = total_time // 3600
    minutes = (total_time // 60) - (hours * 60)

    seconds = total_time - (hours * 3600) - (minutes * 60)
    # Print clock on line 4
    print(f"\u001b[4;12H{str(hours).zfill(2)} / {str(minutes).zfill(2)} / {str(seconds).zfill(2)} ")

    # Print stage of completion for each task : start cursor at 7, 41, eg. \u001b[7;41H
    for i in range (41, 74, 16):
        for j in range (7, 26, 2):
            match i:
                case 41:
                    stage = "NOT STARTED"
                case 57:
                    stage = "IN PROGRESS"
                case 73:
                    stage = " COMPLETED "
                case _:
                    stage = " COMPLETED"
            print(f"\u001b[{j};{i}H{task_log[4][(j-5)//2][stage]}", end="")

    # Print how many robots are working on each task at column 86
    # Print how many humans are working on each task at column 99
    for i in range(86, 100, 13):
            match i:
                case 86:
                    flesh = 0
                case 99:
                    flesh = 1
                case _:
                    flesh = 0
            for j in range(7, 26, 2):
                print(f"\u001b[{j};{i}H{task_log[flesh][(j-5)//2]}", end="")

    print(f"\u001b[38;2H")

show_log()