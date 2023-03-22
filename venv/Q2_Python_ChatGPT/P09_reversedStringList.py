# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 9
# Write a program that takes a list of string as input and returns a new list of strings where each string is reversed


stringList = []

length = int(input("Please enter your list range as input : "))

for i in range(length):
    text = input("Please enter your string here : ")
    stringList.append(text)

print("Here your list : ", stringList)

newList = []

for i in range(len(stringList)):
    newList.append(stringList[i][::-1])

print("Here your new list each string reversed : ", newList)







