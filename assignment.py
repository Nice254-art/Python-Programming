# Assignment
# Python program that checks whether a year is a leap year or not


year = int(input("Enter the year you wish to know if it is a leap year: "))
# To get year (integer input) from the user


# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))

# Python program that checks  whether alphabet is a vowel or a consonant

alphabet = input("Enter a single alphabet: ")

# Make sure the input is a single character
if len(alphabet) == 1:
    # Convert the input to lowercase to handle both uppercase and lowercase alphabets
    alphabet = alphabet.lower()

    # Check if the input is a vowel
    if alphabet in 'aeiou':
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("Please enter a single alphabet.")