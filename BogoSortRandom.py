# Function to execute Bogo sort algorithm on input list, using completely random approach, may God have mercy on our souls

#Imports
import numpy as np
import random as random

def BogoSortRandom(numbers):     # numbers is a list of numbers to be sorted
    #Variable Initializations
    listSorted = False

    while listSorted == False:

        #Get Guess
        guess = random.shuffle(numbers)

        #Check Guess
        listSorted = True
        for i in range(len(guess)):
            if guess[i] > guess[i+1]:
                listSorted = False

    sortedNumbers = guess
    return sortedNumbers