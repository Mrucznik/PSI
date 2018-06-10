kobieta(ala).
kobieta(zofia).
kobieta(magda).

mezczyzna(marek).
mezczyzna(jozef).
mezczyzna(adolf).

lubi(marek, psy).
lubi(marek, adolf).
lubi(adolf, jozef).
lubi(zofia, marek).
lubi(ala, psy).
lubi(ala, koty).

lubi(marek, X):-kobieta(X).
lubi(ala, X):-lubi(marek, X).
