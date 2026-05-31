"""
A junior magician has picked a secret number. 
He has hidden it in a variable named secret_number. 
He wants everyone who runs his program to play the 
Guess the secret number game, 
and guess what number he has picked for them. 
Those who don't guess the number will be stuck in an endless loop forever! 
Unfortunately, he does not know how to complete the code.
"""

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

player_name = input("Who wants to play this game, come up on stage? Tell me your name: ")

while True:
    guess_number = int(input("Guess the secret number: "))

    if guess_number == secret_number:
        print(f"Congratulations, {player_name}! You are free now.")
        break
    else:
        print(f"Ha ha, {player_name}! You're stuck in my loop!")