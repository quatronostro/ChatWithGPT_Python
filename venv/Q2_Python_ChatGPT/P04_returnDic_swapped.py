# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 4
# Write a program that takes a dictionary as input and returns a new dictionary with the keys and values swapped.

dictionaryList = {}

n = int(input("Please enter your dictionary range as an integer : "))

for i in range(n):
    key = input("Enter your key name : ")
    value = input("Enter your value : ")

    dictionaryList[key] = value

def get_swapDict(d):
    return {v: k for k, v in d.items()}

d_swapped = get_swapDict(dictionaryList)
print("\nHere is your swapped dictionary : ", d_swapped)