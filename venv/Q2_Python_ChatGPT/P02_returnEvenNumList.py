# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 1
# Write a program that takes a list of integers as input and returns a new list with only the even numbers from the original list.


def get_even_numbers(numbers_list):
    # Initialize an empty list to hold even numbers
    even_numbers = []

    # Iterate over each number in the list
    for num in numbers_list:
        # Check if the number is even
        if num % 2 == 0:
            # If it's even, append it to the list of even numbers
            even_numbers.append(num)

    # Return the list of even numbers
    return even_numbers


# Example usage

numbers = []

# number of elements as input
n = int(input("This program takes integer list from you and returns a new list with only the even numbers from the original list."
              "\nEnter your list length : "))

# iterating till the range
for i in range(0, n):
    elements = int(input("Enter your element : "))

    numbers.append(elements)  # adding the element


even_numbers = get_even_numbers(numbers)
print("\nYour list with only even numbers : ", even_numbers)
