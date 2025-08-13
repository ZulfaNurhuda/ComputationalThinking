""" PROGRAM DESCRIPTION """
# +------------------------------------------+
# | PROGRAM <Rock-Paper-Scissors Tournament> |
# +------------------------------------------+
# | DETERMINES THE WINNER OF THE             |
# | ROCK-PAPER-SCISSORS TOURNAMENT.          |
# +------------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | choices            | string    |
# +--------------------+-----------+

def winner(p1: int, p2: int, choice1: str, choice2: str) -> int:
    """ Description: `[FUNCTION] winner` """
    # +-------------------------------------------------+
    # | FUNCTION <Determine Match Winner>               |
    # +-------------------------------------------------+
    # | ACCEPTS 4 PARAMETERS: INTEGER PLAYER 1'S SERIAL |
    # | NUMBER, INTEGER PLAYER 2'S SERIAL NUMBER,       |
    # | STRING PLAYER 1'S CHOICE, AND STRING PLAYER 2'S |
    # | CHOICE. THIS SUBPROGRAM WILL RETURN THE WINNER  |
    # | OF THE ROCK-PAPER-SCISSORS MATCH ACCORDING TO   |
    # | THE EXISTING GAME RULES.                        |
    # +-------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | p1                 | integer   |
    # | p2                 | integer   |
    # | choice1            | string    |
    # | choice2            | string    |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # IF CHOICES ARE THE SAME, THE PLAYER WITH THE LOWER SERIAL NUMBER WINS.
    if choice1 == choice2:
        return p1 if p1 < p2 else p2
    # CHECK FOR PLAYER 1'S WINNING CONDITIONS.
    elif (choice1 == 'G' and choice2 == 'K') or (choice1 == 'B' and choice2 == 'G') or (choice1 == 'K' and choice2 == 'B'):
        return p1
    # OTHERWISE, PLAYER 2 WINS.
    else:
        return p2

def tournamentWinner(choices: str) -> None:
    """ Description: `[PROCEDURE] tournamentWinner` """
    # +-------------------------------------------------+
    # | PROCEDURE <Determine Tournament Champion>       |
    # +-------------------------------------------------+
    # | ACCEPTS A STRING OF 8 CHARACTERS, WHERE EACH    |
    # | CHARACTER IS 'G', 'B', OR 'K', REPRESENTING THE |
    # | CHOICE OF EACH PARTICIPANT, STARTING FROM THE   |
    # | 1ST TO THE 8TH PARTICIPANT, AND PRINTS THE      |
    # | WINNER OF THE ROCK-PAPER-SCISSORS TOURNAMENT.   |
    # +-------------------------------------------------+

    # +--------------------+----------------------+
    # | LOCAL DICTIONARY   | DATA TYPE            |
    # +--------------------+----------------------+
    # | choices            | string               |
    # | participants       | list of integer      |
    # | participant_choices| dictionary           |
    # | round_winners      | list of integer      |
    # | i                  | integer              |
    # | p1                 | integer              |
    # | p2                 | integer              |
    # | choice1            | string               |
    # | choice2            | string               |
    # +--------------------+----------------------+

    """ PROCEDURE ALGORITHM """
    # INITIALIZE THE LIST OF PARTICIPANTS.
    participants: list[int] = list(range(1, 9))
    # CREATE A DICTIONARY TO MAP PARTICIPANT NUMBER TO THEIR CHOICE.
    participant_choices: dict[int, str] = {i+1: choices[i] for i in range(8)}

    # LOOP UNTIL ONLY ONE PARTICIPANT REMAINS.
    while len(participants) > 1:
        # LIST TO STORE THE WINNERS OF THE CURRENT ROUND.
        round_winners: list[int] = []
        # PAIR UP PARTICIPANTS FOR MATCHES.
        for i in range(0, len(participants), 2):
            p1: int = participants[i]
            p2: int = participants[i+1]
            choice1: str = participant_choices[p1]
            choice2: str = participant_choices[p2]
            # DETERMINE THE WINNER OF THE MATCH AND ADD TO THE WINNERS LIST.
            round_winners.append(winner(p1, p2, choice1, choice2))
        # THE WINNERS OF THIS ROUND BECOME THE PARTICIPANTS FOR THE NEXT ROUND.
        participants = round_winners

    # PRINT THE TOURNAMENT WINNER.
    print(f"Pemenang turnamen adalah peserta ke-{participants[0]}")

""" PROGRAM ALGORITHM """
# GET THE CHOICES OF ALL 8 PARTICIPANTS FROM THE USER.
user_input: str = input("Masukkan string pilihan peserta: ")

# CLEAN THE INPUT STRING TO REMOVE QUOTES.
choices: str = ""
# REMOVE QUOTES FROM THE INPUT STRING.
for char in user_input:
    if char != '"':
        choices += char

# DETERMINE AND PRINT THE TOURNAMENT WINNER.
tournamentWinner(choices)