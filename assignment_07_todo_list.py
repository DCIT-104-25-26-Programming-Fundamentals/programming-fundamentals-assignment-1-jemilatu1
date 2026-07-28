# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

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
        # Returned when multiple modes exist or data is multimodal in older Python logic
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
    """Safely prompts the user for a valid number."""
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
