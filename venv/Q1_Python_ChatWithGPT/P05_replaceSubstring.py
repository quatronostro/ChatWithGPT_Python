
# This project is about my Python home practice. I want to store here to see that gaining my skills in future.
# So, I asked to ChatGPT about ask me to some Python questions about string manipulations, and I'll be answer these questions here.



### QUESTION 5
# Take two strings from user and replace substring with another substring.
flag = True

text1 = input("Please enter a text : ")
print("This is your text : ", text1)


while flag:
    yOrN = input("If you want to change something in your text please enter please press 'Y', if not please press 'N' : ")

    if yOrN == "Y" or yOrN == "y":
        i = input("Which word do you want to change : ")
        c = input("What do you want to replace it with : ")
        newText = text1.replace(i, c)
        print("Last version of your text : ", newText)
        flag = False
    elif yOrN == "N" or yOrN == "n":
        print("Your text saved like this : ", text1)
        flag = False
    else:
        print("You entered wrong value, please try again.")
        flag = True