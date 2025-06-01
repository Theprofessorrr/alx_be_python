# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the pattern using while and for loops
while row < size:
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Print newline after each row
    row += 1
