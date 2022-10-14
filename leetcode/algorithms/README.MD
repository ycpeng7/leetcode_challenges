# Summary and Patterns


## 14 Leetcode patterns
### Sliding Window
Perform a required operation on a specific window size of a given array or linked list.
Move one at a time, window size can grow, shrink, or stay the same.

When:
  1. Longest or shortest substring
  2. Subarray of a certain value
  3. If the problem input is linear, such as linked list, array or string, it's likely to be sliding window.

Example:
  1. Maximum sum subarray of size K
  2. Longest substring with K distinct characters
  3. String anagrams 

### Two pointers or iterators
Two pointers iterate through the data structure until one or both hit a certain condition.

When:
  1. Often usedful for **sorted** array or linked list.

Example:
  1. Squaring a sorted array
  2. Triplets that sum to zero
  3. Compairing strings that contain backspaces

### Fast and slow pointers
Two pointers that move through the array/linked list at different speeds. Useful in dealing with
cyclic ones. 

When:
  1. Cyclic array/linked list
  2. Need to know the position of a certain element or the overall length of the linked list

Example:
  1. Linked List Cycle
  2. Palindrome Linked List
  3. Cycle in a Circular Array

### Merge Intervals
Deal with overlapping intervals. Given two intervals, a and b, there will
be 5 different ways the two intervals can related to each outher
  1. a and b do not overlap
  2. a and b overlap, b ends after a
  3. a completely overlaps(includes) b
  4. a and b overlap, a ends after b
  5. b completely overlaps(includes) a

When:
  1. Produce a list with only mutually exclusive intervals
  2. "Overlapping intervals"

Example:
  1. Intervals intersection
  2. Maximum CPU load

### Cyclic sort


## Greedy Method
Usually given an array, a1, a2, ... an.
for i = 1 to n:
    x = select(a) , x here is a solution
    if x is feasible solution:
        solution_set = solution_set + x
        
Greedy problems usually look like "Find minimum number of something to do something" or "Find maximum number of something to fit in some conditions", and typically propose an unsorted input.

The idea of greedy algorithm is to pick the locally optimal move at each step, that will lead to the globally optimal solution.

The standard solution has \mathcal{O}(N \log N)O(NlogN) time complexity and consists of two parts:

Figure out how to sort the input data (\mathcal{O}(N \log N)O(NlogN) time). That could be done directly by a sorting or indirectly by a heap usage. Typically sort is better than the heap usage because of gain in space.

Parse the sorted input to have a solution (\mathcal{O}(N)O(N) time).


## Backtracking

Code template:

def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
            

## Dynamic Programming

[Great post for Leetcode patterns](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)

### Memoization
First, populate the list memo[] with a value that can never be a solution (value like -1 depending on problems).
For every iteration, check if memo[i] == -1, if so, solve it.

