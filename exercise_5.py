# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 5:
# Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# use a function and number list
def first_and_last_is_same(number_list):
    first_number = number_list[0]
    last_number = number_list[-1]

    return first_number == last_number

# assign the two list and check by printing the result
first_list = [10, 20, 30, 40, 10]
print(f"First List: {first_list} \nThe result is {first_and_last_is_same(first_list)}")

second_list = [75, 65, 35, 75, 30]
print(f"\nSecond List: {second_list} \nThe result is {first_and_last_is_same(second_list)}")