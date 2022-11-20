import random

grid = """
|1|2|3|
|4|5|6|
|7|8|9|
"""

name = input("""Welcome to the Tic Tac Toe game! Your opponent will be the computer. Please enter your name to proceed:
""")



symbol = input("""
Hi """ + name + """, please pick whether you would like to be represented by 'X' or 'O' in this game. Your opponent will be represented by the other letter.
""")

while symbol != "X" and symbol != "O":
    symbol = input("""
Invalid entry. Please pick whether you would like to be represented by 'X' or 'O' in this game. Your opponent will be represented by the other letter.
""")
    if symbol == "X" or symbol == "O":
        break

bot_symbol = ""

if symbol == "X":
    bot_symbol = "O"
elif symbol == "O":
    bot_symbol = "X"

print("""
In this game, there are nine possible spaces within a three-by-three grid to place your mark. Each space has been assigned a digit from 1 to 9. The numbers follow a left-to-right, top-to-bottom pattern, like so:
|1|2|3|
|4|5|6|
|7|8|9|
""")

player_starts = input("""Would you like to start? Y/N:
""")

while player_starts != "Y" and player_starts != "N":
    player_starts = input("""
Invalid entry. Would you like to start? Y/N:
""")

    if player_starts == "Y" or player_starts == "N":
        break

while player_starts == "Y":
    print(grid)

    if any(i.isdigit() for i in grid) == False:
        print("It's a tie!")
        break

    play = input("""Please type the number at which you would like to place your mark. Type 'End' if you would like to end the game.
""")

    if play.title() == "End":
        break

    if int(play) > 9 or int(play) < 1 or str(play) not in grid:
        print("""
Invalid entry. Please make sure to pick one of the numbers visible on the Tic Tac Toe grid.
    """)
        continue

    if any(i.isdigit() for i in grid) == False:
        print("It's a tie!")
        break

    index = grid.index(str(play))        
    grid = grid[:index] + symbol + grid[index + 1:]
    print(grid)

    if grid[2] == grid [4] and grid[4] == grid[6]:
        print("You won! Congrats!")
        break
    elif grid[10] == grid[12] and grid[12] == grid[14]:
        print("You won! Congrats!")
        break
    elif grid[18] == grid[20] and grid[20] == grid[22]:
        print("You won! Congrats!")
        break
    elif grid[2] == grid[10] and grid[10] == grid[18]:
        print("You won! Congrats!")
        break
    elif grid[4] == grid[12] and grid[12] == grid[20]:
        print("You won! Congrats!")
        break
    elif grid[6] == grid[14] and grid[14] == grid[22]:
        print("You won! Congrats!")
        break
    elif grid[2] == grid[12] and grid[12] == grid[22]:
        print("You won! Congrats!")
        break
    elif grid[6] == grid[12] and grid[12] == grid[18]:
        print("You won! Congrats!")
        break
    
    
    
    print("Time for the computer's move...")

    numlist = []
    
    if int(play) == 1:
        numlist = [2, 4, 5]
    elif int(play) == 2:
        numlist = [1, 3, 4, 5, 6]
    elif int(play) == 3:
        numlist = [2, 5, 6]
    elif int(play) == 4:
        numlist = [1, 2, 5, 7, 8]
    elif int(play) == 5:
        numlist = [1, 2, 3, 4, 6, 7, 8, 9]
    elif int(play) == 6:
        numlist = [2, 3, 5, 8, 9]
    elif int(play) == 7:
        numlist = [4, 5, 8]
    elif int(play) == 8:
        numlist = [4, 5, 6, 7, 9]
    else:
        numlist = [5, 6, 8]
    
    for i in range(numlist[0], numlist[-1] + 1):
        if str(i) not in grid:
            if i in numlist:
                numlist.remove(i)
        else:
            numlist = numlist
    
    if numlist == []:
        for i in grid:
            if i.isdigit():
                numlist.append(int(i))

    if any(i.isdigit() for i in grid) == False:
        print("It's a tie!")
        break

    bot = str(random.choice(numlist))
    index = grid.index(bot)
    grid = grid[:index] + bot_symbol + grid[index + 1:]

    

    if grid[2] == grid [4] and grid[4] == grid[6]:
        print(grid)
        print("""
You lost! Sucks to suck!""")
        break
    elif grid[10] == grid[12] and grid[12] == grid[14]:
        print(grid)
        print("""
You lost! Sucks to suck!""")
        break
    elif grid[18] == grid[20] and grid[20] == grid[22]:
        print(grid)
        print("""
You lost! Sucks to suck!""")
        break
    elif grid[2] == grid[10] and grid[10] == grid[18]:
        print(grid)
        print("""
You lost! Sucks to suck!""")
        break
    elif grid[4] == grid[12] and grid[12] == grid[20]:
        print(grid)
        print("""
You lost! Sucks to suck!""")
        break
    elif grid[6] == grid[14] and grid[14] == grid[22]:
        print(grid)
        print("""
You lost! Sucks to suck!""")
        break
    elif grid[2] == grid[12] and grid[12] == grid[22]:
        print(grid)
        print("""
You lost! Sucks to suck!""")
        break
    elif grid[6] == grid[12] and grid[12] == grid[18]:
        print(grid)
        print("""
You lost! Sucks to suck!""")
        break

numlist = []

while player_starts == "N":
    
    if any(i.isdigit() for i in grid) == False:
        print("It's a tie!")
        break 

    print("""
Time for the computer's move...""")

    if numlist == []:
        numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    bot = str(random.choice(numlist))
    index = grid.index(bot)
    grid = grid[:index] + bot_symbol + grid[index + 1:]

    print(grid)

    if grid[2] == grid [4] and grid[4] == grid[6]:
        print("You lost! Sucks to suck!")
        break
    elif grid[10] == grid[12] and grid[12] == grid[14]:
        print("You lost! Sucks to suck!")
        break
    elif grid[18] == grid[20] and grid[20] == grid[22]:
        print("You lost! Sucks to suck!")
        break
    elif grid[2] == grid[10] and grid[10] == grid[18]:
        print("You lost! Sucks to suck!")
        break
    elif grid[4] == grid[12] and grid[12] == grid[20]:
        print("You lost! Sucks to suck!")
        break
    elif grid[6] == grid[14] and grid[14] == grid[22]:
        print("You lost! Sucks to suck!")
        break
    elif grid[2] == grid[12] and grid[12] == grid[22]:
        print("You lost! Sucks to suck!")
        break
    elif grid[6] == grid[12] and grid[12] == grid[18]:
        print("You lost! Sucks to suck!")
        break

    if any(i.isdigit() for i in grid) == False:
        print("It's a tie!")
        break

    play = input("""Please pick the number at which you would like to place your mark. Type 'End' if you would like to end the game.
""")

    if play.title() == "End":
        break
    
    while int(play) > 9 or int(play) < 1 or str(play) not in grid:
        play = input("""
Invalid entry. Please be sure to pick one of the numbers visible in the grid. Type 'End' if you would like to end the game.
""")
        if int(play) >= 1 and int(play) <= 9 and str(play) in grid:
            pass
        elif play.title() == "End":
            break
    
    if any(i.isdigit() for i in grid) == False:
        print("It's a tie!")
        break

    index = grid.index(str(play))        
    grid = grid[:index] + symbol + grid[index + 1:]

    print(grid)

    if grid[2] == grid [4] and grid[4] == grid[6]:
        print("You won! Congrats!")
        break
    elif grid[10] == grid[12] and grid[12] == grid[14]:
        print("You won! Congrats!")
        break
    elif grid[18] == grid[20] and grid[20] == grid[22]:
        print("You won! Congrats!")
        break
    elif grid[2] == grid[10] and grid[10] == grid[18]:
        print("You won! Congrats!")
        break
    elif grid[4] == grid[12] and grid[12] == grid[20]:
        print("You won! Congrats!")
        break
    elif grid[6] == grid[14] and grid[14] == grid[22]:
        print("You won! Congrats!")
        break
    elif grid[2] == grid[12] and grid[12] == grid[22]:
        print("You won! Congrats!")
        break
    elif grid[6] == grid[12] and grid[12] == grid[18]:
        print("You won! Congrats!")
        break

    numlist = []
    
    if int(play) == 1:
        numlist = [2, 4, 5]
    elif int(play) == 2:
        numlist = [1, 3, 4, 5, 6]
    elif int(play) == 3:
        numlist = [2, 5, 6]
    elif int(play) == 4:
        numlist = [1, 2, 5, 7, 8]
    elif int(play) == 5:
        numlist = [1, 2, 3, 4, 6, 7, 8, 9]
    elif int(play) == 6:
        numlist = [2, 3, 5, 8, 9]
    elif int(play) == 7:
        numlist = [4, 5, 8]
    elif int(play) == 8:
        numlist = [4, 5, 6, 7, 9]
    else:
        numlist = [5, 6, 8]
    
    for i in range(numlist[0], numlist[-1] + 1):
        if str(i) not in grid:
            if i in numlist:
                numlist.remove(i)
        else:
            numlist = numlist
    
    if numlist == []:
        for i in grid:
            if i.isdigit():
                numlist.append(int(i))