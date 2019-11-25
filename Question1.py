# Write a program in python that takes the matrix of 3*3 and allows the user to enter the number like 0 or 1. Make sure if user wants to start first they will fill the random position on matrix with 0 and the next turn would be taken randomly by computer to fill the spot:
# a. No Spot should overlap
# b. Make sure to return (-1) if the matrix if full
#
import random
length = 3
numOnes = 5
while True:
    board = [[(random.random() < float(numOnes)/(length**2))*1 for x in range(length)] for x in range(length)]
    if sum([subarr.count(1) for subarr in board]) == 5:
        break
print(board)
