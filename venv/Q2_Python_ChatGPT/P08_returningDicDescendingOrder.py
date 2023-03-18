# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 8
# Write a program that takes a list of dictionaries as input, where each dictionary contains a "name" key
# and a "age" key, and returns a new list of dictionaries sorted by age in descending order.

dictionaryList = {}

n = int(input("Please enter your dictionary range as an integer: "))

for i in range(n):
    name = input("Enter a name: ")
    age = int(input("Enter the age of {}: ".format(name)))
    dictionaryList[name] = age

sorted_dict = dict(sorted(dictionaryList.items(), key=lambda x: x[1], reverse=True))

print("\nHere your list of dictionary sorted by age in descending order : \n", sorted_dict)



