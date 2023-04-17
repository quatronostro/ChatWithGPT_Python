# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions, and I'll be answer these questions here.



### QUESTION 4
# Write a program that prompts the user to enter a number and then prints out
# all the prime numbers less than or equal to that number.


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter your number here : "))


print("Prime numbers less than or equal to", num, ":")
for i in range(2, num + 1):
    if is_prime(i):
        print(i)