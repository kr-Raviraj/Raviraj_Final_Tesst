matrix = [' ' for x in range(10)]


def insertLetter(letter, pos):
    matrix[pos] = letter


def spaceIsFree(pos):
    return matrix[pos] == ' '


def printMatrix(matrix):
    print(matrix[1], matrix[2], matrix[3])
    print(matrix[4], matrix[5], matrix[6])
    print(matrix[7], matrix[8], matrix[9])


def result(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def insertNum():
    run = True
    while run:
        move = input('Choose a position to enter number: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('1', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def computer():
    possibleMoves = [x for x, letter in enumerate(matrix) if letter == ' ' and x != 0]
    move = 0

    for let in ['0', '1']:
        for i in possibleMoves:
            boardCopy = matrix[:]
            boardCopy[i] = let
            if result(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def emptySpace(matrix):
    if matrix.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Game of zeros and One')
    printMatrix(matrix)

    while not (emptySpace(matrix)):
        if not (result(matrix, '0')):
            insertNum()
            printMatrix(matrix)
        else:
            print('No more free space : -1')
            break

        if not (result(matrix, '1')):
            move = computer()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('0', move)
                print('Computer placed an \'0\' in position', move, ':')
                printMatrix(matrix)
        else:
            print('1\'s won this time! Good Job!')
            break

    if emptySpace(matrix):
        print('Tie Game!')


while True:
    answer = input('Do you want to test code (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        matrix = [' ' for x in range(10)]
        main()
    else:
        break

        # matrix = ["-", "-", "-",
        #           "-", "-", "-",
        #           "-", "-", "-"]
        #
        # emty_place = True
        # result = None
        # current_player = "1"
        #
        #
        # def run_matrix():
        #     display_matrix()
        #     while emty_place:
        #         handle_turn(current_player)
        #         check_if_game_over()
        #         flip_player()
        #     if result == "1" or result == "0":
        #         print("-1")
        #     elif result == None:
        #         print("-1")
        #
        #
        # def display_matrix():
        #     print("\n")
        #     print(matrix[0] + " | " + matrix[1] + " | " + matrix[2])
        #     print(matrix[3] + " | " + matrix[4] + " | " + matrix[5])
        #     print(matrix[6] + " | " + matrix[7] + " | " + matrix[8])
        #     print("\n")
        #
        #
        # def handle_turn(player):
        #     print(player + "'s turn.")
        #     position = input("Choose a position to enter number: ")
        #     valid = False
        #     while not valid:
        #         while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        #             position = input("Choose a position to enter your number: ")
        #         position = int(position) - 1
        #
        #         if matrix[position] == "-":
        #             valid = True
        #         else:
        #             print("You can't go there. Go again.")
        #
        #     matrix[position] = player
        #     display_matrix()
        #
        #
        # def check_if_game_over():
        #     check_for_result()
        #     check_for_tie()
        #
        #
        # def check_for_result():
        #     global result
        #     row_winner = check_rows()
        #     column_winner = check_columns()
        #     diagonal_winner = check_diagonals()
        #     if row_winner:
        #         result = row_winner
        #     elif column_winner:
        #         result = column_winner
        #     elif diagonal_winner:
        #         result = diagonal_winner
        #     else:
        #         result = None
        #
        #
        # def check_rows():
        #     global emty_place
        #     row_1 = matrix[0] == matrix[1] == matrix[2] != "-"
        #     row_2 = matrix[3] == matrix[4] == matrix[5] != "-"
        #     row_3 = matrix[6] == matrix[7] == matrix[8] != "-"
        #     if row_1 or row_2 or row_3:
        #         emty_place = False
        #     if row_1:
        #         return matrix[0]
        #     elif row_2:
        #         return matrix[3]
        #     elif row_3:
        #         return matrix[6]
        #     else:
        #         return None
        #
        #
        # def check_columns():
        #     global emty_place
        #     column_1 = matrix[0] == matrix[3] == matrix[6] != "-"
        #     column_2 = matrix[1] == matrix[4] == matrix[7] != "-"
        #     column_3 = matrix[2] == matrix[5] == matrix[8] != "-"
        #     if column_1 or column_2 or column_3:
        #         emty_place = False
        #     if column_1:
        #         return matrix[0]
        #     elif column_2:
        #         return matrix[1]
        #     elif column_3:
        #         return matrix[2]
        #     else:
        #         return None
        #
        #
        # def check_diagonals():
        #     global emty_place
        #     diagonal_1 = matrix[0] == matrix[4] == matrix[8] != "-"
        #     diagonal_2 = matrix[2] == matrix[4] == matrix[6] != "-"
        #     if diagonal_1 or diagonal_2:
        #         emty_place = False
        #     if diagonal_1:
        #         return matrix[0]
        #     elif diagonal_2:
        #         return matrix[2]
        #     else:
        #         return None
        #
        #
        # def check_for_tie():
        #     global emty_place
        #     if "-" not in matrix:
        #         emty_place = False
        #         return True
        #     else:
        #         return False
        #
        #
        # def flip_player():
        #     global current_player
        #     if current_player == "1":
        #         current_player = "0"
        #     elif current_player == "1":
        #         current_player = "0"
        #
        #
        # run_matrix()