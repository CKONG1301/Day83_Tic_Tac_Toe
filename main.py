import random

print('''\
888   d8b        888                   888
888   Y8P        888                   888
888              888                   888
888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.
888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b
888   888888     888   .d888888888     888   888  88888888888
Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.
 "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888
''')

def check_result(result):
    for n in range(0, 3):
        if result[n*3] == result[n*3+1] and result[n*3+1] == result[n*3+2]:
            return result[n*3]
    for n in range(0, 3):
        if result[n] == result[n+3] and result[n+3] == result[n+6]:
            return result[n]
    if result[0] == result[4] and result[4] == result[8]:
        return result[0]
    if result[2] == result[4] and result[4] == result[6]:
        return result[2]
    return 'N'

def display_result(result):
    print(f"\t{result[0]}\t|\t{result[1]}\t|\t{result[2]}")
    print("-------------------------")
    print(f"\t{result[3]}\t|\t{result[4]}\t|\t{result[5]}")
    print("-------------------------")
    print(f"\t{result[6]}\t|\t{result[7]}\t|\t{result[8]}\n")
    
def setup_result():
    result = ['1']
    for n in range (2, 10):
        result.append(str(n))
    return result

result = setup_result()

is_continue = True
n = 1
while is_continue:
    display_result(result)
    user_choice = input("Enter Your Location Choice (1~9): ")
    # Verify user_choice is between 1~9 and not selected yet.
    if not user_choice.isnumeric():
        continue
    if user_choice < '0' or user_choice > '9':
        continue
    user_choice = int(user_choice)
    if not result[user_choice - 1].isnumeric():
        continue
        
    # Secure the tictactoe space
    result[user_choice - 1] = 'X'
    
    # Get computer_choice not selected yet.
    computer_choice = user_choice
    while not result[computer_choice-1].isnumeric():
        computer_choice = random.randint(1, 9)
    result[computer_choice-1] = 'O'
    answer = check_result(result)
    
    if answer == 'N':
        n += 1
        # no winner
        if n < 5:
            continue
    
    display_result(result)
    # Someone win or no more choice
    if answer == 'X':
        print("You Win!!")
    elif answer == 'O':
        print("You Lose..")
    else:
        print("Draw.")

    if input('Another game? (Y/N) ').upper() == 'Y':
        n = 1
        result = setup_result()
    else:
        is_continue = False

        