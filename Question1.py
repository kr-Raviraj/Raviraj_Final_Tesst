#Question:
"""Write a program in python that takes the matrix of 3*3 and allows the user to enter the number like 0 or 1. Make sure if user wants to start first they will fill the random position on matrix with 0 and the next turn would be taken randomly by computer to fill the spot:
a. No Spot should overlap
b. Make sure to return (-1) if the matrix if full
"""

matrix = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

emty_place = True
result = None
current_player = "1"
def run_matrix():
    display_matrix()
    while emty_place:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if result == "1" or result == "0":
        print("-1")
    elif result == None:
        print("-1")

def display_matrix():
    print("\n")
    print(matrix[0] + " | " + matrix[1] + " | " + matrix[2])
    print(matrix[3] + " | " + matrix[4] + " | " + matrix[5])
    print(matrix[6] + " | " + matrix[7] + " | " + matrix[8])
    print("\n")


def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position to enter number: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position to enter your number: ")
        position = int(position) - 1

        if matrix[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    matrix[position] = player
    display_matrix()

def check_if_game_over():
    check_for_result()
    check_for_tie()

def check_for_result():
    global result
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        result = row_winner
    elif column_winner:
        result = column_winner
    elif diagonal_winner:
        result = diagonal_winner
    else:
        result = None



def check_rows():
    global emty_place
    row_1 = matrix[0] == matrix[1] == matrix[2] != "-"
    row_2 = matrix[3] == matrix[4] == matrix[5] != "-"
    row_3 = matrix[6] == matrix[7] == matrix[8] != "-"
    if row_1 or row_2 or row_3:
        emty_place = False
    if row_1:
        return matrix[0]
    elif row_2:
        return matrix[3]
    elif row_3:
        return matrix[6]
    else:
        return None


def check_columns():
    global emty_place
    column_1 = matrix[0] == matrix[3] == matrix[6] != "-"
    column_2 = matrix[1] == matrix[4] == matrix[7] != "-"
    column_3 = matrix[2] == matrix[5] == matrix[8] != "-"
    if column_1 or column_2 or column_3:
        emty_place = False
    if column_1:
        return matrix[0]
    elif column_2:
        return matrix[1]
    elif column_3:
        return matrix[2]
    else:
        return None



def check_diagonals():
    global emty_place
    diagonal_1 = matrix[0] == matrix[4] == matrix[8] != "-"
    diagonal_2 = matrix[2] == matrix[4] == matrix[6] != "-"
    if diagonal_1 or diagonal_2:
        emty_place = False
    if diagonal_1:
        return matrix[0]
    elif diagonal_2:
        return matrix[2]
    else:
        return None



def check_for_tie():
    global emty_place
    if "-" not in matrix:
        emty_place = False
        return True
    else:
        return False

def flip_player():
    global current_player
    if current_player == "1":
        current_player = "0"
    elif current_player == "1":
        current_player = "0"


run_matrix()