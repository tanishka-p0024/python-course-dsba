'''Write a function that returns the 𝑛-th Fibonacci number, 
defined by
𝐹0 = 𝐹1 = 1, 𝐹𝑛 = 𝐹𝑛−1 + 𝐹𝑛−2
so the sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34, …
Print the first ten terms.'''

def fib(n):
    if n == 1 or n==0:
        return 1
    elif n>=2:
        return fib(n-1) + fib(n-2)

# for i in range(10):
#     print(fib(i))

import time
start = time.perf_counter()

result = fib(30)

end = time.perf_counter()

print("Result:", result)
print("Time taken:", end - start, "seconds")



