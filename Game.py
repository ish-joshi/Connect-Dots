#Game

#Get the row,col size from user or set automatically
def IsInRange(num, mi, ma):
    return num <= ma and num >= mi

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
filled = "*"
taken = "#"

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
# PrintBoard(Board)

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
    # print(Connections)
    SymbolsForKey = {}
    for node in Connections:
        if(SymbolsForKey.get(node) is None):
            SymbolsForKey[node] = connectable
        for edges in Connections[node]:
            SymbolsForKey[edges] = filled

    output = ""
    vertical = ""
    for i in range(row*column):
        connections = Connections[i]
        if (i % column == 0):
            # output += "\n"
            print(output)
            print(vertical)
            output, vertical = "",""
        if(i+1 in connections):
            if(i%column == column-1):
                output += (filled)
            else:
                output += (filled + "\t--\t")
        else:
            if(i-1 in connections or i-column in connections or i+column in connections):
                output += (filled + "\t  \t")
            else:
                output += (connectable + "\t  \t")
        if(i+column in connections):
            vertical += "|\t  \t"
        else:
            vertical += " \t  \t"

    print(output)
    print()
    # print(SymbolsForKey)
    # output = ""
    #
    # output += "\t\t"
    # for i in range(column):
    #     output += (str(i) + "\t\t")
    #
    #
    # for i in range(row*column):
    #     if(i%column==0):
    #         print(output)
    #         print()
    #         output = ""
    #         output += (str(i//column) + "\t\t")
    #
    #     output+=(SymbolsForKey[i] + "\t\t")
    # print(output)
    # print()


# Connections[1].append(2)
# Connections[2].append(1)
# Connections[2].append(3)
# Connections[3].append(2)
# Connections[0].append(4)
# Connections[4].append(0)

# print(Connections)

# DrawWithConnections()

players = []


def IsValidConnection(id1, id2):
    if(id1 > id2):
        temp = id1
        id1 = id2
        id2 = temp



    id1 = GetIndex(id1)
    id2 = GetIndex(id2)

    print(id1, id2)
    return (id2[1] - id1[1] == 1 and id2[0] == id1[0]) or (id2[0] - id1[0] == 1 and id2[1] == id1[1])

scores = []


def Scored(i):
    print(i)
    print(Connections)
    #check left top
    high = row*column
    connectioni = Connections.get(i)

    if(IsInRange(i-column, 0, high)):
        connectionIminusCol = Connections.get(i-column)
    else:
        connectionIminusCol = None
    if(IsInRange(i - column - 1, 0, high)):
        connectionIminusColminusOne = Connections.get(i-column+1)
    else:
        connectionIminusColminusOne = None
    if (IsInRange(i - column + 1, 0, high)):
        connectionIminusColplusOne = Connections.get(i - column + 1)
    else:
        connectionIminusColplusOne = None


    if (IsInRange(i + column, 0, high)):
        connectionIplusCol = Connections.get(i - column)
    else:
        connectionIplusCol = None

    if (IsInRange(i + column - 1, 0, high)):
        connectionIplusColminusOne = Connections.get(i - column + 1)
    else:
        connectionIplusColminusOne = None
    if (IsInRange(i + column + 1, 0, high)):
        connectionIplusColplusOne = Connections.get(i - column + 1)
    else:
        connectionIplusColplusOne = None

    try:
        if(connectioni is not None and connectionIminusCol is not None and connectionIminusColminusOne is not None):
            if(i-1 in connectioni and i-column in connectioni and i-column-1 in connectionIminusCol and i-1 in connectionIminusColminusOne):
                return True
        elif(connectioni is not None and connectionIminusCol is not None and connectionIminusColplusOne is not None):
            if (i + 1 in connectioni and i - column in connectioni and i - column + 1 in connectionIminusCol and i + 1 in connectionIminusColplusOne):
                return True
        elif(connectioni is not None and connectionIplusCol is not None and connectionIplusColminusOne is not None):
            if(i-1 in connectioni and i+column in connectioni and i+column-1 in connectionIplusCol and i-1 in connectionIplusColminusOne):
                return True
        elif(connectioni is not None and connectionIplusCol is not None and connectionIplusColplusOne is not None):
            if(i + 1 in connectioni and i + column in connectioni and i + column + 1 in connectionIplusCol and i + 1 in connectionIplusColplusOne):
                return True
        else:
            return False
    except Exception as e:
        print(e)


def GameControl(players, scores):
    turn = 0
    Ended = False

    while not Ended:
        Valid = False

        userinput = input("Make a choice, [row:col, row:col] " + players[turn % len(players)] + "\n")
        if (userinput.lower() == 'quit'):
            print("Game ended\n")
            Ended = True
            break

        r1, c1, r2, c2 = 0, 0, 0, 0

        try:
            userinput = userinput.split(",")
            coordinate1 = userinput[0].split(":")
            r1 = int(coordinate1[0])
            c1 = int(coordinate1[1])
            coordinate2 = userinput[1].split(":")
            r2 = int(coordinate2[0])
            c2 = int(coordinate2[1])

            id1 = GetID(r1, c1)
            id2 = GetID(r2, c2)

            if (IsValidConnection(id1, id2)):

                Connections[GetID(r1, c1)].append(GetID(r2, c2))
                Connections[GetID(r2, c2)].append(GetID(r1, c1))
                DrawWithConnections()

                point = Scored(id2)
                print(point)
                print(scores, turn)

                if(not point or None):
                    Valid = True
                else:
                    scores[turn] += 1
                    Valid = False
            else:
                print("Invalid connection :(\n")

            if(Valid):
                turn += 1
        except Exception as e:
            print(e)
            print("An error in your input prevented calculation. ")



def SetupGame():
    players = input("Enter player names seperated by comma [Katie, Ishan]\n")
    players = players.split(",")
    scores = [0]*len(players)

    for player in players:
        print("Welcome, "+player)

    DrawWithConnections()

    GameControl(players, scores)




SetupGame()