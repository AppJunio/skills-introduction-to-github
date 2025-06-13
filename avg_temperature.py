# Task 1: Create the Data
temperatures = [28, 30, 31, 29, 32, 33, 30]
print(f"Original weekly temperatures: {temperatures}")

# Task 2: Perform Calculations (on the original data)
# We can do this without a function for simplicity, using Python's built-in tools.
# Calculate the sum of all temperatures
total_temperature = sum(temperatures)
# Get the number of days
number_of_days = len(temperatures)
# Calculate the average
average = total_temperature / number_of_days

# Find the highest and lowest temperatures
hottest_day = max(temperatures)
coldest_day = min(temperatures)

# Task 3: Update a Value
# The index for Friday is 4 (since lists start at index 0)
temperatures[4] = 34

# Task 4: Print Everything
print(f"Final (updated) temperatures: {temperatures}")
print(f"Average temperature for the week: {average:.2f}°C") # .2f formats to 2 decimal places
print(f"Highest temperature this week: {hottest_day}°C")
print(f"Lowest temperature this week: {coldest_day}°C")
