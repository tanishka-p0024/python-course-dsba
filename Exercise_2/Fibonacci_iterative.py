def fib_iterative(n):
    if n == 0 or n == 1:
        return 1

    previous = 1
    current = 1
    for iteration in range(n-1):
        next = previous + current
        previous = current
        current = next
    return current

# print(fib_iterative(5))


import time
start = time.perf_counter()

result = fib_iterative(30)

end = time.perf_counter()

print("Result:", result)
print("Time taken:", end - start, "seconds")