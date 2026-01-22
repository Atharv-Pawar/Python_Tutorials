"""
Question 1: String Manipulation (Easy)
Write a function that takes a string and returns a dictionary with the count of each character (case-insensitive). Ignore spaces.
Example:
Input: "Hello World"
Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
"""

def count_letters(input_string):
    char_count = {}
    for char in input_string.lower():
        if char != ' ':
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

user_string = "Hello World"
print(count_letters(user_string))

"""
Question 2: List Processing (Medium)
Given a list of dictionaries representing transactions, write a function to:

Group transactions by user_id
Calculate total amount per user
Return top 3 users by total amount

Example:
pythontransactions = [
    {'user_id': 'U1', 'amount': 100},
    {'user_id': 'U2', 'amount': 200},
    {'user_id': 'U1', 'amount': 150},
    {'user_id': 'U3', 'amount': 300},
    {'user_id': 'U2', 'amount': 50}
]
"""

def top_users_by_transaction(transactions):
    user_totals = {}
    for transaction in transactions:
        user_id = transaction['user_id']
        amount = transaction['amount']
        if user_id in user_totals:
            user_totals[user_id] += amount
        else:
            user_totals[user_id] = amount
    sorted_users = sorted(user_totals.items(), key=lambda x: x[1], reverse=True)
    return sorted_users[:3]

transactions = [
    {'user_id': 'U1', 'amount': 100},
    {'user_id': 'U2', 'amount': 200},
    {'user_id': 'U1', 'amount': 150},
    {'user_id': 'U3', 'amount': 300},
    {'user_id': 'U2', 'amount': 50}
]
print(top_users_by_transaction(transactions))


