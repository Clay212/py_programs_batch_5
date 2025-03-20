# Ask the user to input a number
num = int(input("Enter a number (0-1000): "))
if 0 <= num <= 1000:
    #Format the input in six digits
    digit = f"{num:06d}" 
    print("Formatted Output:", digit)
else:
    print("Invalid input! Please enter a number between 0 and 1000 :) .") 
