class Types:
    KEYWORD_REAL = "REAL : "
    KEYWORD_INT = "INT : "
    KEYWORD_ID = "ID : "
    REAL = 0.0
    INT = 0
    LPAR = "LPAR"
    RPAR = "RPAR"
    ASG = "ASG"
    SUM = "SUM"
    DIV = "DIV"
    MIN = "MIN"
#Mines
    MUL = "MUL"
    POW = "POW"
    ID = "name"
##################################################
buffer = []
writer = ""
Result = []
##################################################
def main():
    State=0
    Index=0
    X = Types()
    with open("CalculatorConsol.txt") as file:
        for line in file:
            for ch in line:
                if ch != "\n":
                    buffer.append(ch)
            buffer.append(" ")
    file.close()
    print("Things inside my buffer : ")
    print(buffer)
    print("+-------------------------------------+")
    print("|-------------- Result ---------------|")
    print("+-------------------------------------+")
    N = len(buffer)
    while Index < N:
        while buffer[Index] != " ":
            if State == 0:
                if buffer[Index] == "0" or buffer[Index] == "1" or buffer[Index] == "2" or buffer[Index] == "3" or buffer[Index] == "4" or buffer[Index] == "5" or buffer[Index] == "6" or buffer[Index] == "7" or buffer[Index] == "8" or buffer[Index] == "9":
                    writer = buffer[Index]
                    State = 1
                elif buffer[Index] == "-":
                    writer = X.MIN
                    State = 100
                elif buffer[Index] == "A" or buffer[Index] == "B" or buffer[Index] == "C" or buffer[Index] == "D" or buffer[Index] == "E" or buffer[Index] == "F" or buffer[Index] == "X" or buffer[Index] == "Y" or buffer[Index] == "Z":
# My calculator has A,B,C,D,E,F,X,Y,Z as Variables. Engineering calculators are like this.
                    X.ID = buffer[Index]
                    writer = X.ID
                    State = 101
                elif buffer[Index] == "(":
                    writer = X.LPAR
                    State = 106
                elif buffer[Index] == ")":
                    writer = X.RPAR
                    State = 107
                elif buffer[Index] == "=":
                    writer = X.ASG
                    State = 105
                elif buffer[Index] == "/":
                    State = 102
                    writer = X.DIV
                elif buffer[Index] == "*":
                    writer = X.MUL
                    State = 103
                elif buffer[Index] == "^":
                    writer = X.POW
                    State = 104
                elif buffer[Index] == "+":
                    writer = X.SUM
                    State = 108
            elif State == 1:
                if buffer[Index] == "0" or buffer[Index] == "1" or buffer[Index] == "2" or buffer[Index] == "3" or buffer[Index] == "4" or buffer[Index] == "5" or buffer[Index] == "6" or buffer[Index] == "7" or buffer[Index] == "8" or buffer[Index] == "9":
                    State = 1
                    writer = writer + buffer[Index]
                    Index = Index + 1
                    if buffer[Index] != "0" or buffer[Index] != "1" or buffer[Index] != "2" or buffer[Index] != "3" or buffer[Index] != "4" or buffer[Index] != "5" or buffer[Index] != "6" or buffer[Index] != "7" or buffer[Index] != "8" or buffer[Index] != "9":
                        Result.append(X.KEYWORD_INT)
                        X.INT = int(writer[1:])
                        Result.append(X.INT)
                        Result.append(" ")
                        writer = ""
                        State = 0
                elif buffer[Index] == ".":
                    State = 2
                    writer = writer + buffer[Index]
                    Index = Index + 1
            elif State == 2:
                if buffer[Index] == "0" or buffer[Index] == "1" or buffer[Index] == "2" or buffer[Index] == "3" or buffer[Index] == "4" or buffer[Index] == "5" or buffer[Index] == "6" or buffer[Index] == "7" or buffer[Index] == "8" or buffer[Index] == "9":
                    State = 1
                    writer = writer + buffer[Index]
                    Index = Index + 1
                    if buffer[Index] != "0" or buffer[Index] != "1" or buffer[Index] != "2" or buffer[Index] != "3" or buffer[Index] != "4" or buffer[Index] != "5" or buffer[Index] != "6" or buffer[Index] != "7" or buffer[Index] != "8" or buffer[Index] != "9":
                        Result.append(X.KEYWORD_REAL)
                        X.REAL = float(writer[1:])
                        Result.append(X.REAL)
                        Result.append(" ")
                        writer = ""
                        State = 0
            elif State == 100:
                Result.append(writer)
                Result.append(" ")
                writer = ""
                Index = Index + 1
                State = 0
            elif State == 101:
                Result.append(X.KEYWORD_ID)
                Result.append(writer)
                Result.append(" ")
                writer = ""
                Index = Index + 1
                State = 0
            elif State == 102:
                Result.append(writer)
                Result.append(" ")
                writer = ""
                Index = Index + 1
                State = 0
            elif State == 103:
                Result.append(writer)
                Result.append(" ")
                writer = ""
                Index = Index + 1
                State = 0
            elif State == 104:
                Result.append(writer)
                Result.append(" ")
                writer = ""
                Index = Index + 1
                State = 0
            elif State == 105:
                Result.append(writer)
                Result.append(" ")
                writer = ""
                Index = Index + 1
                State = 0
            elif State == 106:
                Result.append(writer)
                Result.append(" ")
                writer = ""
                State = 0
                Index = Index + 1
            elif State == 107:
                Result.append(writer)
                Result.append(" ")
                writer = ""
                Index = Index + 1
                State = 0
            elif State == 108:
                Result.append(writer)
                Result.append(" ")
                writer = ""
                Index = Index + 1
                State = 0
            else:
                print("ERROR")
        Index = Index + 1
####################################################
def printResultAndWritOnFile():
    i=0
    f = open("Result.txt", "w")
    while i < len(Result):
        if Result[i] == " ":
            print("")
            f.write("\n")
        else:
            print(str(Result[i]),end="")
            f.write(str(Result[i]))
        i = i + 1
    f.close()
####################################################
if __name__ == "__main__":
    main()
    printResultAndWritOnFile()
    print("+-------------------------------------+")
    print("|------ End Of Lexical Analyzer ------|")
    print("+-------------------------------------+")
####################################################
