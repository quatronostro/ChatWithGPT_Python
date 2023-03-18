# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 7
# Write a program that takes a string as input and returns the string with all the vowels removed


print("This program takes a string from you and returns the string with all the vowels removed.")
text = input("Enter your text : ")


result = str()
for i in text:
    if i not in "aeiouAEIOU":
        result = result + i
    else:
        pass


print(result)



