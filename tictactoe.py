import tkinter
from random import *

def threeInARow(symbol, realMove):
    if grid[1] == symbol and grid[2] == symbol and grid[3] == symbol:
        if realMove == True: changeButtonColors(b1, b2, b3)
        return True
    elif grid[4] == symbol and grid[5] == symbol and grid[6] == symbol:
        if realMove == True:  changeButtonColors(b4, b5, b6)
        return True
    elif grid[7] == symbol and grid[8] == symbol and grid[9] == symbol:
        if realMove == True:  changeButtonColors(b7, b8, b9)
        return True
    elif grid[1] == symbol and grid[4] == symbol and grid[7] == symbol:
        if realMove == True: changeButtonColors(b1, b4, b7)
        return True
    elif grid[2] == symbol and grid[5] == symbol and grid[8] == symbol:
        if realMove == True: changeButtonColors(b2, b5, b8)
        return True
    elif grid[3] == symbol and grid[6] == symbol and grid[9] == symbol:
        if realMove == True:  changeButtonColors(b3, b6, b9)
        return True
    elif grid[1] == symbol and grid[5] == symbol and grid[9] == symbol:
        if realMove == True: changeButtonColors(b1, b5, b9)
        return True
    elif grid[7] == symbol and grid[5] == symbol and grid[3] == symbol:
        if realMove == True: changeButtonColors(b7, b5, b3)
        return True
    else:
        return False

def changeButtonColors(bi, bj, bk):
    bi["fg"] = "red"
    bj["fg"] = "red"
    bk["fg"] = "red"
    grid[0] = 1

def checkTie():
    for i in range(1, 10):
        if grid[i] == i:
            return False   
    return True
    
def setSymbolOnClick(button, index):
    if(grid[0] == 0):
        ret = setSymbol('X', button, index)
    if(grid[0] == 0 and ret == True):
        ai()

def ai():
    flag = 0
    difficulty = randint(0, 10)
    if difficulty <= 6:
        for i in range(1,10):
            if grid[i] == i:
                grid[i] = 'O'
                if threeInARow('O', False):
                    setAiSymbol(i)
                    flag = 1
                    break
                else: grid[i] = i
                
        if flag == 0:        
            for i in range(1,10):
                if grid[i] == i:
                    grid[i] = 'X'
                    if threeInARow('X', False):
                        setAiSymbol(i)
                        flag = 1
                        break
                    else: grid[i] = i
                    
        if flag == 0:
            for i in range(1, 10, 2):
                r = randrange(1, 10, 2)
                if grid[r] == r:
                    setAiSymbol(r)
                    flag = 1
                    break
                       
    while(flag == 0):
        r = randint(1, 10)
        if setAiSymbol(r):
            break

def setAiSymbol(r):
    if r == 1:
        return setSymbol('O', b1, 1)
    elif r == 2:
        return setSymbol('O', b2, 2)
    elif r == 3:
        return setSymbol('O', b3, 3)
    elif r == 4:
        return setSymbol('O', b4, 4)
    elif r == 5:
        return setSymbol('O', b5, 5)
    elif r == 6:
        return setSymbol('O', b6, 6)
    elif r == 7:
        return setSymbol('O', b7, 7)
    elif r == 8:
        return setSymbol('O', b8, 8)
    elif r == 9:
        return setSymbol('O', b9, 9)
    
def setSymbol(symbol, button, index):
    if button["text"] == "":
        button["text"] = symbol
        button["relief"] = "sunken"
        grid[index] = symbol
        threeInARow(symbol, True)
        return True
    elif checkTie() == True:
        return True
    return False

def resetAll():
    for i in range (0, 10): grid[i] = i
    resetButton(b1)
    resetButton(b2)
    resetButton(b3)
    resetButton(b4)
    resetButton(b5)
    resetButton(b6)
    resetButton(b7)
    resetButton(b8)
    resetButton(b9)
    playOrder = randint(0, 1)
    if playOrder == 1: ai()

def resetButton(button):
    button["text"] = ""
    button["fg"] = "black"
    button["relief"] = "raised"
    
def main():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, grid
    grid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    master = tkinter.Tk()
    master.title("tic-tac-toe")
    b1 = tkinter.Button(width = 5, height = 2, text = "", font = "bold", command = lambda: setSymbolOnClick(b1, 1))
    b2 = tkinter.Button(width = 5, height = 2, text = "", font = "bold", command = lambda: setSymbolOnClick(b2, 2))
    b3 = tkinter.Button(width = 5, height = 2, text = "", font = "bold", command = lambda: setSymbolOnClick(b3, 3))
    b4 = tkinter.Button(width = 5, height = 2, text = "", font = "bold", command = lambda: setSymbolOnClick(b4, 4))
    b5 = tkinter.Button(width = 5, height = 2, text = "", font = "bold", command = lambda: setSymbolOnClick(b5, 5))
    b6 = tkinter.Button(width = 5, height = 2, text = "", font = "bold", command = lambda: setSymbolOnClick(b6, 6))
    b7 = tkinter.Button(width = 5, height = 2, text = "", font = "bold", command = lambda: setSymbolOnClick(b7, 7))
    b8 = tkinter.Button(width = 5, height = 2, text = "", font = "bold", command = lambda: setSymbolOnClick(b8, 8))
    b9 = tkinter.Button(width = 5, height = 2, text = "", font = "bold", command = lambda: setSymbolOnClick(b9, 9))
    reset = tkinter.Button(width = 17, height = 2, text = "Reset", font = "bold", command = resetAll)
    b1.grid(row = 1, column = 1)
    b2.grid(row = 1, column = 2)
    b3.grid(row = 1, column = 3)
    b4.grid(row = 2, column = 1)
    b5.grid(row = 2, column = 2)
    b6.grid(row = 2, column = 3) 
    b7.grid(row = 3, column = 1)
    b8.grid(row = 3, column = 2)
    b9.grid(row = 3, column = 3)
    reset.grid(row = 4, column = 1, columnspan = 3)
    playOrder = randint(0, 1)
    if playOrder == 1: ai()
    master.resizable(0,0)
    master.mainloop()

if __name__ == '__main__':
    main()
