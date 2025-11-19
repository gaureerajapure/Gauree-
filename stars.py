# Pyramid Pattern Program

# Input number of rows
N = int(input("Enter number of rows: "))

# Outer loop for rows
for i in range(1, N + 1,):
    # Print spaces (to center the pyramid)
    for j in range(N - i):
        print(" ", end="")

    # Print stars (odd number: 2*i - 1)
    for j in range(2 * i - 1):
        print("*", end="")

    # Move to next line after each row
    print()
