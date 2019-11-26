#Question:
"""Write a program in python that takes the matrix of 3*3 and allows the user to enter the number like 0 or 1. Make sure if user wants to start first they will fill the random position on matrix with 0 and the next turn would be taken randomly by computer to fill the spot:
a. No Spot should overlap
b. Make sure to return (-1) if the matrix if full
"""
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