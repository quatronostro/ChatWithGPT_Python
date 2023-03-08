# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 1
# Write a program that takes a list of integers as input and returns a new list with only the even numbers from the original list.

print("This program takes list of integers from you as input and returns a new list with only even numbers."
      "\nTo finish entering elements of your list, please press 'Q' ")

lst = []

nums = (input("Please enter your elements : "))

while (nums != "Q"):
    if nums != "Q" or "q":
        for i in range(0, nums):
            elements = int(nums)

            lst.append(elements)
    else:
        break

newLst = []

for i in lst:
    if i % 2 == 0:
        newLst.append(i)

print(newLst)