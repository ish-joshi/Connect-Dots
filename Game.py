#Game

#Get the row,col size from user or set automatically

def GetSize():
    Size = input("Enter [row,column] size seperated by comma.\n")
    Size = Size.strip()
    Sizes = Size.split(",")
    try:
        row = int(Sizes[0])
        column = int(Sizes[1])
        return [row,column]
    except Exception:
        print("Invalid input\n")
        GetSize()

Sizes = GetSize()
row = Sizes[0]
column = Sizes[1]

Board = []

connectable = "O"
filled = "X"

def InitializeBoard():
    for i in range(0, row):
        col = [connectable]*column
        Board.append(col)

def PrintBoard(board):
    for row in board:
        values = ""
        for column in row:
            values += (str(column) + "\t")

        print(values)
        print()

InitializeBoard()
PrintBoard(Board)

Connections = {}

def GetID(i, j):
    return column*i + j

def GetIndex(n):
    return [n//column, n%column]

def InitializeConnections():
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            Connections[GetID(i, j)] = []
    print(Connections)


InitializeConnections()

def DrawWithConnections():
    #1, -1 to count the fact that we're checking sides.
    for i in range(len(Board) - 1):
        output = ""
        previousConnected = False
        for j in range(len(Board[i]) - 1):
            connected = Connections.get(GetID(i, j))
            if GetID(i, j+1) in connected:
                output += (filled + "\t--\t")
                previousConnected = True
            else:
                output += (connectable + "\t  \t")
                previousConnected = False
        print(output)
        print()


Connections[1].append(2)

DrawWithConnections()


