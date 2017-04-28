#Game

#Get the row,col size from user or set automatically

def GetSize():
    Size = input("Enter [row,column] size seperated by comma.\n")
    Size = Size.strip()
    Sizes = Size.split(",")
    try:
        row = int(Sizes[0])
        column = int(Sizes[1])
        if(row < 3 or column < 3):
            print("Must be atleast 3x3")
            GetSize()
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
    # print(Connections)


InitializeConnections()



def DrawWithConnections():
    SymbolsForKey = {}
    for node in Connections:
        if(SymbolsForKey.get(node) is None):
            SymbolsForKey[node] = connectable
        for edges in Connections[node]:
            SymbolsForKey[edges] = filled
    print(SymbolsForKey)
    output = ""
    for i in range(row*column):

        if(i%column==0):
            print(output)
            print()
            output = ""
        output+=(SymbolsForKey[i] + "\t\t")


Connections[1].append(2)
Connections[2].append(1)
Connections[2].append(3)
Connections[3].append(2)
Connections[0].append(4)
Connections[4].append(0)

print(Connections)

DrawWithConnections()


