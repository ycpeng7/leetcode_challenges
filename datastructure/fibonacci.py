# 0, 1, 1, 2, 3, 5, ...

# Recursion

def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

# Memoization: For each n, only runs recursion once, minimizing duplicated calls

def fib_memo(n):
    memo = [-1 for _ in range(n + 1)]
    def fib_recur_memo(i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            if memo[i] != -1:
                return memo[i]
            else:
                return fib_recur(i-1) + fib_recur(i-2)
    return fib_recur_memo(n)
    

# Bottom-up

def fib_bottom_up(n):

    memo = [-1 for _ in range(n+1)]


    for i in range(n+1):
        if i == 0:
            memo[i] = 0
        elif i == 1:
            memo[i] = 1
        else:
            memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

assert fib_recur(0) == 0
assert fib_recur(1) == 1
assert fib_recur(2) == 1
assert fib_recur(4) == 3
assert fib_recur(5) == 5 

assert fib_memo(0) == 0
assert fib_memo(1) == 1
assert fib_memo(2) == 1
assert fib_memo(4) == 3
assert fib_memo(5) == 5 

assert fib_bottom_up(0) == 0
assert fib_bottom_up(1) == 1
assert fib_bottom_up(2) == 1
assert fib_bottom_up(4) == 3
assert fib_bottom_up(5) == 5 