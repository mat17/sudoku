#Sudoku je seznam seznamov, vrstica je indeks med 0 in 8, elementi s ostevila od 1-9 ter vrednost None
def pregled_po_vrsticah(sudoku):
    '''za vsako prazno mesto v vrstici preverimo, ce je mozno vpisati novo stevilko'''
    # za vsako mesto v vrstici pregledamo pripadajoc 3x3 kvadrat in stolpec

    seznam_moznih = [[] for i in range(9)]  #seznam[i][j] -> bo mnozica, ki bo vsebovala vse mozne stevilke, ki bi lahko zasedle prazno mesto v danem kvadratku

    for vrstica in range(9):

        vpisane = set(sudoku[vrstica]).difference({None})                   # stevilke, ki so ze vpisane v vrstici
        mozne = set(range(1,10)).difference(vpisane)                        # stevilke, ki niso se vpisane v vrstici

        for stolpec in range(9):
            if sudoku[vrstica][stolpec]:        #ce je kvadratek ze zapolnjen ga preskocimo
                seznam_moznih[vrstica].append(set())
                continue
            mozne_kvadratek = set(i for i in mozne)
            for i in range(9):                  # odstranimo tiste stevilke, ki so ze v stolpcu
                mozne_kvadratek.discard(sudoku[i][stolpec])
            for i in range(3):      #odstranimo clane 3x3 kvadratka
                for j in range(3):
                    mozne_kvadratek.discard(sudoku[(vrstica//3)*3 + i][(stolpec//3)*3 + j])
            seznam_moznih[vrstica].append(mozne_kvadratek)

    return seznam_moznih

def resevanje_brez_ugibanja(original_sudoku, original_seznam_moznih):
    sudoku = [i for i in original_sudoku]
    seznam_moznih = [i for i in original_seznam_moznih]
    novo_stevilo = 1
    while novo_stevilo:
        novo_stevilo = None
        # ce je v nekem kvadratku samo ena opcija jo izberemo
        for v in range(9):
            for s in range(9):
                if len(seznam_moznih[v][s]) == 1:
                    novo_stevilo = (seznam_moznih[v][s].pop(), v, s)
                    break
            if novo_stevilo:
                break
        # ce je v neki vrstici neko stevilo mozno le v enem kvadratku ga izberemo
        # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        if not novo_stevilo:
            v  = 0
            while v < 9:
                for element in {i for sublist in seznam_moznih[v] for i in sublist}:
                    if [i for sublist in seznam_moznih[v] for i in sublist].count(element) == 1:
                        novo_stevilo = element
                        break
                if novo_stevilo:
                    s = 0
                    while s < 9:
                        if novo_stevilo in seznam_moznih[v][s]:
                            novo_stevilo = (novo_stevilo, v, s)
                            break
                        s += 1
                    break
                v += 1
        # ce je v nekem stolpcu neko stevilo mozno le v enem kvadratku ga izberemo
        if not novo_stevilo:
            s = 0
            while s < 9:
                for element in {i for sublist in [i[s] for i in seznam_moznih] for i in sublist}:
                    if [i for sublist in [i[s] for i in seznam_moznih] for i in sublist].count(element) == 1:
                        novo_stevilo = element
                        break
                if novo_stevilo:
                    v = 0
                    while v < 9:
                        if novo_stevilo in seznam_moznih[v][s]:
                            novo_stevilo = (novo_stevilo, v, s)
                            break
                        v += 1
                    break
                s += 1
        # ce je v nekem 3x3 kvadratu neko stevilo mozno le v enem kvadratku ga izberemo
        if not novo_stevilo:
            for x in range(9):
                for element in {i for sublist in [i for sublist in seznam_moznih[(x//3)*3 : (x//3)*3 + 3] for i in sublist[(x%3)*3 : (x%3)*3 + 3]] for i in sublist}:
                    if [i for sublist in [i for sublist in seznam_moznih[(x//3)*3 : (x//3)*3 + 3] for i in sublist[(x%3)*3 : (x%3)*3 + 3]] for i in sublist].count(element) == 1:
                        novo_stevilo = novo_stevilo
                        break
                if novo_stevilo:
                    break
            if novo_stevilo:
                for i in range(9):
                    if novo_stevilo in seznam_moznih[(x//3)*3 + i//3][(x%3)*3 + i%3]:
                        novo_stevilo = (novo_stevilo, (x//3)*3 + i//3, (x%3)*3 + i%3)
                        break
        #ce smo dobili novo stevilo ga moramo izbrisati iz ustreznih mnozic
        if novo_stevilo:
            sudoku[v][s] = novo_stevilo[0]
            seznam_moznih[v][s] = set()
            for i in range(9):
                seznam_moznih[novo_stevilo[1]][i].discard(novo_stevilo[0])
                seznam_moznih[i][novo_stevilo[2]].discard(novo_stevilo[0])
                seznam_moznih[(novo_stevilo[1]//3)*3 + i//3][(novo_stevilo[2]//3)*3 + i%3].discard(novo_stevilo[0])
        # ce nismo dobili novega stevila poskusimo poboljsati seznam_moznih
        # npr ce imamo v vrstici/stolpcu/3x3 2 kvadratka, v katera lahko vpisemo le isti par stevil,
        # lahko ta par stevil odstranimo iz moznosti za druge kvadratke v tej vrstici/stolpcu/3x3
        if not novo_stevilo:
            nova_stevila = []
            # najprej za vrstice:
            for v in range(9):
                for i in range(9):
                    if len(seznam_moznih[v][i]) != 2:
                        continue
                    for j in range(i+1, 9):
                        if seznam_moznih[v][i] == seznam_moznih[v][j]:
                            nova_stevila.append((seznam_moznih[v][i], ('v', v)))
                            print('ZGODI SE1', (seznam_moznih[v][i], ('v', v)))
                            break
                    if novo_stevilo:
                        break
                if novo_stevilo:
                    break
            # za stolpce:
            for s in range(9):
                for i in range(9):
                    if len(seznam_moznih[i][s]) != 2:
                        continue
                    for j in range(i+1, 9):
                        if seznam_moznih[i][s] == seznam_moznih[j][s]:
                            nova_stevila.append((seznam_moznih[i][s], ('s', s)))
                            print('ZGODI SE2', (seznam_moznih[i][s], ('s', s)))
                            break
                    if novo_stevilo:
                        break
                if novo_stevilo:
                    break
            # za 3x3:
            for x in range(9):
                for i in range(9):
                    if len(seznam_moznih[(x//3)*3 + i//3][(x%3)*3 + i%3]) != 2:
                        continue
                    for j in range(i+1, 9):
                        if seznam_moznih[(x//3)*3 + i//3][(x%3)*3 + i%3] == seznam_moznih[(x//3)*3 + j//3][(x%3)*3 + j%3]:
                            nova_stevila.append((seznam_moznih[(x//3)*3 + i//3][(x%3)*3 + i%3], ('3x3', x)))
                            print('ZGODI SE3', (seznam_moznih[(x//3)*3 + i//3][(x%3)*3 + i%3], ('3x3', x)))
                            break
                    if novo_stevilo:
                        break
                if novo_stevilo:
                    break
            # ce imamo v 3x3 kvadratu polno vrstico/stolpec, lahko pride do tega,
            # da je neko manjkajoce stevilo lahko le v eni od preostalih dveh
            # vrstic/stolpcev in se mora tako v tisti vrstici/stolpcu pojaviti
            # v danem 3x3 kvadratu in ne na ostalih 6ih mestih.

            
            # popravimo seznam_moznih
            # s spremenljivko 'vsota_dolzin' preverimo, da smo dejansko opravili spremembo - sicer se lahko zaciklamo 
            if nova_stevila != []:
                vsota_dolzin = sum([len(i) for sublist in seznam_moznih for i in sublist])
                for novo in nova_stevila:
                    if novo[1][0] == 'v':
                        for i in range(9):
                            if seznam_moznih[novo[1][1]][i] != novo[0]:
                                seznam_moznih[novo[1][1]][i] = seznam_moznih[novo[1][1]][i].difference(novo[0])               
                    if novo[1][0] == 's':
                        for i in range(9):
                            if seznam_moznih[i][novo[1][1]] != novo[0]:
                                seznam_moznih[i][novo[1][1]] = seznam_moznih[i][novo[1][1]].difference(novo[0])
                    if novo[1][0] == '3x3':
                        for i in range(9):
                            if seznam_moznih[(novo[1][1]//3)*3 + i//3][(novo[1][1]%3)*3 + i%3] != novo[0]:
                                seznam_moznih[(novo[1][1]//3)*3 + i//3][(novo[1][1]%3)*3 + i%3] = seznam_moznih[(novo[1][1]//3)*3 + i//3][(novo[1][1]%3)*3 + i%3].difference(novo[0])            
                if vsota_dolzin == sum([len(i) for sublist in seznam_moznih for i in sublist]):
                    # ni sprememb, koncamo
                    novo_stevilo = None
                else:
                    # naredili smo spremembe, zato gremo se en krog
                    novo_stevilo = True
        print('ddasdsadas', novo_stevilo)
        print(sudoku)
        print(seznam_moznih)
        print()
    return (sudoku, seznam_moznih)

def je_vse_ok(sudoku, seznam_moznih):
    #preverimo, da vsakemu zapolnjenemu polju v sudokuju ustreza prazna mnozica v seznamu_moznih in
    #preverimo, da vsakemu praznemu polju v sudokuju ustreza neprazna mnozica v seznamu_moznih
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]:
                if not seznam_moznih[i][j] == set():
                    print('false1', seznam_moznih[i][j], sudoku[i][j], i, j)
                    return False
            else:
                if seznam_moznih[i][j] == set():
                    print('false2', seznam_moznih[i][j], sudoku[i][j], i, j)
                    return False
    return True
                

# ce uporabimo resevanje_brez_ugibanja, dobimo pa nedokoncan sudoku, uporabimo funkcijo ugibanje
# vrnemo seznam seznamov trojk
# vsaka trojka ima obliko (stevilo, index_vrstice, index_stolpca)
# vsaka trojka predstavlja eno 'ugibanje'
# v seznamih so vse mozne kombinacije teh ugibanj
# vedno dodamo samo eno novo ugibanje (torej novo ugibanje za eno polje)
# ce sudokuja se vedno ni mogoce resiti ponovno uporabimo funkcijo ugibanje
def ugibanje(seznam_moznih):
    min_len = 9
    for i in range(9):
        for j in range(9):
            if seznam_moznih[i][j] == set():
                continue
            min_len = min(min_len, len(seznam_moznih[i][j]))
            if min_len == len(seznam_moznih[i][j]):
                koordinata = (i,j)
            if min_len == 2:
                break
        if min_len == 2:
            break
    return koordinata
        
def postopek_resevanja(sudoku):
    while True:
        #ustvarimo seznam_moznih:
        seznam_moznih = pregled_po_vrsticah(sudoku)
        sudoku, seznam_moznih = resevanje_brez_ugibanja(sudoku, seznam_moznih)
        if not je_vse_ok(sudoku, seznam_moznih):
            print('slaba resitev', sudoku)
            break
        # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        if [item for sublist in seznam_moznih for item in sublist] == [set() for i in range(81)]:
            print('YEA', sudoku)
            return sudoku
        else:
            k0, k1 = ugibanje(seznam_moznih)
            for moznost in seznam_moznih[k0][k1]:
                print((k0, k1), seznam_moznih[k0][k1], moznost)
                kopija = []
                for vrstica in sudoku:
                    kopija.append(vrstica.copy())
                kopija[k0][k1] = moznost
                x = postopek_resevanja(kopija)
                if x == None:
                    pass
                else:
                    return x
            break














        
        
        
        
    
