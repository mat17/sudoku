# sudoku

Program za resevanje sudokujev.
Naceloma iz dveh delov - uporabniskega vmesnika in logike za resevanje.
V uporabniskem vmesniku je 9x9 vnosnih polj. V ustrezna polja uporabnik vpise znane stevilke,
potem pa na dnu okna klikne gumb 'Zazeni!'. Ko program resi sudoku se v ostalih vnosnih poljih 
izpisejo vse preostale stevilke.
Ce zeli uporabnik resiti nov sudoku lahko klikne gumb 'reset' in tako pobrise vsa vnosna polja.

Logicni del resuje sudoku tako, da preverja moznosti za vsak kvadratek (izmed 81).
Ko naleti na primer, ko ne ve kako naprej, najde polje, ki ima najmanj moznih resitev in (rekurzivno) 
preveri vse resitve, razen v primeru, ko ze pred preverbo vseh resitev naleti na pravilno.