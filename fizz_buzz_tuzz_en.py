"""
FizzBuzzTuzz – A Python exercise that extends the classic FizzBuzz with dynamic input,
user validation, and combined counting for divisibility by 3, 5, and 2.

Author: Alessio Fuscà
Year: 2025
"""

while True:
    try:
        # Intro message explaining the program's rules
        print("Welcome to FizzBuzzTuzz! This program asks you to enter two numbers (in ascending order).")
        print("Then it will count how many numbers between them are divisible by 3, 5, and 2.")
        print("Divisible by 3 = Fizz")
        print("Divisible by 5 = Buzz")
        print("Divisible by 2 = Tuzz")
        print("Numbers divisible by multiple values will be combined (e.g., FizzBuzz).")
        print("At the end, you'll see how many numbers matched each rule.")

        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))

        # Make sure the starting number is less than the ending number
        if start >= end:
            print("The starting number must be less than the ending number. Try again.")
        else:
            break  # Input is valid, exit the loop
    except ValueError:
        print("Please enter valid integers only!")

# Dictionary to track how many times each combination occurs
counters = {}
neutral_count = 0  # Counts numbers not divisible by 3, 5, or 2

# Loop through the range and build a label based on divisibility
for number in range(start, end + 1):
    label = ""

    # Dynamically build the label string
    if number % 3 == 0:
        label += "Fizz"
    if number % 5 == 0:
        label += "Buzz"
    if number % 2 == 0:
        label += "Tuzz"

    # Update the dictionary count, or increase neutral if no label applies
    if label:
        counters[label] = counters.get(label, 0) + 1
    else:
        neutral_count += 1

# Final summary of results
print("--- Summary ---")
for key, value in counters.items():
    print(f"{key}: {value}")
print(f"Other (not divisible by 3, 5, or 2): {neutral_count}")
