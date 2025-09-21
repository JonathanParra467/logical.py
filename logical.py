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

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer (different from the first): "))

print("\nLogical Comparisons:\n")

result1 = (num1 > 0) and (num2 > 0)
print(f"Both numbers are positive:{result1}")

result2 = (num1 % 2 == 0) and (num2 % 2 == 0)
print(f"Both numbers are even: {result2}")

result3 = (num1 < 0) or (num2 < 0)
print(f"At least one number is negative: {result3}")

result4 = (num1 == 10) or (num2 == 10)
print(f"At least one number is 10: {result4}")

result5 = not (num1 == num2)
print(f"The numbers are not equal: {result5}")

result6 = not ((num1 < 0) or (num2 < 0))
print(f"Neither number is negative: {result6}")

