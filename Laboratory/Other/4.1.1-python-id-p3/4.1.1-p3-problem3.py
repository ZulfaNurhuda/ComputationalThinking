""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <System Sabotage>              |
# +----------------------------------------+
# | Simulates system sabotage by           |
# | swapping subprograms.                  |
# +----------------------------------------+

# +--------------------+----------------------+
# | PROGRAM DICTIONARY | DATA TYPE            |
# +--------------------+----------------------+
# | num_subprograms    | integer              |
# | subprograms        | dictionary           |
# +--------------------+----------------------+

def generateSubprogram(message: str):
    """ Description: `[FUNCTION] generateSubprogram` """
    # +------------------------------------------------+
    # | FUNCTION <Generate a subprogram>               |
    # +------------------------------------------------+
    # | Creates and returns a subprogram (closure)     |
    # | that prints a message followed by a variable.  |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | message            | string    |
    # | subprogram         | function  |
    # | variable           | string    |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # DEFINE INNER FUNCTION (CLOSURE) THAT CAPTURES MESSAGE
    def subprogram(variable: str):
        # PRINT MESSAGE FOLLOWED BY VARIABLE VALUE
        print(f"{message} {variable}")
    
    # RETURN THE GENERATED SUBPROGRAM FUNCTION
    return subprogram

def initializeSubprograms():
    """ Description: `[FUNCTION] initializeSubprograms` """
    # +------------------------------------------------+
    # | FUNCTION <Initialize Subprograms>              |
    # +------------------------------------------------+
    # | Creates and initializes all subprograms        |
    # | based on user input.                           |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | num_subprograms    | integer   |
    # | subprograms        | dict      |
    # | name               | string    |
    # | message            | string    |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # GET NUMBER OF SUBPROGRAMS TO CREATE
    num_subprograms: int = int(input("Masukkan jumlah subprogram: "))
    subprograms: dict = {}  # DICTIONARY TO STORE SUBPROGRAM FUNCTIONS

    # LOOP TO CREATE EACH SUBPROGRAM
    for _ in range(num_subprograms):
        name: str = input("Masukkan nama subprogram: ")     # SUBPROGRAM NAME
        message: str = input("Masukkan pesan: ")            # SUBPROGRAM MESSAGE
        # GENERATE AND STORE SUBPROGRAM IN DICTIONARY
        subprograms[name] = generateSubprogram(message)

    print("")
    return subprograms

def performSabotage(subprograms: dict):
    """ Description: `[FUNCTION] performSabotage` """
    # +------------------------------------------------+
    # | FUNCTION <Perform Sabotage>                   |
    # +------------------------------------------------+
    # | Swaps two subprograms in the dictionary        |
    # | if both exist and there are enough programs.   |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | name1              | string    |
    # | name2              | string    |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # VERIFY THAT SWAPPING IS POSSIBLE (AT LEAST 2 SUBPROGRAMS)
    if len(subprograms) > 1:
        name1: str = input("Masukkan nama subprogram pertama: ")
        name2: str = input("Masukkan nama subprogram kedua: ")
        
        # VALIDATE THAT BOTH SUBPROGRAMS EXIST
        if name1 in subprograms and name2 in subprograms:
            # PERFORM SUBPROGRAM SWAP (SABOTAGE)
            subprograms[name1], subprograms[name2] = subprograms[name2], subprograms[name1]
        else:
            # ERROR: ONE OR BOTH SUBPROGRAMS NOT FOUND
            print("Salah satu atau kedua subprogram tidak ditemukan.")
    else:
        # ERROR: INSUFFICIENT SUBPROGRAMS FOR SWAPPING
        print("Hanya terdapat satu subprogram, tidak bisa melakukan swapping.")

def executeSubprogram(command: str, subprograms: dict):
    """ Description: `[FUNCTION] executeSubprogram` """
    # +------------------------------------------------+
    # | FUNCTION <Execute Subprogram>                 |
    # +------------------------------------------------+
    # | Executes a subprogram with user input         |
    # | variable if the subprogram exists.             |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | variable           | string    |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # GET VARIABLE VALUE FROM USER
    variable: str = input("Masukkan nilai variabel: ")
    # EXECUTE THE SUBPROGRAM WITH THE VARIABLE
    subprograms[command](variable)

def processCommand(command: str, subprograms: dict) -> bool:
    """ Description: `[FUNCTION] processCommand` """
    # +------------------------------------------------+
    # | FUNCTION <Process Command>                    |
    # +------------------------------------------------+
    # | Processes user commands and returns whether   |
    # | the program should continue running.           |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | continue_program   | boolean   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # CHECK FOR STOP COMMAND
    if command == "stop":
        return False  # SIGNAL TO STOP THE PROGRAM
    
    # CHECK FOR SABOTAGE COMMAND (SWAP SUBPROGRAMS)
    elif command == "!!!":
        performSabotage(subprograms)
    
    # CHECK IF COMMAND MATCHES AN EXISTING SUBPROGRAM NAME
    elif command in subprograms:
        executeSubprogram(command, subprograms)
    
    # HANDLE UNKNOWN COMMANDS
    else:
        print(f"Subprogram {command} tidak ditemukan.")
    
    return True  # CONTINUE PROGRAM EXECUTION

def runMainLoop(subprograms: dict):
    """ Description: `[FUNCTION] runMainLoop` """
    # +------------------------------------------------+
    # | FUNCTION <Run Main Loop>                      |
    # +------------------------------------------------+
    # | Runs the main command processing loop until   |
    # | user enters stop command.                      |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | command            | string    |
    # | continue_program   | boolean   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # MAIN COMMAND LOOP SECTION
    while True:
        command: str = input("Masukkan perintah: ")  # GET USER COMMAND
        
        # PROCESS COMMAND AND CHECK IF PROGRAM SHOULD CONTINUE
        continue_program: bool = processCommand(command, subprograms)
        
        # EXIT LOOP IF STOP COMMAND WAS ENTERED
        if not continue_program:
            break
        
        print("")  # PRINT EMPTY LINE BETWEEN COMMANDS

""" PROGRAM ALGORITHM """
# MAIN PROGRAM EXECUTION
# INITIALIZATION SECTION: CREATE SUBPROGRAMS
subprograms: dict = initializeSubprograms()

# RUN MAIN COMMAND PROCESSING LOOP
runMainLoop(subprograms)