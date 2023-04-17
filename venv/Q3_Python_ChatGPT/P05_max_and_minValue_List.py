# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions, and I'll be answer these questions here.



### QUESTION 5
# Write a program that asks the user to enter a list of numbers and then prints out
# the maximum and minimum values in the list.



user_list = []

r = int(input("Please enter size for your list range : "))

for i in range(0, r):
    nums = int(input("Please enter numbers for your list : "))
    user_list.append(nums)

print("\n Maximum value on your list : ", max(user_list), ", Minimum value on your list : ", min(user_list))


