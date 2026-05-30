"""Create a program that helps organize a family reunion with two tasks. 
First, read two integers and find the leading digit of the first number raised to the power of the second 
(this helps estimate large quantities). Then, read a text message and rearrange it by moving all consonants 
to the beginning while keeping vowels, spaces, and punctuation after them—all in their original order."""
# Read the two integers
base = int(input())
exponent = int(input())

# Calculate base^exponent and find the leading digit
result = base ** exponent
leading_digit = int(str(result)[0])
print(leading_digit)

# Read the text message
message = input()

# Define vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Separate consonants and non-consonants (vowels, spaces, punctuation)
consonants = []
non_consonants = []

for char in message:
    if char.isalpha() and char not in vowels:
        # It's a consonant
        consonants.append(char)
    else:
        # It's a vowel, space, or punctuation
        non_consonants.append(char)

# Combine consonants first, then non-consonants
rearranged = ''.join(consonants) + ''.join(non_consonants)
print(rearranged)