# ==================== strings ===============================
string1 = "ice cream"
string2 = 'butter fly'

text1 = "atharv111p@gmail.com"
text2 = "rj@yA45%uIS-orwdl"

# Indexing
print(string1[1])
print(string1[0])
print(string2[-1])

# strings are immutable - not changeable
string2[0] = 'a'

# Slicing
print(string1[0: 3])
print(string1[: 3])
print(string1[1: ])

# Reversing
print(string1[::-1])

# Fun with strings
print(string1 + ' ' + string2)
print(string1*2)
print(string1 + 2) # TypeError: can only concatenate str (not "int") to str
print(string1 + str(2)) # Typecasting means conversion of datatype

# Iteration
s = "Python"
for char in s:
    print(char)