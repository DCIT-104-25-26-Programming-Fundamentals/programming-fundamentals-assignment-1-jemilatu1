# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================







import sys
import statistics
from pathlib import Path


def calculate_sum(numbers):
    return sum(numbers)


def calculate_average(numbers):
    if not numbers:
        return 0.0
    return statistics.mean(numbers)


def calculate_median(numbers):
    if not numbers:
        return 0.0
    return statistics.median(numbers)


def calculate_mode(numbers):
    if not numbers:
        return None
    try:
        return statistics.mode(numbers)
    except statistics.StatisticsError:
        return "No unique mode"


def calculate_variance(numbers):
    if len(numbers) < 2:
        return 0.0
    return statistics.variance(numbers)


def calculate_std_dev(numbers):
    if len(numbers) < 2:
        return 0.0
    return statistics.stdev(numbers)


def find_max(numbers):
    return max(numbers) if numbers else None


def find_min(numbers):
    return min(numbers) if numbers else None


def get_float_input(prompt):
    """Safely prompts the user for a valid float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def load_numbers_from_file(file_path):
    """Reads numbers separated by commas, spaces, or newlines from a file."""
    numbers = []
    path = Path(file_path)

    if not path.exists():
        print(f"Error: File '{file_path}' not found.")
        return None

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read().replace(",", " ")
            for token in content.split():
                try:
                    numbers.append(float(token))
                except ValueError:
                    print(f"Warning: Skipped non-numeric entry '{token}'")
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    return numbers


def get_numbers_from_console():
    """Prompts user to enter numbers interactively."""
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

    return numbers


def print_results(numbers):
    """Prints a detailed statistical report for the input dataset."""
    if not numbers:
        print("\nNo numbers to analyze.")
        return

    mode_val = calculate_mode(numbers)
    mode_str = f"{mode_val:.2f}" if isinstance(mode_val, (int, float)) else str(mode_val)

    print("\n" + "=" * 35)
    print("        STATISTICAL REPORT        ")
    print("=" * 35)
    print(f"Count:              {len(numbers)}")
    print(f"Sum:                {calculate_sum(numbers):.2f}")
    print(f"Average (Mean):     {calculate_average(numbers):.2f}")
    print(f"Median:             {calculate_median(numbers):.2f}")
    print(f"Mode:               {mode_str}")
    print(f"Maximum:            {find_max(numbers):.2f}")
    print(f"Minimum:            {find_min(numbers):.2f}")
    print(f"Range:              {find_max(numbers) - find_min(numbers):.2f}")
    print(f"Variance (Sample):  {calculate_variance(numbers):.2f}")
    print(f"Std Dev (Sample):   {calculate_std_dev(numbers):.2f}")
    print("=" * 35)


def main():
    print("Data Analysis Tool")
    print("1. Enter numbers manually")
    print("2. Read numbers from a file (.txt, .csv)")
    
    choice = input("Choose input method (1 or 2): ").strip()

    if choice == "2":
        file_path = input("Enter path to file: ").strip()
        numbers = load_numbers_from_file(file_path)
    else:
        numbers = get_numbers_from_console()

    if numbers:
        print_results(numbers)


if __name__ == "__main__":
    main()
