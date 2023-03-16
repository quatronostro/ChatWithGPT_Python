# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 6
# Write a program that takes a list of integers as input and returns a new list with the numbers sorted in descending order.


nums_list = []


numsLength = int(input("Please enter your list length as an integer : "))

for i in range(numsLength):
    nums = int(input("Please enter your numbers : "))
    nums_list.append(nums)

new_list = []
new_list.extend(nums_list)
new_list.sort(reverse=True)

print("\nThis is your list : ", nums_list)
print("This is the new list with the numbers sorted descending order : ", new_list)



