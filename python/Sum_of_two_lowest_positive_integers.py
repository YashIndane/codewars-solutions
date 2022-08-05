import heapq
def sum_two_smallest_numbers(numbers):
    a = heapq.nsmallest(2 , numbers)
    return sum(a)
