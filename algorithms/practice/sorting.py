# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 10:30:27 2020

@author: joepa
"""


def test(func):
    lis_1 = [9, 8, 1, 5]
    lis_2 = [0]
    lis_3 = []
    lis_4 = [-x for x in range(500)]
    for lis in [lis_1, lis_2, lis_3, lis_4]:
        assert(sorted(lis) == func(lis))


def bubble_sort(lis):
    done = False
    n = len(lis)
    i = -1
    while not done:
        i += 1
        done = True
        for j in range(0, n - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                done = False
    return lis


def selection_sort(lis):
    for i in range(len(lis)):
        minimum = i
        for j in range(i+1, len(lis)):
            if lis[j] < lis[minimum]:
                minimum = j
        lis[i], lis[minimum] = lis[minimum], lis[i]
    return lis


def insertion_sort(lis):
    for i in range(len(lis) - 1):
        ins = i + 1
        while lis[ins] < lis[ins - 1] and ins > 0:
            lis[ins], lis[ins - 1] = lis[ins - 1], lis[ins]
            ins -= 1
    return lis


def merge_sort(lis):
    def merge(left, right):
        merged = [-1 for _ in range(len(left) + len(right))]
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged[i + j] = left[i]
                i += 1
            else:
                merged[i + j] = right[j]
                j += 1
        while i < len(left):
            merged[i + j] = left[i]
            i += 1
        while j < len(right):
            merged[i + j] = right[j]
            j += 1
        return merged

    def sort(lis):
        if len(lis) in [0, 1]:
            return lis
        else:
            mid = len(lis) // 2
            left = sort(lis[:mid])
            right = sort(lis[mid:])
            return merge(left, right)
    return sort(lis)


def quick_sort(lis):
    def partition(lis, start, end):
        pivot = lis[end]
        # j makes sure everything to the left of j is smaller than pivot
        j = start
        for i in range(start, end):
            if lis[i] < pivot:
                lis[j], lis[i] = lis[i], lis[j]
                j += 1
        lis[j], lis[end] = lis[end], lis[j]
        # j is now the index of pivot value
        return j

    def sort(lis, start, end):
        if start < end:
            pivot_ind = partition(lis, start, end)
            sort(lis, start, pivot_ind - 1)
            sort(lis, pivot_ind + 1, end)

    sort(lis, 0, len(lis) - 1)
    return lis


if __name__ == "__main__":
    test(bubble_sort)
    test(selection_sort)
    test(insertion_sort)
    test(merge_sort)
    test(quick_sort)
