'''Write a program that reads the cost of a restaurant meal excluding 
taxes. The program computes the VAT (10 %for a meal served in a
restaurant in France), then asks how much tip 
to add as a percentage of the pre-tax cost.
Finally it prints the total, with the three lines that make it up'''

a = float(input('Cost excluding Taxes'))
vat = 0.1*a
print(f'The VAT for the {a}€ is {vat:.2f}')

total = a + vat
print(f'Your total is {total:.2f}')