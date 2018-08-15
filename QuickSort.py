# Function to execute Quick sort algorithm on input list

import numpy as np

def QuickSort(numbers):     # numbers is a list of numbers to be sorted
    quicksort_helper(numbers, 0, len(numbers)-1)

def quicksort_helper(list, first, last):
    if first < last:
        split = partition(list, first, last)
        quicksort_helper(list, first, split - 1)
        quicksort_helper(list, split + 1, last)


def partition(list, first, last):
    pivot = list[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while(left <= right and list[left] <= pivot):
            left = left + 1
        while(list[right] >= pivot and right >= left):
            right = right - 1
        if(right < left):
            done = True
        else:
            temp = list[left]
            list[left] = list[right]
            list[right] = temp

        temp = list[first]
        list[first] = list[right]
        list[right] = temp
        return right

