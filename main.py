import tkinter
import sys
app = tkinter.Tk()

cv = tkinter.Canvas(app, height=920, width=920, bd=0)
cv.create_rectangle(300, 0, 310, 920, fill="black")
cv.create_rectangle(610, 0, 620, 920, fill="black")
cv.create_rectangle(0, 300, 920, 310, fill="black")
cv.create_rectangle(0, 610, 920, 620, fill="black")

turn = "x"

data = [
    [
        {"val": " ", "x": 70, "y": 70, "mxs": 0, "mxe": 300, "mys": 0, "mye": 300},
        {"val": " ", "x": 380, "y": 70, "mxs": 310, "mxe": 610, "mys": 0, "mye": 300},
        {"val": " ", "x": 690, "y": 70, "mxs": 620, "mxe": 920, "mys": 0, "mye": 300}
    ], [
        {"val": " ", "x": 70, "y": 380, "mxs": 0, "mxe": 300, "mys": 310, "mye": 610},
        {"val": " ", "x": 380, "y": 380, "mxs": 310, "mxe": 610, "mys": 310, "mye": 610},
        {"val": " ", "x": 690, "y": 380, "mxs": 620, "mxe": 920, "mys": 310, "mye": 610}
    ], [
        {"val": " ", "x": 70, "y": 690, "mxs": 0, "mxe": 300, "mys": 620, "mye": 920},
        {"val": " ", "x": 380, "y": 690, "mxs": 310, "mxe": 610, "mys": 620, "mye": 920},
        {"val": " ", "x": 690, "y": 690, "mxs": 620, "mxe": 920, "mys": 620, "mye": 920}
    ]
]

def drawCross(cv, x, y, w, h):
    cv.create_line(x, y, x + w, y + h, width=10, fill="red")
    cv.create_line(x, y + h, x + w, y, width=10, fill="red")

def drawCircle(cv, x, y, w, h):
    cv.create_oval(x, y, x + w, y + h, width=10, outline="blue")

def checkWin():
    global data
    
    fullpass = ["", "", "", "", "", "", "", "", ""]
    verticalpass = [["", "", ""], ["", "", ""], ["", "", ""]]
    horizontalpass = [["", "", ""], ["", "", ""], ["", "", ""]]

    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            verticalpass[j][i] = cell['val']
            horizontalpass[i][j] = cell['val']
            fullpass[i * 3 + j] = cell['val']
    
    for p in verticalpass:
        val = "".join(p)
        if val == "xxx":
            print("x wins!")
            sys.exit()
        elif val == "ooo":
            print("o wins!")
            sys.exit()
    
    for p in horizontalpass:
        val = "".join(p)
        if val == "xxx":
            print("x wins!")
            sys.exit()
        elif val == "ooo":
            print("o wins!")
            sys.exit()
    
    diag1 = data[0][0]['val'] + data[1][1]['val'] + data[2][2]['val']
    diag2 = data[0][2]['val'] + data[1][1]['val'] + data[2][0]['val']

    if diag1 == "xxx":
        print("x wins!")
        sys.exit()
    elif diag1 == "ooo":
        print("o wins!")
        sys.exit()
    
    if diag2 == "xxx":
        print("x wins!")
        sys.exit()
    elif diag2 == "ooo":
        print("o wins!")
        sys.exit()
    
    if not " " in fullpass:
        print("tie!")
        sys.exit()



def canvasClicked(e):
    global cv, turn, data

    for row in data:
        for cell in row:
            if e.x > cell['mxs'] and e.x < cell['mxe'] and e.y > cell['mys'] and e.y < cell['mye'] and cell['val'] == " ":
                cell['val'] = turn
                func = drawCross if turn == 'x' else drawCircle
                func(cv, cell['x'], cell['y'], 150, 150)
                turn = 'o' if turn == 'x' else 'x'
    
    checkWin()


cv.bind("<Button-1>", canvasClicked)

cv.pack()
app.mainloop()