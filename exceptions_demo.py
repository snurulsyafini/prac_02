"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:      # answer for question 3
        print(f"Denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")


# 1) When will a ValueError occur?
#  ValueError occurs when input is not a number (e.g, alphabets)
# 2) When will a ZeroDivisionError occur?
#  ZeroDivisionError occurs when denominator is 0
# 3) Could you change the code to avoid the possibility of a ZeroDivisionError?
#  Yes.
