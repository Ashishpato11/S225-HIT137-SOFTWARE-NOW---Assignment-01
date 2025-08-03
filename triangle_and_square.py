"""
Triangle Checker Program
This script allows the user to input three side lengths and checks
if those lengths can form a valid triangle based on triangle inequality rules.
"""

def is_triangle_possible(a, b, c):
    """
    Determines whether three sides can form a triangle.

    A triangle is valid if the sum of any two sides is greater than the third.

    Parameters:
        a (float): Length of the first side
        b (float): Length of the second side
        c (float): Length of the third side

    Returns:
        bool: True if a triangle can be formed, False otherwise
    """
    return a + b > c and a + c > b and b + c > a

def main():
    print("Welcome! Let's find out if your three sides can make a triangle.")

    try:
        # Taking user inputs
        side1 = float(input("Please enter the length of side 1: "))
        side2 = float(input("Please enter the length of side 2: "))
        side3 = float(input("Please enter the length of side 3: "))

        # Processing
        if is_triangle_possible(side1, side2, side3):
            print("\nGreat! These lengths CAN form a triangle.")
            print("Here's a simple triangle representation:")
            print("    /\\")
            print("   /  \\")
            print("  /    \\")
            print(" /      \\")
            print("/________\\")
        else:
            print("\nOops! These lengths CANNOT form a triangle.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
