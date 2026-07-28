# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================




# Function to calculate the sum
def calculate_sum(numbers):
    return sum(numbers)


# Function to calculate the average
def calculate_average(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


# Function to find the maximum value
def find_max(numbers):
    return max(numbers) if numbers else None


# Function to find the minimum value
def find_min(numbers):
    return min(numbers) if numbers else None


def get_float_input(prompt):
    """Safely prompts the user for a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    while True:
        try:
            n = int(input("How many numbers? "))
            if n <= 0:
                print("Error: Number of values must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    numbers = []
    for i in range(n):
        num = get_float_input(f"Enter number {i + 1}: ")
        numbers.append(num)

    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers):.2f}")
    print(f"Average: {calculate_average(numbers):.2f}")
    print(f"Maximum: {find_max(numbers):.2f}")
    print(f"Minimum: {find_min(numbers):.2f}")


if __name__ == "__main__":
    main()
