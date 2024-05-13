""" 
    Created on Thu Sept 17 2020

    @author: umairkarel
"""

import time
from constants import MAX_SIZE


############# Bubble Sort #############
def bubble_sort(data, draw_data, time_tick):
    """
    Sorts the given data using the Bubble Sort algorithm.

    Parameters:
        data (list): The list of elements to be sorted.
        draw_data (function): A function that takes a list of elements and returns None.
        This function is used to draw the data on a visualization.
        time_tick (float): The time delay between each iteration of the algorithm.

    Returns:
        None
    """
    for _ in range(len(data) - 1):
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                draw_data(
                    data,
                    [
                        "lightgreen" if x == i or x == i + 1 else "#3b4249"
                        for x in range(len(data))
                    ],
                )
                time.sleep(time_tick)
    draw_data(data, ["green" for x in range(len(data))])


############# Insertion Sort #############
def insertion_sort(data, draw_data, time_tick):
    """
    Sorts the given data using the Insertion Sort algorithm.

    Parameters:
        data (list): The list of elements to be sorted.
        draw_data (function): A function that takes a list of elements and returns None.
        This function is used to draw the data on a visualization.
        time_tick (float): The time delay between each iteration of the algorithm.

    Returns:
        None
    """
    for i in range(1, len(data)):
        value = data[i]
        j = i
        while value <= data[j - 1] and j != 0:
            draw_data(
                data, ["lightgreen" if x == j else "#3b4249" for x in range(len(data))]
            )
            time.sleep(time_tick)

            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1

        draw_data(
            data, ["lightgreen" if x == j else "#3b4249" for x in range(len(data))]
        )
        time.sleep(time_tick)
    draw_data(data, ["green" for x in range(len(data))])


############# Selection Sort #############
def selection_sort(data, draw_data, time_tick):
    """
    Sorts the given data using the Selection Sort algorithm.

    Parameters:
        data (list): The list of elements to be sorted.
        draw_data (function): A function that takes a list of elements and returns None.
        This function is used to draw the data on a visualization.
        time_tick (float): The time delay between each iteration of the algorithm.

    Returns:
        None
    """
    for i in range(len(data) - 1):
        pos = i
        last = MAX_SIZE
        for j in range(i + 1, len(data)):
            draw_data(
                data,
                [
                    (
                        "lightyellow"
                        if x == j
                        else ("lightblue" if x == i else "#3b4249")
                    )
                    for x in range(len(data))
                ],
            )
            time.sleep(time_tick)

            if data[j] < data[i] and data[j] < last:
                pos = j
                last = data[j]

        draw_data(
            data,
            [
                ("lightgreen" if x == pos else ("lightblue" if x == i else "#3b4249"))
                for x in range(len(data))
            ],
        )
        time.sleep(time_tick)
        temp = data[i]
        data[i] = data[pos]
        data[pos] = temp

    draw_data(data, ["green" for x in range(len(data))])


############# Merge Sort #############
def merge_sort(data, draw_data, time_tick):
    """
    Sorts the given data using the Merge Sort algorithm.

    Parameters:
        data (list): The list of elements to be sorted.
        draw_data (function): A function that takes a list of elements and returns None.
        This function is used to draw the data on a visualization.
        time_tick (float): The time delay between each iteration of the algorithm.

    Returns:
        None
    """
    merge_sort_alg(data, 0, len(data) - 1, draw_data, time_tick)

    draw_data(data, ["green" for x in range(len(data))])
    time.sleep(time_tick)


def merge_sort_alg(data, left, right, draw_data, time_tick):
    """
    Sorts a given list of elements using the merge sort algorithm.

    Parameters:
        data (list): The list of elements to be sorted.
        left (int): The starting index of the sublist to be sorted.
        right (int): The ending index of the sublist to be sorted.
        draw_data (function): A function that takes a list of elements and returns None.
        This function is used to draw the data on a visualization.
        time_tick (float): The time delay between each iteration of the algorithm.

    Returns:
        None
    """
    if left >= right:
        return
    middle = (left + right) // 2

    merge_sort_alg(data, left, middle, draw_data, time_tick)
    merge_sort_alg(data, middle + 1, right, draw_data, time_tick)
    merge(data, left, middle, right, draw_data, time_tick)


def merge(data, left, middle, right, draw_data, time_tick):
    """
    Merges two subarrays of data[].

    Parameters:
        data (list): The list to be sorted.
        left (int): Index of the leftmost element.
        middle (int): Index of the middle element.
        right (int): Index of the rightmost element.
        draw_data (function): A function to draw the data on a visualization.
        time_tick (float): The time delay between iterations.

    Returns:
        None
    """
    draw_data(data, ["#3b4249" for x in range(len(data))])
    time.sleep(time_tick)

    left_part = data[left : middle + 1]
    right_part = data[middle + 1 : right + 1]

    left_idx, right_idx = 0, 0

    for i in range(left, right + 1):
        if left_idx < len(left_part) and right_idx < len(right_part):
            if left_part[left_idx] <= right_part[right_idx]:
                data[i] = left_part[left_idx]
                left_idx += 1
            else:
                data[i] = right_part[right_idx]
                right_idx += 1
        elif left_idx < len(left_part):
            data[i] = left_part[left_idx]
            left_idx += 1
        else:
            data[i] = right_part[right_idx]
            right_idx += 1

        draw_data(
            data, ["lightblue" if x == i else "#3b4249" for x in range(len(data))]
        )
        time.sleep(time_tick)


############# Quick Sort #############

colordata = []


def partition(data, low, high, draw_data, time_tick):
    """
    Partitions the given data array into two subarrays based on a pivot element.

    Args:
        data (list): The list to be partitioned.
        low (int): The starting index of the partition.
        high (int): The ending index of the partition.
        draw_data (function): A function to draw the data on a visualization.
        time_tick (float): The time delay between iterations.

    Returns:
        int: The index of the pivot element after partitioning.
    """
    i = low - 1
    pivot = data[high]
    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]

        colordata[:] = [
            "#3b4249" if x not in (i, high) else ("#ff0000" if x == i else "lightblue")
            for x in range(len(colordata))
        ]

        draw_data(data, colordata)
        time.sleep(time_tick)

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


def quick_sort_algo(data, low, high, draw_data, time_tick):
    """
    Sorts a given list of elements using the Quick Sort algorithm.

    Parameters:
        data (list): The list of elements to be sorted.
        low (int): The starting index of the sublist to be sorted.
        high (int): The ending index of the sublist to be sorted.
        draw_data (function): A function to draw the data on a visualization.
        time_tick (float): The time delay between iterations.

    Returns:
        None
    """
    if low < high:
        pi = partition(data, low, high, draw_data, time_tick)
        quick_sort_algo(data, low, pi - 1, draw_data, time_tick)
        quick_sort_algo(data, pi + 1, high, draw_data, time_tick)


def quick_sort(data, draw_data, time_tick):
    """
    Sorts the given data using the Quick Sort algorithm.

    Parameters:
        data (list): The list of elements to be sorted.
        draw_data (function): A function that takes a list of elements and returns None.
            This function is used to draw the data on a visualization.
        time_tick (float): The time delay between each iteration of the algorithm.

    Returns:
        None
    """
    # pylint: disable=global-statement
    global colordata

    colordata = ["#3b4249" for x in range(len(data))]
    quick_sort_algo(data, 0, len(data) - 1, draw_data, time_tick)
    draw_data(data, ["green" for x in range(len(data))])


############# Heap Sort #############

colordata = []


def heapify(data, n, i, draw_data, time_tick):
    """
    Recursively heapifies the given array based on the provided index and heap size.

    Parameters:
        data (list): The array to be heapified.
        n (int): The size of the heap.
        i (int): The index to start heapifying from.
        draw_data (function): A function to draw the data on a visualization.
        time_tick (float): The time delay between iterations.

    Returns:
        None
    """
    largest = i
    l = 2 * i
    r = 2 * i + 1

    if l < n and data[largest] < data[l]:
        largest = l

    if r < n and data[largest] < data[r]:
        largest = r

    if largest != i:
        data[i], data[largest] = data[largest], data[i]

        draw_data(
            data,
            [
                "lightblue" if x == i or x == largest else colordata[x]
                for x in range(len(data))
            ],
        )
        time.sleep(time_tick)

        heapify(data, n, largest, draw_data, time_tick)


def heap_sort(data, draw_data, time_tick):
    """
    Sorts the given data using the Heap Sort algorithm.

    Parameters:
        data (list): The list of elements to be sorted.
        draw_data (function): A function that takes a list of elements and returns None.
        This function is used to draw the data on a visualization.
        time_tick (float): The time delay between each iteration of the algorithm.

    Returns:
        None
    """
    # pylint: disable=global-statement
    global colordata

    colordata = ["#3b4249" for x in range(len(data))]

    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, draw_data, time_tick)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]

        draw_data(
            data,
            [
                "lightyellow" if x == i or x == 0 else colordata[x]
                for x in range(len(data))
            ],
        )
        time.sleep(time_tick)
        # colordata[i] = 'green'

        heapify(data, i, 0, draw_data, time_tick)

    draw_data(data, ["green" for x in range(len(data))])
