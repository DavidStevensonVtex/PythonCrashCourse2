print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# First number: 123
# Second number: 0
# Traceback (most recent call last):
#   File "D:\drs\Python\PythonCrashCourse2\ch10\division_calculator.py", line 11, in <module>
#     answer = int(first_number) / int(second_number)
#              ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
# ZeroDivisionError: division by zero