"""
Triangle Checker Program
# This program checks if three numbers can form a triangle,
"""

def is_triangle_possible(a, b, c):
    """
    Determines whether three sides can form a triangle.

    A triangle is valid if the sum of any two sides is greater than the third.

    """
    return a + b > c and a + c > b and b + c > a

def main():
    print("Let's find out if three sides can make a triangle.")

    try:
        # Taking user inputs
        side1 = float(input("Please enter the length of side 1: "))
        side2 = float(input("Please enter the length of side 2: "))
        side3 = float(input("Please enter the length of side 3: "))

        # Checking and Displaying
        if is_triangle_possible(side1, side2, side3):
            print("Yes, these three lengths can form a triangle.")
            print("No, these lengths cannot form a triangle. ")
        else:
            print("Please enter valid numbers only.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
