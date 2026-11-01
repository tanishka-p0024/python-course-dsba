
import numpy as np

# Simulation settings
n_flights = 1000
n_seats = 300

# Create 1000 flights, each containing 300 seats
seats = np.tile(np.arange(n_seats), (n_flights, 1))

# Passenger 1 randomly selects a seat in each flight
rows = np.arange(n_flights)
random_seats = np.random.randint(0, 300, size=n_flights)

# Mark passenger 1's seats as occupied
seats[rows, random_seats] = -1

# Simulate passengers 2 through 299
for passenger in range(2, 300):

    expected_seat = passenger - 1

    # Check whether assigned seats are available
    assigned_available = seats[:, expected_seat] != -1

    # Passengers take their assigned seats when available
    seats[assigned_available, expected_seat] = -1

    # Find flights where assigned seats are occupied
    unavailable_rows = np.where(~assigned_available)[0]

    # Randomly select an available seat in those flights
    if len(unavailable_rows) > 0:

        available_seats = seats[unavailable_rows] != -1

        random_scores = np.random.random(available_seats.shape)

        # Exclude occupied seats
        random_scores[~available_seats] = -1

        # Select one random available seat per flight
        random_choices = np.argmax(random_scores, axis=1)

        # Mark randomly selected seats as occupied
        seats[unavailable_rows, random_choices] = -1


# Check whether passenger 300's assigned seat is still available
success = seats[:, 299] != -1

# Calculate probability
success_count = np.sum(success)
probability = success_count / n_flights

print("Successful flights:", success_count)
print("Estimated probability:", probability)

