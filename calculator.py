# imports needed for the program 
import math  # Provides mathematical functions like sqrt and pi
from fractions import Fraction  # Used for fractional calculations

# fraction made for easy access
f12 = Fraction(1, 2)  # Represents 1/2 as a fraction

# for compounding/depreciation
basequestion = (
    "Choose a number from 1-4. \n"
    "- 1 = Simple Compounding\n"
    "- 2 = Complex Compounding\n"
    "- 3 = Depreciation\n"
    "- 4 = Complex Depreciation\n"
    "Enter your answer here:\n"
)

# functions for the starting user interface to execute
def get_user_input():
    """Gets user input for the desired calculation."""
    print("What would you like to calculate?\n")
    print("1. Pythagorean Theorem")
    print("2. Area of a Triangle")
    print("3. Area of a Circle")
    print("4. Find the circumference of a circle")
    print("5. Rounding")
    print("6. Find the area of a square")
    print("7. Find the area of a kite")
    print("8. Compounding and Depreciation")
    print("9. Exit\n")
    choice = input("Enter the number of your choice: ")
    return choice

# Calculate the circumference of a circle
def calculate_circumference(radiusInput):
    """Calculates and prints the circumference of a circle."""
    c = 2 * math.pi  # Formula for circumference
    d = c * radiusInput
    print('Your answer is ' + str(d) + "!")

# Calculate the hypotenuse using the Pythagorean theorem
def calculate_hypotenuse(a, b):
    """Calculates and prints the hypotenuse of a right triangle."""
    c = (a**2 + b**2)  # Sum of squares of the two sides
    d = math.sqrt(c)  # Square root of the sum
    finalAnswer = "Your answer is " + str(d) + "!"
    print(finalAnswer)

# Rounding a number to a specified number of decimal places
def rounding(numInput, roundInput):
    """Rounds a number to the specified number of decimal places."""
    finalAnswer = round(numInput, roundInput)
    print(finalAnswer)

# Calculate the area of a triangle
def triangle_area(baseInput, heightInput):
    """Calculates and prints the area of a triangle."""
    triangle_area = (baseInput * heightInput) / 2
    print("Your triangle's area is " + str(triangle_area) + "!")

# Calculate the area of a circle
def circle_area(radiusInput):
    """Calculates and prints the area of a circle."""
    circle_area = math.pi * radiusInput * 2  # Formula for area
    print("Your circle's area is " + str(circle_area) + "!")

# Calculate the area of a square or rectangle
def square_area(lengthInput, widthInput):
    """Calculates and prints the area of a square or rectangle."""
    square_area = lengthInput * widthInput
    print("Your rectangle's area is " + str(square_area) + "!")

# Calculate the area of a kite
def kite_area(diagonalOne, diagonalTwo):
    """Calculates and prints the area of a kite."""
    kite_area = f12 * diagonalOne * diagonalTwo  # Formula for kite area
    print(kite_area)

# Simple compounding interest calculation
def compound_interest1(principal, rate, periods):
    """Calculates and prints simple compounding interest."""
    A = principal * (1 + rate)**periods
    print('Your answer is:')
    print(round(A, 2))

# Complex compounding interest calculation
def compound_interest2(principal, rate, times_compounded, years):
    """Calculates and prints complex compounding interest."""
    A = principal * (1 + (rate/times_compounded))**(times_compounded*years)
    print('Your answer is:') 
    print(round(A, 2))

# Simple depreciation calculation
def depreciation1(principal, rate, periods):
    """Calculates and prints simple depreciation."""
    A = principal * (1 - rate)**periods
    print(round(A, 2))

# Complex depreciation calculation
def depreciation2(rate, principal, times_depreciated, years):
    """Calculates and prints complex depreciation."""
    A = principal * (1 - rate/times_depreciated)**(times_depreciated*years)
    print(round(A, 2))

# Main user interface loop
while True:
    choice = get_user_input()  # Get the user's choice
    if choice == "1":
        # Pythagorean theorem
        print("What is the value of a?")
        aInput = int(input())
        print("What is the value of b?")
        bInput = int(input())
        calculate_hypotenuse(aInput, bInput)
    elif choice == "2":
        # Area of a triangle
        print("What is the base of the triangle?")
        baseInput = int(input())
        print("What is the height of the triangle?")
        heightInput = int(input())
        triangle_area(baseInput, heightInput)
    elif choice == "3":
        # Area of a circle
        print("What is the radius of the circle?")
        radiusInput = int(input())
        circle_area(radiusInput)
    elif choice == "4":
        # Circumference of a circle
        print("What is the radius of the circle?")
        radiusInput2 = int(input())
        calculate_circumference(radiusInput2)
    elif choice == "5":
        # Rounding
        print("What decimal point would you like to round to? Write as a number.")
        roundInput = int(input())
        print("What is the number you want to round to?")
        numInput = float(input())
        rounding(numInput, roundInput)
    elif choice == "6":
        # Area of a square or rectangle
        print("What is the length of your rectangle/square?")
        lengthInput = int(input())
        print("What is the width of your rectangle/square?")
        widthInput = int(input())
        square_area(lengthInput, widthInput)
    elif choice == "7":
        # Area of a kite
        print("What is the length of diagonal one?")
        diagonalOne = int(input())
        print("What is the length of diagonal two?")
        diagonalTwo = int(input())
        kite_area(diagonalOne, diagonalTwo)
    elif choice == '8':
        # Compounding and depreciation
        c2 = int(input(basequestion))
        if c2 == 1:
            # Simple compounding
            print('What is your principal?')
            principal = int(input())
            print('What is your rate?')
            r1 = str(input())
            r2 = r1.replace('%', '')
            r3 = int(r2)
            rate = r3 / 100
            print('What is the amount of periods it is converted over?')
            periods = int(input())
            compound_interest1(principal, rate, periods)
        elif c2 == 2:
            # Complex compounding
            print('What is your principal?')
            principal = int(input())
            print('What is your rate?')
            r1 = str(input())
            r2 = r1.replace('%', '')
            r3 = int(r2)
            rate = r3 / 100
            print('What is the amount of times it is compounded in one year?')
            times_compounded = int(input())
            print('How many years has it been compounding for?')
            years = int(input())
            compound_interest2(principal, rate, times_compounded, years)
        elif c2 == 3:
            # Simple depreciation
            print('What is your principal?')
            principal = int(input())
            print('What is your rate?')
            r1 = str(input())
            r2 = r1.replace('%', '')
            r3 = int(r2)
            rate = r3 / 100
            print('What is your amount of periods')
            periods = int(input())
            depreciation1(principal, rate, periods)
        elif c2 == 4:
            # Complex depreciation
            print('What is your principal?')
            principal = int(input())
            print('What is your rate?')
            r1 = str(input())
            r2 = r1.replace('%', '')
            r3 = int(r2)
            rate = r3 / 100
            print('What is the amount of times it is depreciated in one year?')
            times_depreciated = int(input())
            print('How many years has it been depreciating for?')
            years = int(input())
            depreciation2(principal, rate, times_depreciated, years)
    elif choice == "9":
        # Exit the program
        print("Exiting the program. Goodbye!")
        print('Note: This program is still in development.')
        break  # Exit the loop
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")
