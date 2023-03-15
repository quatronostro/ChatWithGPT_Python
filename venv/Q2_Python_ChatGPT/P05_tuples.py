import ast

# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 5
# Write a program that takes a list of tuples, where each tuple contains two strings, and returns a new list of tuples
#where the strings in each tuple are swaped

def swap_strings_in_tuple(tuples_list):
    # Initialize an empty list to hold swapped tuples
    swapped_tuples = []

    # Iterate over each tuple in the list
    for tup in tuples_list:
        # Swap the order of the strings in the tuple and append the new tuple to the list of swapped tuples
        swapped_tuples.append((tup[1], tup[0]))

    # Return the list of swapped tuples
    return swapped_tuples

try:
    input_list = ast.literal_eval(
        input('Enter a valid Python set, e.g. {"a", "b"}: ')
    )
except ValueError:
    print('The provided value is not a set object')

print(input_list)


# Example usage
tuples = [('hello', 'world'), ('good', 'morning'), ('how', 'are you')]
swapped_tuples = swap_strings_in_tuple(tuples)
print(swapped_tuples)

