# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================







import csv
import json
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


def get_stats_dict(numbers):
    """Generates a dictionary containing all statistical measures."""
    mode_val = calculate_mode(numbers)
    mode_str = f"{mode_val:.2f}" if isinstance(mode_val, (int, float)) else str(mode_val)

    return {
        "Count": len(numbers),
        "Sum": round(calculate_sum(numbers), 2),
        "Average (Mean)": round(calculate_average(numbers), 2),
        "Median": round(calculate_median(numbers), 2),
        "Mode": mode_str,
        "Maximum": round(find_max(numbers), 2),
        "Minimum": round(find_min(numbers), 2),
        "Range": round(find_max(numbers) - find_min(numbers), 2),
        "Variance (Sample)": round(calculate_variance(numbers), 2),
        "Std Dev (Sample)": round(calculate_std_dev(numbers), 2),
    }


def print_results(stats):
    """Prints a formatted report to stdout."""
    print("\n" + "=" * 35)
    print("        STATISTICAL REPORT        ")
    print("=" * 35)
    for key, value in stats.items():
        print(f"{key:<20}: {value}")
    print("=" * 35)


def export_report(stats, filename, fmt="txt"):
    """Exports the statistical summary to TXT, JSON, or CSV."""
    path = Path(filename)
    
    if fmt == "json":
        with open(path.with_suffix(".json"), "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=4)
    elif fmt == "csv":
        with open(path.with_suffix(".csv"), "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Metric", "Value"])
            for k, v in stats.items():
                writer.writerow([k, v])
    else:  # TXT
        with open(path.with_suffix(".txt"), "w", encoding="utf-8") as f:
            f.write("=" * 35 + "\n")
            f.write("        STATISTICAL REPORT        \n")
            f.write("=" * 35 + "\n")
            for k, v in stats.items():
                f.write(f"{k:<20}: {v}\n")
            f.write("=" * 35 + "\n")

    print(f"\nReport successfully saved to {path.with_suffix('.' + fmt)}")


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
        stats = get_stats_dict(numbers)
        print_results(stats)

        save_choice = input("\nWould you like to export this report? (y/n): ").strip().lower()
        if save_choice == "y":
            fmt = input("Enter format (txt / json / csv): ").strip().lower()
            if fmt not in ["txt", "json", "csv"]:
                fmt = "txt"
            filename = input("Enter output filename (without extension): ").strip() or "stats_report"
            export_report(stats, filename, fmt)


if __name__ == "__main__":
    main()
