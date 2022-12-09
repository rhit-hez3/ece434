size = int(input("size of board: "))

penX = int(input("pen's x coordinate (0-indexed): "))
while (penX >= size):
    print("x coordinate too big!")
    penX = int(input("x coordinate again: "))

penY = int(input("pen's y coordinate (0-indexed): "))
while (penY >= size):
    print("y coordinate too big!")
    penY = int(input("y coordinate again: "))

history = [[penX, penY]]

def print_board(history, clearCalled):
    # set up initial board
    board = [[]] * (size + 1)
    board[0] = [' ', ' ', ' ']
    for k in range(0, size):
        board[0].append(k)
        board[k + 1] = [k, ':', ' ']
        for j in range(0, size):
            board[k + 1].append(' ')

    if clearCalled == False:
        if (len(history) > 1):
            for a in range(0, len(history) - 1):
                board[history[a][1]][history[a][0] + 2] = 'x'
            
            board[history[len(history)-1][1]][history[len(history)-1][0] + 2] = 'o'
        else:
            board[history[0][1]][history[0][0] + 2] = 'o'
    else:
        for a in range(0, len(history)):
            board[history[a][1]][history[a][0] + 2] = 'x'
    
    for k in board:
        print(' '.join(str(e) for e in k))

clearCalled = False

# handle strokes
while(1):
    print_board(history, clearCalled)
    penMove = input("where to move pen (up, down, left, right, undo, clear, exit): ")
    match penMove:
        case "up":
            clearCalled = False
            if penY - 1 <= 0:
                print('wrong move, boddy!')
            else: 
                penY -= 1
                history.append([penX, penY])
        case "down":
            clearCalled = False
            if penY + 1 > size:
                print('wrong move, boddy!')
            else: 
                penY += 1
                history.append([penX, penY])
        case "left":
            clearCalled = False
            if penX - 1 <= 0:
                print('wrong move, boddy!')
            else: 
                penX -= 1
                history.append([penX, penY])
        case "right":
            clearCalled = False
            if penX + 1 > size:
                print('wrong move, boddy!')
            else: 
                penX += 1
                history.append([penX, penY])
        case "undo":
            clearCalled = False
            if (len(history) > 1):
                history.pop()
                penX = history[len(history)-1][0]
                penY = history[len(history)-1][1]
            else:
                print("nothing to clear!")
        case "clear":
            clearCalled = True
            # clears all the current pen locations in history table
            history = [e for e in history if e != [penX, penY]]
        case "exit": 
            break

    print("current pen posistion: " + str(penX) + ", " + str(penY))
                