# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions, and I'll be answer these questions here.



### QUESTION 4
# Write a program that prompts the user to enter a number and then prints out
# all the prime numbers less than or equal to that number.

try:
    num = int(input("Enter your number here : "))
except:
    print("You have to enter a number!")

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    i = 1
    for i in range(num):
        if (num % i) == 0:
            print(i)
else:
    print("You have to enter positive number")