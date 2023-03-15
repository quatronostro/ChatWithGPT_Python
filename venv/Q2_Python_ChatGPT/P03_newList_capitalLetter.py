# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 3
# Write a program that takes a list of strings as input and returns a new list with only the strings that start with a capital letter.

def upperControler(text_list):
    newList = []
    for i in text_list:
        if i[0].isupper():
            newList.append(i)
    return newList


text_list = []

n = int(input("This program takes string list from you and returns a new list if there is string with only start a capital letter."
              "\nEnter your list lenght : "))

for i in range(0, n):
    elements = input("Enter your string element : ")

    text_list.append(elements)



print("Here your new list : ", upperControler(text_list))

