# Task 1: Check if a Number is Even or Odd
# Take an integer input from the user
'''
a = int(input('Enter an integer: '))

# Check if the number is even or odd
if a % 2 == 0:
    print(f"{a} is an even number")
else:
    print(f'{a} is an odd number')
'''



#Task 2: Sum of Integers from 1 to 50 Using a Loop
# Initialize the sum to 0
a = 0

# Use a for loop to iterate over numbers from 1 to 50
for x in range(1, 51):
    a += x  # Add each number to the total sum

# Display the final sum
print('The sum of all integers from 1 to 50 is:', a)
