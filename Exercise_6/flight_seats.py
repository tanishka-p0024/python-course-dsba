'''A plane has 300 seats and 300 passengers, each holding a ticket for 
one seat.The first passenger ignores their ticket and sits at random. 
Every other passenger sits in their own seat if it is free, 
otherwise in a free seat chosen at random.
What is the probability that the last passenger sits in their own seat?
1. Simulate 1000 flights with plain Python and estimate the probability.
2. Vectorize the simulation with numpy. How much faster is it?
3. The exact answer is a simple fraction. Find it, and explain why.'''

import random



def simulate_flight():

     # Representing the 300 seats as lists [0 to 299]
    seats = list(range(300))
    # Passenger 1 -- chooses random seat
        
    random_seat = random.choice(seats)
    seats.remove(random_seat)

    # for next passenger logic:
    # if 1 in seats:
    #     seats.remove(1)
    # else:
    #     new_seat = random.choice(seats)
    #     seats.remove(new_seat)
    success=False
    # passenger 1 - 0th seat,passenger 2 - 1st seat
    for passenger in range(2,301):
        expected_seat = passenger - 1

        if passenger == 300:
            success = expected_seat in seats
        if expected_seat in seats:
            seats.remove(expected_seat)
        else:
            new_seat = random.choice(seats)
            seats.remove(new_seat)

    # Sabkoooooo mil gya seats lol
    return success

success_count = 0
for i in range(1000):
    result = simulate_flight()
    if result == True:
        success_count+=1
print(success_count)

