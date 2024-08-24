score = 0
name = input("Welcome to GC mini golf! What is your name? ")
holes = int(input(f'Hi, {name}! Would you like to play 3 or 6 holes? '))

# Gets score for each hole
if holes == 3:
    par = 9
    score += int(input("How many putts for hole 1?(par:3) "))
    score += int(input("How many putts for hole 2?(par:3) "))
    score += int(input("How many putts for hole 3?(par:3) "))
elif holes == 6:
    par = 18
    score += int(input("How many putts for hole 1?(par:3) "))
    score += int(input("How many putts for hole 2?(par:3) "))
    score += int(input("How many putts for hole 3?(par:3) "))
    score += int(input("How many putts for hole 4?(par:3) "))
    score += int(input("How many putts for hole 5?(par:3) "))
    score += int(input("How many putts for hole 6?(par:3) "))
else:
    print(f'{holes} is an invalid number')

# Caluculates total score
if score > par:
    total_score = score - par
    print(f'Nice try,{name}... Your total score was: +{total_score}')
elif score < par:
    total_score = par - score
    print(f'Great job,{name}! Your total score was: -{total_score}')
else:
    print(f'Good game,{name}. Your total score was: 0')