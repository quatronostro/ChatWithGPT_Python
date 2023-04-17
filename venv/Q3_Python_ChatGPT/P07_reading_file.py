# This project is about my Python home practice. I want to store here to see that gaining my skills in the future.
# So, I asked to ChatGPT about ask me to some Python questions, and I'll be answer these questions here.



### QUESTION 7
# Write a program that reads in a file called input.txt and writes out a file called output.txt
# that contains the same lines as input.txt but with all the vowels removed.



# Open input and output files
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # Loop through each line in the input file
    for line in input_file:
        # Remove vowels from the line and write to output file
        vowels = 'aeiouAEIOU'
        new_line = ''.join([char for char in line if char not in vowels])
        output_file.write(new_line)
