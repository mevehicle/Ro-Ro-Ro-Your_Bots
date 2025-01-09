total_time = 23525

# ----------------------------------------------------- Task codes are:
task_log = [(("IDLE     ", "IDLE                          "),  # --> 00
             ("SCREWing ", "SCREWing arms on              "),  # --> 01
             ("WELDing  ", "WELDing legs on               "),  # --> 02
             ("HAMMERing", "HAMMERing heads on            "),  # --> 03
             ("POLISHing", "POLISHing eyes                "),  # --> 04
             ("DRILLing ", "DRILLing ears                 "),  # --> 05
             ("ATTACHing", "ATTACHing waste hoses         "),  # --> 06
             ("TESTing  ", "TESTing the functioning       "),  # --> 07
             ("UNLOADing", "UNLOADing trucks with forklift"),  # --> 08
             ("BOXing   ", "BOXing and shipping product   "),  # --> 09
             ("FETCHing ", "FETCHing cups of tea          "),  # --> 10
             ("FINISHED ", "FINISHED_TASK                 "))]  # --> 11

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
    task_log[5][i] = {
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
                 [task_log[0][10][1], 0],
                 [task_log[0][11][1], 0]])

################################################################################## Helper function to print out data in columns:
def column_printer(data, column):
    for row in range(9, 28, 2):
        print(f"\u001b[{row};{column}H{data}", end="")


print((f'                                              ----------------                                            \n'
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
############################

print(task_log[3])