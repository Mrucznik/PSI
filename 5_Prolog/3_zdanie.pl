pilkarz(marek).
pilkarz(jan).

plywak(jan).
plywak(adam).

sportowiec(OSOBA):-
    biegacz(OSOBA);
    plywak(OSOBA).
    
bierze_udzial_w_zawodach(OSOBA):-
    sportowiec(OSOBA),
    ma_dobra_kondycje(OSOBA).

biegacz(OSOBA):-
    pilkarz(OSOBA).

ma_dobra_kondycje(OSOBA):-
    pilkarz(OSOBA).


