# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions, and I'll be answer these questions here.



### QUESTION 3
# Write a function called count_vowels that takes a string as input and returns the number of vowels in the string.

def count_vowels(text):
    num = 0
    for i in text:
        if i in "aeiouAEIOU":
            num += 1
    return num

str = input("Please enter your text : ")

print("You text has", count_vowels(str), "vowel letters")