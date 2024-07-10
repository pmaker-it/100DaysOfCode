"""
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
"""
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?

name = (name1 + name2).replace(' ', '', -1).lower()

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
first_digit = t + r + u + e

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')
second_digit = l + o + v + e

total = int(str(first_digit) + str(second_digit))

if total < 10 or total > 90:
    diagnose = ", you go together like coke and mentos."
elif 40 < total < 50:
    diagnose = ", you are alright together."
else:
    diagnose = "."

print(f"Your score is {total}{diagnose}")
