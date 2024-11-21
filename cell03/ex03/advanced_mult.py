#!/usr/bin/env python3

# Loop through each number from 0 to 10
for table in range(11):
    # Print the table header
    print(f"Table de {table}: ", end="")
    # Generate and print the multiplication table
    for multiplier in range(11):
        print(f"{table * multiplier}", end=" ")
    # Print a newline after each table
    print()
