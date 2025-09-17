"""
User Input: Start by asking the user to input two distinct integers. 
Logical Operators: Implement six different logical comparisons using the input integers. Include two examples for each of the following operators:
and
or
not
Display Results: Print the logical statement and its result for each comparison.
Guidelines for Logical Comparisons:
Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
Try to use comparisons that could yield different results based on user input.
Sample Output: Here's an example of what your program's output might look like:
"""

print(int(input("enter a number: ")))
print(int(input("enter another number: ")))

A = 10

B = 20

C = 30

if A > B and A > C:
    print("this number is lower then 10 ")
elif A < B and A < C:
    print("the number is higher then 10")
else: print("your number is 10")

if B > C and B > A:
    print("your number is lower then 10 ")
elif B < C and B < A:
    print("your number is higher then 10")
else: print("Your number is 20")

if C > A or C > B:
    print("your number is in between 10 and 30")
elif C < A or C < B:
    print("your number is between 20 and 30")
else: print("your number is 30")

if A < C or A < B:
    print("your number is lower then 20")
elif B < C or B > A:
    print("your number is in between 10 and 30")
else: print("your number is 10")

if not B > A:
    print("Your number is higher then 10 ")
else: print("your number is 20")

if not C > B:
    print("Your number is higher then 20 ")
else: print("your number is 30")
