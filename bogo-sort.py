import random

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5]
    print("Unsorted array:", arr)
    bogo_sort(arr)
    print("Sorted array:", arr)
