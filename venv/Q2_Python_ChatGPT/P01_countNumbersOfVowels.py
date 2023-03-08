# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions about data types and manipulating them, and I'll be answer these questions here.



### QUESTION 1
# Write a program that takes a string as input and counts the number of vowels in the string.

text = input("This program will count vowel letters in your text"
             "\nPlease enter some text here : ")

vowel = {"a", "e", "i", "o", "u"}
count = 0

for i in vowel:
    count += text.count(i)

print("Sum of vowel letters in your text : ", count)


