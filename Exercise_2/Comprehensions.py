'''
1. Generate the list of squares of the numbers from 1 to 10.
2. The same, but only for the odd numbers.
3. Generate the list of prime numbers up to 100 using a comprehension.
4. Build a dictionary mapping each word of a sentence to its length.
For each, write the equivalent explicit loop and compare the two.'''

comp_1 = [
    n**2
    for n in range(1,11)
]
# print(comp_1)
comp_2 = [
    n**2
    for n in range(1,11,2)

]
print(comp_2)

