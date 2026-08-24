import random
import json
import time
print("________________")
print("    MENU     ")
print("_________________")
print("LET'S HAVE SOME FUN ")
print("_______________________")
print("This are the games:")
print(" 1.CHOICE GAME \n 2.QUIZ \n 3.SLOT MACHINE \n 4.TIK-TAK-TOE\n5.Random lader\n6.Rock,Paper,Scissor")
op=int(input("\tEnter your choice:"))

if op==1:
    print("\nHello! Player let's play a game of CHOICES!\n")

    player_choice=input("Will you play a game of CHOICES! (yes/no): ").lower()

    if player_choice=="yes":
        print("Great! Let's play!")
        print("this will be a game of CHOICES where your Choices will take you near the 'TREASURE' or to your 'DEATH'!,Then shall we began?\n")
        #HEAR START OF THE GAME
        print("You have walked as your grandfather told you ,but you know the half way only from know on ypu have to chose your path wisely!\n")
        direction=input("Know you have two different ways to go 'WHAT YOU WILL YOUR CHOICE' (left/right): ").lower()
        if direction=="left":
            print("You have chose has saved your life!, But your far away from the treasure!!!!!")
            print()
            print("The end of this path you have a 'bridge ON THE RIVER'\n")
            way=input("How do you want to cross the IT? (SWIM/WALK): \n").lower()
            if way=="swim":
                print("Yu have crossed the bridge, DONT BE HAPPY SOON! You have many ways to Die!☠️☠️☠️👹\n")
                print("After crossing the bridge you have two 'GATES' FRONT of you!!!🚪🚪\n")
                print("ONE GATE IS FULL OF TRAPES AND OTHER GATE HAVE A LION (which has not eaten for 4 weeks),,, THIS ARE THE INFORMATION ON THE GATES\n")
                gate=input("Which gate will you choose? (TRAPS gate/LION gate): \n").lower()
                if gate=="traps gate":
                    print("You have chosen the wrong gate! You have fallen into a pit of spikes and died!💀☠️\n")
                elif gate=="lion gate":
                    print("YOUR CHOICES ARE GOING incredible! You have chosen the right gate!,BUT LONG WAY TO GO! FOR THE TREASURE!💰💰💰\n")
                    print("HEAR IS  A BONUS GIFT FOR YOU! ")
                    bonus=input("Do you want to take the bonus gift, THE bonus IS  A KNIFE, YOU WANT TO TAKE IT OR NOT?(yes/no):\n ").lower()
                    if bonus=="yes":
                        print("you have a 'KNIFE' now\n")
                        print("But end of the path you swa a soldier with a gun.\n")
                        solider1=input("What will you do? (ATTACK/ESCAPE):\n ").lower()
                        if solider1=="attack":
                            print("You have attacked the soldier with your knife and killed,But solider swa you first and shoot you down!🔫🔫🤺🤺\n")
                        elif solider1=="escape":
                            print("You have tried to escape from the soldier but he was faster than you and shoot you down!🔫🔫🤺🤺\n")
                        else:
                            print("Invalid choice. You have been caught by the soldier and died!☠️💀\n")
                    elif bonus=="no":
                        print("But end of the path you swa a soldier with a gun.\n")
                        solider2=input("What will you do? (ATTACK/sneak): \n").lower()
                        if solider2=="attack":
                            print("You have attacked the soldier with your bare hands and killed,But solider swa you first and shoot you down!🔫🔫🤺🤺\n")
                        elif solider2=="sneak":
                            print("You have tried to sneak past the soldier and you have successfully sneaked past the soldier!! \n")
                            print("You have found the treasure!💰💰💰\n")
                            treasure=input("Do you want to take the treasure or leave it? (TAKE/LEAVE): \n").lower()
                            if treasure=="take":
                                print("You have taken the treasure , but it was a trap! you killed by the poison on the treasure!💀☠️")
                            elif treasure=="leave":
                                print("You have left the treasure , but you see the real treasure behind the soldier and you have successfully taken the treasure!💰💰💰\n")
                                print("\t\tCONGRATULATIONS! YOU HAVE WON THE GAME!🎉🎉🎉\t\n")
                                print("\t\tTHANK YOU FOR PLAYING THE GAME! HOPE YOU ENJOYED IT!😊😊😊\t\n")
                                print("\t\tBYE! HAVE A NICE DAY!👋👋👋\t\n")
                            else:
                                print("Invalid choice. You have been caught by the soldier and died!☠️💀")
                        else:
                            print("Invalid choice. You have been caught by the soldier and died!☠️💀")

            elif way=="walk":
                print("You have crossed the bridge successfully!,but killed by a soldier who was guarding the bridge!🤺🤺☠️💀")
            else:
                print("You CHOSE THE WRONG PATH! You have fallen into a pit of spikes and died!💀☠️")
        elif direction=="right":
            print("You CHOSE THE WRONG PATH! You have fallen into a pit of spikes and died!💀☠️")
        else:
            print("Invalid choice. Please enter 'left' or 'right'.")
    else:
        print("Okay, maybe next time!")

elif op==2:
    def load_question():
        with open("questions.json", "r") as f:
            questions=json.load(f)["questions"]
        return questions

    def ask_question(questions):
        print(questions["question"])
        for i ,option in enumerate(questions["options"]):
            print(str(i+1)+".", option)

        number=int(input("enter your choice no :"))
        if number<1 or number>len(questions["options"]):
            print("Invalid choice:!!!!")
            return False

        correct=questions["options"][number-1]==questions["answer"]
        return correct

    def random_question(question,number_question):
        if number_question>len(questions):
            number_question=len(questions)
        random_question=random.sample(questions,number_question)
        return random_question

    questions=load_question()
    total_questions=int(input("enter the no. of question"))
    random_question=random_question(questions,total_questions)
    correct=0
    start_time=time.time()

    for question in random_question:
        is_correct=ask_question(question)
        if is_correct:
            correct+=1
        print("------------------------")


    completed_time=time.time()-start_time
    print("Summary")
    print("total Questions:",total_questions)
    print("Correct Answer",correct)
    print("Score: ",str(round((correct/total_questions)*100,2)),"%")
    print("Time: ",round(completed_time,2),"sec")

elif op==3:
    MAX_LINES = 3
    MAX_BET = 100
    MIN_BET = 1

    ROWS = 3
    COLS = 3

    symbol_count = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8
    }

    symbol_value = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2
    }


    def check_winnings(columns, lines, bet, values):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)

        return winnings, winning_lines


    def get_slot_machine_spin(rows, cols, symbols):
        all_symbols = []
        for symbol, symbol_count in symbols.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)

        columns = []
        for _ in range(cols):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)

            columns.append(column)

        return columns


    def print_slot_machine(columns):
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], end=" | ")
                else:
                    print(column[row], end="")

            print()


    def deposit():
        while True:
            amount = input("What would you like to deposit? $")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("Amount must be greater than 0.")
            else:
                print("Please enter a number.")

        return amount


    def get_number_of_lines():
        while True:
            lines = input(
                "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Enter a valid number of lines.")
            else:
                print("Please enter a number.")

        return lines


    def get_bet():
        while True:
            amount = input("What would you like to bet on each line? $")
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
            else:
                print("Please enter a number.")

        return amount


    def spin(balance):
        lines = get_number_of_lines()
        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > balance:
                print(
                    f"You do not have enough to bet that amount, your current balance is: ${balance}")
            else:
                break

        print(
            f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        print(f"You won ${winnings}.")
        print(f"You won on lines:", *winning_lines)
        return winnings - total_bet


    def main():
        balance = deposit()
        while True:
            print(f"Current balance is ${balance}")
            answer = input("Press enter to play (q to quit).")
            if answer == "q":
                break
            balance += spin(balance)

        print(f"You left with ${balance}")


    main()

elif op==4:
    def print_board(board):
        for i, row in enumerate(board):
            row_str = " | ".join(value if value != "" else " " for value in row)
        print(row_str)
        if i != len(board) - 1:
            print("-" * (len(row) * 4 - 3))  # dynamic separator


    def get_move(turn, board):
        while True:
            try:
                row = int(input("Enter the row (1-3): "))
                col = int(input("Enter the col (1-3): "))
            except ValueError:
                print("Please enter numbers only!")
                continue

            if row < 1 or row > len(board):
                print("Invalid row, try again.")
            elif col < 1 or col > len(board[row - 1]):
                print("Invalid column, try again.")
            elif board[row - 1][col - 1] != "":
                print("Invalid move, already taken.")
            else:
                board[row - 1][col - 1] = turn
                break


    def check_winner(board):
        # Rows
        for row in board:
            if row[0] == row[1] == row[2] != "":
                return row[0]
        # Columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                return board[0][col]
        # Diagonals
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]
        return None


    def is_full(board):
        return all(cell != "" for row in board for cell in row)


    # Game loop
    board = [["", "", ""],
            ["", "", ""],
            ["", "", ""]]

    turn = "X"
    while True:
        print_board(board)
        get_move(turn, board)

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        # Switch turns
        turn = "O" if turn == "X" else "X"

elif op==5:

    MAX = 50
    stack = [None] * MAX
    top = -1

    def push(value):
        global top
        if top == MAX - 1:
            print("Game Over (stack full)")
        else:
            top += 1
            stack[top] = value

    def pop():
        global top
        if top == -1:
            print("Stack is empty")
        else:
            value = stack[top]
            stack[top] = None
            top -= 1
            return value

    def display():
        if top == -1:
            print("No dice rolls yet")
        else:
            print("Dice roll history:", stack[:top+1])

    def roll_dice():
        return random.randint(1, 6)

    # Player position
    position = 0

    while True:
        print("\n--- Dice Game Menu ---")
        print("1. Roll Dice")
        print("2. Show Roll History")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            dice = roll_dice()
            print("Dice:", dice)
            push(dice)
            position += dice
            if position > 50:
                position = 50
            print("Player position:", position)

            if position == 50:
                print("🎉 You reached 50! You win!")
                break

        elif choice == "2":
            display()

        elif choice == "3":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Try again.")

elif op==6:
    you_win=0
    computer_win=0

    op=["rock","paper","scissor"]

    while True:
        user=input("Enter the your option rock||paper||scissor or quit(q): ").lower()
        if user=="q":
            break
        if user not in op:
            continue

        random_pick=random.randint(0,2)
        com_pick=op[random_pick]
        print("computer pick",com_pick +".")

        if user=="rock" and com_pick=="scissor":
            print("You Win!!!!\n")
            you_win+=1
        elif user=="paper" and com_pick=="rock":
            print("You Win!!!!")
            you_win+=1
        elif user=="scissor" and com_pick=="paper":
            print("You Win!!!!")
            you_win+=1
        else:
            print("You loss!!")
            computer_win+=1

    print("You have wine:",you_win ,"times.")
    print("computer have wine:",computer_win ,"times.")
    print("Thanks for playing")
        
