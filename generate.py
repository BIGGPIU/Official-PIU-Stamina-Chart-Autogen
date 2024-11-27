import os
from random import randint
col1 = ["..X..\n","...X.\n","....X\n"] # valid patterns for the first column
col2 = ["..X..\n","...X.\n","....X\n"] # valid patterns for the second column
col3L = [".X...\n","X....\n"]
col3R = ["....X\n","....X\n"]
col4 = ["..X..\n",".X...\n","X....\n"]
col5 = ["..X..\n",".X...\n","X....\n"]
# .X...  
# ..X..
# X..
#
def main():
    x = os.listdir("./Charts/")
    print(x)
    for i in x:
        print(GenerateChart(i))

def col3context(lastcontext:str) -> str:
    if lastcontext == ".X...\n" or lastcontext == "X....\n":
        y = randint(0,len(col3L)-1)
        print(lastcontext)
        print(col3L[y])
        return col3L[y]
    else:
        y = randint(0,len(col3R)-1)
        print(lastcontext)
        print("..X..\n")
        print(col3R[y])
        return col3R[y]
    



def GenerateChart(file):
    context = []
    newchart = ""
    info = ""
    previous = 0
    with (open(f"./Charts/{file}","r+")) as f:
        while True:
            x = f.readline()
            if len(x) == 0:
                break
            if x[0] == ":":
                info += x
            if x[0] == ".":
                if len(context) == 0:
                    newchart += "X....\n"
                    context.append("X....")
                else:
                    if context[-1][0] == "X":
                        y = randint(0,len(col1)-1)
                        if y == previous:
                            y = randint(0,len(col1)-1)
                        newchart += col1[y]
                        context.append(col1[y])
                    elif context[-1][1] == "X":
                        y = randint(0,len(col2)-1)
                        if y == previous:
                            y = randint(0,len(col2)-1)
                        newchart += col2[y]
                        context.append(col2[y])
                    elif context[-1][2] == "X":
                        y = col3context(context[-2])
                        newchart += y
                        context.append(y)
                    elif context[-1][3] == "X":
                        y = randint(0,len(col4)-1)
                        if y == previous:
                            y = randint(0,len(col4)-1)
                        newchart += col4[y]
                        context.append(col4[y])
                    elif context[-1][4] == "X":
                        y = randint(0,len(col5)-1)
                        if y == previous:
                            y = randint(0,len(col5)-1)
                        newchart += col5[y]
                        context.append(col5[y])
    with open(f"./Completed/{file}","w") as f:
        f.write(info)
        f.write(newchart)
    return 0



                

if __name__ == "__main__":
    main()