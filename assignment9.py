
def printGrid(rows):
    for i in rows:
        print(i)


def naturalNumberYield(question: str,  rangeMin: int = 0, rangeMax: int = 15) -> int:
    while True:
        i = input(question)
        try:
            assert int(i) >= rangeMin and int(i) <= rangeMax
        except:
            print("ERROR, your number is invalid: ")
            continue
        else:
            return int(i)

def shipMovement(board, missilesRemaining) -> list:
    playerOption = ""
    while True:
        playerOption = input("Do you want to move left, right, or shoot?: ").lower()
        if playerOption == "left" or playerOption == "right" or playerOption == "shoot":
            break
        else:
            print("Error, invalid input (left, right, shoot): ")
    if playerOption == "left":
        location = board[len(board) - 1].index('S')
        for i, s in enumerate(board[len(board) - 1]):
            board[len(board) - 1][i] = ' '
        newLocation = location - 1
        if newLocation < 0: 
            newLocation = location
        board[len(board) - 1][newLocation] = "S"
    if playerOption == "right":
        location = board[len(board) - 1].index('S')
        for i, s in enumerate(board[len(board) - 1]):
            board[len(board) - 1][i] = ' '
        newLocation = location + 1
        if newLocation > len(board[len(board) - 1]) - 1:
            newLocation = location
        board[len(board) - 1][newLocation] = "S"
    if playerOption == "shoot":
        if missilesRemaining > 0:
            missilesRemaining -= 1
            location = board[len(board) - 1].index('S')
            board[len(board) - 2][location] = "^"
            print("Player one now has " + str(missilesRemaining) + " missiles remaining.")
        else:
            print("You can't fire, you're out of missiles.")

    return [board, missilesRemaining]

def cleanseRockets(s: list):
    for i, row in enumerate(s):
        if '^' in row:
            if i == 0: 
                for iii, e in enumerate(row):
                    if e == '^':
                        row[iii] = ' '
            else:
                indeces = []
                for ii, e in enumerate(row):
                    if e == '^':
                        indeces.append(ii)
                        row[ii] = ' '
                for rocket in indeces:
                    if s[i - 1][rocket] == "U":
                        return "YOU WIN!!!:)"
                    s[i - 1][rocket] = '^'
    return s

def main():
    print("SPACE INVADERS")
    rows = naturalNumberYield("How many rows?: ", 4)
    columns = naturalNumberYield("How many columns?: ", 4)
    s = [] * rows
    for i in range(rows):
        s.append([' '] * columns)
    print("The blank board has been created.")
    printGrid(s)
    shipCol = naturalNumberYield("Where will you put your ship? Columns 0 through " + str(columns - 1) + ": ", 0, columns - 1)
    s[len(s) - 1][shipCol] = "S"
    printGrid(s)
    ufoCol = naturalNumberYield("Where will you put your UFO? Columns 0 through " + str(columns - 1) + ": ", 0, columns - 1)
    s[0][ufoCol] = "U"
    printGrid(s)
    missilesRemaining = 20
    while True:
        s = cleanseRockets(s)
        if isinstance(s, str):
            print(s)
            break
        shipMovementResults = shipMovement(s, missilesRemaining)
        s = shipMovementResults[0]
        missilesRemaining = shipMovementResults[1]
        printGrid(s)

while True:
    main()