
"""
Excellent question! Let me break this down step by step. Your visualization is almost correct, but let's see exactly what happens.

---

## **Breaking Down `print(' '.join([str(i)] * i))`**

Let me trace through this with **i = 3** as an example:

### **Step 1: `str(i)`**
```python
str(3)  →  "3"
```
Converts the number to a string.

### **Step 2: `[str(i)]`**
```python
["3"]
```
Creates a **list** with one element: the string "3"

### **Step 3: `[str(i)] * i`**
```python
["3"] * 3  →  ["3", "3", "3"]
```
Multiplies the list, creating a list with **3 copies** of "3"

### **Step 4: `' '.join([str(i)] * i)`**
```python
' '.join(["3", "3", "3"])  →  "3 3 3"
```
The `join()` method takes all elements in the list and **connects them with a space** between each element.

**Key Point:** `join()` puts the space **BETWEEN** elements, not before or after!

---

## **Complete Example for i = 1 to 5:**

```python
for i in range(1, 6):
    print(' '.join([str(i)] * i))
```

**Iteration by iteration:**

| i | [str(i)] | [str(i)] * i | ' '.join(...) | Output |
|---|----------|--------------|---------------|--------|
| 1 | ["1"] | ["1"] | "1" | `1` |
| 2 | ["2"] | ["2", "2"] | "2 2" | `2 2` |
| 3 | ["3"] | ["3", "3", "3"] | "3 3 3" | `3 3 3` |
| 4 | ["4"] | ["4", "4", "4", "4"] | "4 4 4 4" | `4 4 4 4` |
| 5 | ["5"] | ["5", "5", "5", "5", "5"] | "5 5 5 5 5" | `5 5 5 5 5` |

**Final Output:**
```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

## **Why Your Visualization Was Close But Not Quite Right**

You thought: "space 1, next line, space 22, next line..."

But actually:
- `join()` doesn't add a space at the **beginning**
- `join()` only adds spaces **between** the elements
- So for `["3", "3", "3"]`, it produces `"3 3 3"` (space between, not before)

---

## **Visualizing `join()` More Clearly**

Think of `join()` as **gluing** items together with the string you specify:

```python
# Example 1: Join with space
' '.join(['a', 'b', 'c'])  →  "a b c"

# Example 2: Join with comma
','.join(['a', 'b', 'c'])  →  "a,b,c"

# Example 3: Join with dash
'-'.join(['2025', '01', '15'])  →  "2025-01-15"

# Example 4: Join with nothing
''.join(['H', 'e', 'l', 'l', 'o'])  →  "Hello"
```

The pattern: `glue.join([item1, item2, item3])` → `"item1{glue}item2{glue}item3"`

---

## **Comparison: Your Method vs join() Method**

### **Your Method:**
```python
print(str(i) * i)
```
- When i=3: `"3" * 3` → `"333"` (no spaces)

### **With join():**
```python
print(' '.join([str(i)] * i))
```
- When i=3: Creates `["3", "3", "3"]` then joins with space → `"3 3 3"` (with spaces)

---

## **Alternative Ways to Add Spaces**

If you want spaces in your original approach:

```python
# Method 1: Add space to the string before multiplying
for i in range(1, 6):
    print((str(i) + ' ') * i)
```
**Output:**
```
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
```
*(Note: Extra space at the end of each line)*

```python
# Method 2: Use strip() to remove trailing space
for i in range(1, 6):
    print(((str(i) + ' ') * i).strip())
```
**Output:**
```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

## **Quick Test - Try These in Your Mind**

```python
# What will these produce?

1. '-'.join(['10', '20', '30'])
2. ''.join(['P', 'y', 't', 'h', 'o', 'n'])
3. ', '.join(['apple', 'banana', 'cherry'])
4. ' and '.join(['Tom', 'Jerry'])
```

<details>
<summary>Answers (click to reveal)</summary>

1. `"10-20-30"`
2. `"Python"`
3. `"apple, banana, cherry"`
4. `"Tom and Jerry"`

</details>

---

## **Does This Make Sense Now?**

The key insight: **`join()` only puts the string BETWEEN items, never at the start or end.**

Let me know if you want me to explain anything else, or if you're ready to continue with Questions 5-10! 🚀
"""

"""
## **Question 1: Variables and Data Types (Easy)**
Write a Python program that:
- Takes a user's name (string) and age (integer) as input
- Calculates what year they were born
- Prints: "Hello [name], you were born in [year]"
"""
from datetime import datetime

current_date = datetime.now()
current_year = datetime.now().year

def answer_user_birth_year():
    user_name = input("Could you please tell me your good name?")
    age = int(input("What is your age?"))
    year_of_birth = current_year-age
    print(f"Hello {user_name}, you were born in {year_of_birth}")
    
answer_user_birth_year()

"""
## **Question 2: Operators (Easy)**
What will be the output of this code? Explain why.
```python
x = 10
y = 3
print(x // y)
print(x % y)
print(x ** y)
```
"""
x = 10 # integer value = 10
y = 3 # integer value = 3
print(x // y) # integer value = 3, here it is doing implicit type casting on using // which means integer division so, it is int(3.3333)=3
print(x % y) # = 1, return remainder 
print(x ** y) # = 1000; double * is used for calculating power

"""
## **Question 3: Control Flow - Conditionals (Medium)**
Write a program that takes a number as input and prints:
- "Positive and Even" if the number is positive and even
- "Positive and Odd" if the number is positive and odd
- "Negative and Even" if the number is negative and even
- "Negative and Odd" if the number is negative and odd
- "Zero" if the number is zero
"""
k = int(input("Enter an integer"))
if k > 0 and k % 2 == 0:
    print("Positive and Even")
elif k > 0 and k % 2 != 0:
    print("Positive and Odd")
elif k < 0 and k % 2 == 0:
    print("Negative and Even")
elif k < 0 and k % 2 != 0:
    print("Negative and Odd")
else:
    print("Zero")
# OR
if k > 0:
    if k % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif k < 0:
    if k % 2 == 0:
        print("Negative and Even")
    else:
        print("Negative and Odd")
else:
    print("Zero")

"""
## **Question 4: Loops (Medium)**
Write a program that prints the following pattern:
```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```
"""
for i in range(1, 6):
    print((str(i)+' ')*i)
# OR
for i in range(5):
    print(" ".join(str(i+1)*(i+1)))
# OR
for i in range(1, 6):
    print(" ".join(str(i)*i))

"""
## **Question 5: Functions (Medium)**
Write a function called `is_prime(n)` that:
- Takes a number as input
- Returns `True` if the number is prime, `False` otherwise
- Test it with numbers: 7, 10, 13, 1
"""
def is_prime(n):
    count = 0
    if n > 2:
        for i in range(2, (n+1)//2, 1):
            if n % i != 0:
                count += 1

            else:
                count = 0
    if n == 2 or n == 3:
        count += 1
    elif n < 2:
        count = 0

    if count != 0:
        return True
    else:
        return False
    
x = int(input("Enter a number"))
print(is_prime(x))

# OR
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


"""
## **Question 6: Nested Loops (Medium-Hard)**
Write a program to find all pairs of numbers from 1 to 20 where:
- The sum of the two numbers equals 25
- Print each pair only once (e.g., if you print (5, 20), don't print (20, 5))
"""

sum_of_pairs = 25
list_of_result_pairs = []
for i in range(0, (sum_of_pairs+1)//2):
    j = sum_of_pairs-i
    list_of_result_pairs.append((i, j))

print(list_of_result_pairs)

# OR 
target = 25

for a in range(1, 21):
    b = target - a
    if a < b and 1 <= b <= 20:
        print(a, b)


"""
## **Question 7: Functions with Multiple Parameters (Medium)**
Write a function `calculate(num1, num2, operation)` that:
- Takes two numbers and an operation (string: "add", "subtract", "multiply", "divide")
- Returns the result of the operation
- Handles division by zero with an appropriate message
"""
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1+num2
    if operation == 'subtract':
        return num1-num2
    if operation == 'multiply':
        return num1*num2
    if operation == 'divide':
        try:
            return num1/num2
        except Exception as e:
            print(f'Exception as {e}')
            return None
    
    else:
        return 'Invalid input'

print(calculate(231, 376, 'add'))
print(calculate(142, 349, 'multiply'))
print(calculate(990, 287, 'subtract'))
print(calculate(293, 987, 'subtract'))
print(calculate(932, 0, 'divide'))
print(calculate(932, 134, 'divide'))
print(calculate(932, 9987, 'divide'))
print(calculate(1254, 2314, 'abcd'))


"""
## **Question 8: Logic Challenge (Hard)**
Write a program that takes a year as input and determines if it's a leap year.
Rules:
- Divisible by 4 → leap year
- EXCEPT if divisible by 100 → not a leap year
- EXCEPT if divisible by 400 → leap year

Test with: 2000, 1900, 2024, 2023
"""
y = int(input("Enter a year"))
# y = 1000, 1001, 1002, 1003, 1004,.........1900, 1901, 1902,...2020, 2021...
if y%4 == 0 and y%100 != 0:
    print("Leap year")
elif y%4 == 0 and y%400 == 0:
    print("Leap year")
else:
    print("Not a Leap year")

"""
## **Question 9: String Manipulation (Medium-Hard)**
Write a function `reverse_words(sentence)` that:
- Takes a sentence as input
- Returns the sentence with each word reversed, but words in the same order
- Example: "Hello World" → "olleH dlroW"
"""
def reverse_string(s):
    s_rev = s.split(' ')
    words_s_rev = []
    for i in range(len(s_rev)):
        rev_s_words = s_rev[i][::-1]
        words_s_rev.append(rev_s_words)

    return words_s_rev

users_string = input()
print(reverse_string(users_string))   # I am unable to convert the list into string and result the string out. I know, I am wrong, but I am not understanding the logic

# corrected code
def reverse_words(sentence):
    words = sentence.split()              # Split into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return " ".join(reversed_words)       # Convert list → string

s = "Hello Micheal Hey Sam What'sup John"
print(reverse_words(s))

"""
## **Question 10: Problem Solving (Hard)**
Write a program that finds the **second largest number** in a list without using sorting functions.

Example: `[10, 5, 8, 20, 15, 3]` → Output: `15`
"""
l = [10, 5, 8, 20, 15, 3]
m = max(l)
diff_l = []
for i in l:
    diff_l.append(m-i)
print(diff_l)
l.sort()
print(l[-2]) # I know I am wrong but, I tried a lot but not getting the logic

# corrected code
num = [10, 5, 8, 20, 15, 3]

largest_number = float('-inf')
second_largest_number = float('-inf')

for i in num:
    if i > largest_number:
        second_largest_number = largest_number
        largest_number = i

    elif i > second_largest_number and i != largest_number:
        second_largest_number = i

print(second_largest_number)
