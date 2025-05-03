def fib(n):
    if isinstance(n, int):
        return fib_aux(n)
    else: return "ERROR"

def fib_aux(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib_aux (n -1) + fib_aux(n - 2)
