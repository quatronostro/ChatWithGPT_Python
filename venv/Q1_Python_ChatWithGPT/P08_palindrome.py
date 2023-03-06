# This project is about my Python home practice. I want to store here to see that gaining my skills in future.
# So, I asked to ChatGPT about ask me to some Python questions about string manipulations, and I'll be answer these questions here.



### QUESTION 8
# Check if a string is a palindrome or not.

print("This program checks your text if its palindrome or not.")
text = input("Enter your text : ")

if text == text[::-1]:
    print("\nYour text is palindrome.")
else:
    print("\nYour text is NOT a palindrome.")