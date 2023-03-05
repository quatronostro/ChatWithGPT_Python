
# This project is about my Python home practice. I want to store here to see that gaining my skills in future.
# So, I asked to ChatGPT about ask me to some Python questions about string manipulations, and I'll be answer these questions here.



### QUESTION 4
# Take two strings from user and control it if its contain certain substrings.

print("Please enter two text back to back, this program will control second text if its contain first text")
text1 = input("Enter your fist text : ")
text2 = input("\nEnter your second text : ")

if text1.__contains__(text2):
    print(text1, " contains ", text2)
else:
    print(text1, " doesnt contains ", text2)
