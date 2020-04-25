import tkinter.ttk as ttk
from tkinter.font import Font
from tkinter import messagebox
from tkinter import *
import sudoku_resevanje as sudoku_resevanje


root = Tk()
style = ttk.Style()
style.theme_use('clam')
root.option_add("*Font", ("comic sans MS",9))
root.title('Sudoku')
root.geometry('255x310')

okvir0 = Frame(root)
okvir0.grid(row = 0, column = 0, sticky = 'w')
napis00 = Label(root, text = 'Vpiši številke v sudoku. \nKo končaš pritisni gumb \'Zaženi!\'', justify=LEFT)
napis00.grid(row = 0, column = 0, sticky = 'w', columnspan = 3, padx = (7,0), pady = (10,0))

okvir1 = Frame(root)
okvir1.grid(row = 1, column = 0, sticky = 'w', padx = (10,0), pady = (10,0))
vnos1 = Entry(okvir1, width = 3)
vnos1.grid(row = 0, column = 0, sticky = 'w')
vnos2 = Entry(okvir1, width = 3)
vnos2.grid(row = 0, column = 1, sticky = 'w')
vnos3 = Entry(okvir1, width = 3)
vnos3.grid(row = 0, column = 2, sticky = 'w')
vnos4 = Entry(okvir1, width = 3)
vnos4.grid(row = 1, column = 0, sticky = 'w')
vnos5 = Entry(okvir1, width = 3)
vnos5.grid(row = 1, column = 1, sticky = 'w')
vnos6 = Entry(okvir1, width = 3)
vnos6.grid(row = 1, column = 2, sticky = 'w')
vnos7 = Entry(okvir1, width = 3)
vnos7.grid(row = 2, column = 0, sticky = 'w')
vnos8 = Entry(okvir1, width = 3)
vnos8.grid(row = 2, column = 1, sticky = 'w')
vnos9 = Entry(okvir1, width = 3)
vnos9.grid(row = 2, column = 2, sticky = 'w')

okvir2 = Frame(root)
okvir2.grid(row = 1, column = 1, sticky = 'w', padx = (5,0), pady = (10,0))
vnos10 = Entry(okvir2, width = 3)
vnos10.grid(row = 0, column = 0, sticky = 'w')
vnos11 = Entry(okvir2, width = 3)
vnos11.grid(row = 0, column = 1, sticky = 'w')
vnos12 = Entry(okvir2, width = 3)
vnos12.grid(row = 0, column = 2, sticky = 'w')
vnos13 = Entry(okvir2, width = 3)
vnos13.grid(row = 1, column = 0, sticky = 'w')
vnos14 = Entry(okvir2, width = 3)
vnos14.grid(row = 1, column = 1, sticky = 'w')
vnos15 = Entry(okvir2, width = 3)
vnos15.grid(row = 1, column = 2, sticky = 'w')
vnos16 = Entry(okvir2, width = 3)
vnos16.grid(row = 2, column = 0, sticky = 'w')
vnos17 = Entry(okvir2, width = 3)
vnos17.grid(row = 2, column = 1, sticky = 'w')
vnos18 = Entry(okvir2, width = 3)
vnos18.grid(row = 2, column = 2, sticky = 'w')


okvir3 = Frame(root)
okvir3.grid(row = 1, column = 2, sticky = 'w', padx = (5,10), pady = (10,0))
vnos19 = Entry(okvir3, width = 3)
vnos19.grid(row = 0, column = 0, sticky = 'w')
vnos20 = Entry(okvir3, width = 3)
vnos20.grid(row = 0, column = 1, sticky = 'w')
vnos21 = Entry(okvir3, width = 3)
vnos21.grid(row = 0, column = 2, sticky = 'w')
vnos22 = Entry(okvir3, width = 3)
vnos22.grid(row = 1, column = 0, sticky = 'w')
vnos23 = Entry(okvir3, width = 3)
vnos23.grid(row = 1, column = 1, sticky = 'w')
vnos24 = Entry(okvir3, width = 3)
vnos24.grid(row = 1, column = 2, sticky = 'w')
vnos25 = Entry(okvir3, width = 3)
vnos25.grid(row = 2, column = 0, sticky = 'w')
vnos26 = Entry(okvir3, width = 3)
vnos26.grid(row = 2, column = 1, sticky = 'w')
vnos27 = Entry(okvir3, width = 3)
vnos27.grid(row = 2, column = 2, sticky = 'w')

okvir4 = Frame(root)
okvir4.grid(row = 2, column = 0, sticky = 'w', padx = (10,0), pady = (5,0))
vnos28 = Entry(okvir4, width = 3)
vnos28.grid(row = 0, column = 0, sticky = 'w')
vnos29 = Entry(okvir4, width = 3)
vnos29.grid(row = 0, column = 1, sticky = 'w')
vnos30 = Entry(okvir4, width = 3)
vnos30.grid(row = 0, column = 2, sticky = 'w')
vnos31 = Entry(okvir4, width = 3)
vnos31.grid(row = 1, column = 0, sticky = 'w')
vnos32 = Entry(okvir4, width = 3)
vnos32.grid(row = 1, column = 1, sticky = 'w')
vnos33 = Entry(okvir4, width = 3)
vnos33.grid(row = 1, column = 2, sticky = 'w')
vnos34 = Entry(okvir4, width = 3)
vnos34.grid(row = 2, column = 0, sticky = 'w')
vnos35 = Entry(okvir4, width = 3)
vnos35.grid(row = 2, column = 1, sticky = 'w')
vnos36 = Entry(okvir4, width = 3)
vnos36.grid(row = 2, column = 2, sticky = 'w')


okvir5 = Frame(root)
okvir5.grid(row = 2, column = 1, sticky = 'w', padx = (5,0), pady = (5,0))
vnos37 = Entry(okvir5, width = 3)
vnos37.grid(row = 0, column = 0, sticky = 'w')
vnos38 = Entry(okvir5, width = 3)
vnos38.grid(row = 0, column = 1, sticky = 'w')
vnos39 = Entry(okvir5, width = 3)
vnos39.grid(row = 0, column = 2, sticky = 'w')
vnos40 = Entry(okvir5, width = 3)
vnos40.grid(row = 1, column = 0, sticky = 'w')
vnos41 = Entry(okvir5, width = 3)
vnos41.grid(row = 1, column = 1, sticky = 'w')
vnos42 = Entry(okvir5, width = 3)
vnos42.grid(row = 1, column = 2, sticky = 'w')
vnos43 = Entry(okvir5, width = 3)
vnos43.grid(row = 2, column = 0, sticky = 'w')
vnos44 = Entry(okvir5, width = 3)
vnos44.grid(row = 2, column = 1, sticky = 'w')
vnos45 = Entry(okvir5, width = 3)
vnos45.grid(row = 2, column = 2, sticky = 'w')



okvir6 = Frame(root)
okvir6.grid(row = 2, column = 2, sticky = 'w', padx = (5,10), pady = (5,0))
vnos46 = Entry(okvir6, width = 3)
vnos46.grid(row = 0, column = 0, sticky = 'w')
vnos47 = Entry(okvir6, width = 3)
vnos47.grid(row = 0, column = 1, sticky = 'w')
vnos48 = Entry(okvir6, width = 3)
vnos48.grid(row = 0, column = 2, sticky = 'w')
vnos49 = Entry(okvir6, width = 3)
vnos49.grid(row = 1, column = 0, sticky = 'w')
vnos50 = Entry(okvir6, width = 3)
vnos50.grid(row = 1, column = 1, sticky = 'w')
vnos51 = Entry(okvir6, width = 3)
vnos51.grid(row = 1, column = 2, sticky = 'w')
vnos52 = Entry(okvir6, width = 3)
vnos52.grid(row = 2, column = 0, sticky = 'w')
vnos53 = Entry(okvir6, width = 3)
vnos53.grid(row = 2, column = 1, sticky = 'w')
vnos54 = Entry(okvir6, width = 3)
vnos54.grid(row = 2, column = 2, sticky = 'w')



okvir7 = Frame(root)
okvir7.grid(row = 3, column = 0, sticky = 'w', padx = (10,0), pady = (5,10))
vnos55 = Entry(okvir7, width = 3)
vnos55.grid(row = 0, column = 0, sticky = 'w')
vnos56 = Entry(okvir7, width = 3)
vnos56.grid(row = 0, column = 1, sticky = 'w')
vnos57 = Entry(okvir7, width = 3)
vnos57.grid(row = 0, column = 2, sticky = 'w')
vnos58 = Entry(okvir7, width = 3)
vnos58.grid(row = 1, column = 0, sticky = 'w')
vnos59 = Entry(okvir7, width = 3)
vnos59.grid(row = 1, column = 1, sticky = 'w')
vnos60 = Entry(okvir7, width = 3)
vnos60.grid(row = 1, column = 2, sticky = 'w')
vnos61 = Entry(okvir7, width = 3)
vnos61.grid(row = 2, column = 0, sticky = 'w')
vnos62 = Entry(okvir7, width = 3)
vnos62.grid(row = 2, column = 1, sticky = 'w')
vnos63 = Entry(okvir7, width = 3)
vnos63.grid(row = 2, column = 2, sticky = 'w')



okvir8 = Frame(root)
okvir8.grid(row = 3, column = 1, sticky = 'w', padx = (5,0), pady = (5,10))
vnos64 = Entry(okvir8, width = 3)
vnos64.grid(row = 0, column = 0, sticky = 'w')
vnos65 = Entry(okvir8, width = 3)
vnos65.grid(row = 0, column = 1, sticky = 'w')
vnos66 = Entry(okvir8, width = 3)
vnos66.grid(row = 0, column = 2, sticky = 'w')
vnos67 = Entry(okvir8, width = 3)
vnos67.grid(row = 1, column = 0, sticky = 'w')
vnos68 = Entry(okvir8, width = 3)
vnos68.grid(row = 1, column = 1, sticky = 'w')
vnos69 = Entry(okvir8, width = 3)
vnos69.grid(row = 1, column = 2, sticky = 'w')
vnos70 = Entry(okvir8, width = 3)
vnos70.grid(row = 2, column = 0, sticky = 'w')
vnos71 = Entry(okvir8, width = 3)
vnos71.grid(row = 2, column = 1, sticky = 'w')
vnos72 = Entry(okvir8, width = 3)
vnos72.grid(row = 2, column = 2, sticky = 'w')



okvir9 = Frame(root)
okvir9.grid(row = 3, column = 2, sticky = 'w', padx = (5,10), pady = (5,10))
vnos73 = Entry(okvir9, width = 3)
vnos73.grid(row = 0, column = 0, sticky = 'w')
vnos74 = Entry(okvir9, width = 3)
vnos74.grid(row = 0, column = 1, sticky = 'w')
vnos75 = Entry(okvir9, width = 3)
vnos75.grid(row = 0, column = 2, sticky = 'w')
vnos76 = Entry(okvir9, width = 3)
vnos76.grid(row = 1, column = 0, sticky = 'w')
vnos77 = Entry(okvir9, width = 3)
vnos77.grid(row = 1, column = 1, sticky = 'w')
vnos78 = Entry(okvir9, width = 3)
vnos78.grid(row = 1, column = 2, sticky = 'w')
vnos79 = Entry(okvir9, width = 3)
vnos79.grid(row = 2, column = 0, sticky = 'w')
vnos80 = Entry(okvir9, width = 3)
vnos80.grid(row = 2, column = 1, sticky = 'w')
vnos81 = Entry(okvir9, width = 3)
vnos81.grid(row = 2, column = 2, sticky = 'w')

vnosi = [vnos1, vnos2, vnos3, vnos10, vnos11, vnos12, vnos19, vnos20, vnos21,
         vnos4, vnos5, vnos6, vnos13, vnos14, vnos15, vnos22, vnos23, vnos24, 
         vnos7, vnos8, vnos9, vnos16, vnos17, vnos18, vnos25, vnos26, vnos27,
         vnos28, vnos29, vnos30, vnos37, vnos38, vnos39, vnos46, vnos47, vnos48,
         vnos31, vnos32, vnos33, vnos40, vnos41, vnos42, vnos49, vnos50, vnos51,
         vnos34, vnos35, vnos36, vnos43, vnos44, vnos45, vnos52, vnos53, vnos54,
         vnos55, vnos56, vnos57, vnos64, vnos65, vnos66, vnos73, vnos74, vnos75,
         vnos58, vnos59, vnos60, vnos67, vnos68, vnos69, vnos76, vnos77, vnos78,
         vnos61, vnos62, vnos63, vnos70, vnos71, vnos72, vnos79, vnos80, vnos81]

okvir10 = Frame(root)
okvir10.grid(row = 4, column = 0, sticky = 'w')
def reset():
    for i in range(9):
        for j in range(9):
            vnosi[i*9 + j].delete(0, END)
gumb0 = Button(okvir10, text = 'Reset', command = reset)
gumb0.grid(row = 0, column = 0, padx = (10,0), pady = (0,7), sticky = 'e w')

okvir11 = Frame(root)
okvir11.grid(row = 4, column = 2, sticky = 'e')
def klik():
    sudoku = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            vrednost = vnosi[i*9 + j].get()
            if vrednost != '':
                sudoku[i].append(int(vrednost))
            else:
                sudoku[i].append(None)
    # najprej naredi spremenljivko 'sudoku' iz vnosov iz vnosnih polj
    #ne pozabi na int()
    for i in sudoku:
        print(i)
    resen_sudoku = sudoku_resevanje.postopek_resevanja(sudoku)
    for i in range(9):
        for j in range(9):
            vnosi[i*9 + j].delete(0, END)
            vnosi[i*9 + j].insert(0, resen_sudoku[i][j])
gumb = Button(okvir11, text = 'Zaženi!', command = klik, justify = RIGHT)
gumb.grid(row = 0, column = 0, padx = (0,10), pady = (0,7), sticky = 'e w')


root.mainloop()
