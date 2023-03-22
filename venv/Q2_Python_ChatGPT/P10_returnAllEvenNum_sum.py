# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 10
# Write a program that takes a list of integers as input and returns the sum of all the even numbers in the list.

numberList = []

length = int(input("Please enter your integer list length as integer here : "))

s = 0

for i in range(length):
    num = int(input("Please enter your list element as integer : "))
    numberList.append(num)
    if num % 2 == 0:
        s += num


print("\nHere your integer list : ", numberList, "\n"
            "Here your even numbers sum : ", s)

