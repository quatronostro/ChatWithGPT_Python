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


# Get user input for the list of tuples
tuples_list = []
n = int(input("Enter the number of tuples: "))
for i in range(n):
    tup = tuple(input(f"Enter tuple {i + 1} (comma-separated values): ").split(","))
    tuples_list.append(tup)

# Call the function to swap the strings in each tuple
swapped_tuples = swap_strings_in_tuple(tuples_list)

# Print the resulting list of swapped tuples
print("Original List of Tuples: ", tuples_list)
print("Swapped List of Tuples: ", swapped_tuples)




