#!/usr/bin/env python3

# Prompt the user for input
number = int(input("Enter a number: "))

# Generate the multiplication table
for i in range(10):
    print(f"{i} x {number} = {i * number}")
