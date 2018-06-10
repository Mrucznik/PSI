mezczyzna(franciszek).
mezczyzna(jan).
mezczyzna(krzysztof).
mezczyzna(wojciech).
mezczyzna(robert).
mezczyzna(bogdan).

kobieta(wanda).
kobieta(anna).
kobieta(ewa).
kobieta(zofia).
kobieta(katarzyna).
kobieta(maria).

malzenstwo(wojciech, zofia).
malzenstwo(zofia, wojciech).
malzenstwo(jan, maria).
malzenstwo(maria, jan).
malzenstwo(anna, bogdan).
malzenstwo(bogdan, anna).

rodzic(franciszek, maria).
rodzic(wanda, bogdan).
rodzic(jan, krzysztof).
rodzic(maria, krzysztof).
rodzic(jan, wojciech).
rodzic(maria, wojciech).
rodzic(wojciech, katarzyna).
rodzic(zofia, katarzyna).
rodzic(wojciech, robert).
rodzic(zofia, robert).
rodzic(bogdan, zofia).
rodzic(anna, zofia).
rodzic(bogdan, ewa).
rodzic(anna, ewa).

matka(RODZIC,DZIECKO):-
    kobieta(RODZIC),
    rodzic(RODZIC,DZIECKO).

ojciec(RODZIC,DZIECKO):-
    mezczyzna(RODZIC),
    rodzic(RODZIC,DZIECKO).

babcia(BABCIA,DZIECKO):-
    kobieta(BABCIA),
    rodzic(RODZIC,DZIECKO),
    rodzic(BABCIA,RODZIC).

dziadek(DZIADEK,DZIECKO):-
    mezczyzna(DZIADEK),
    rodzic(RODZIC,DZIECKO),
    rodzic(DZIADEK,RODZIC).

siostra(SIOSTRA,JA):-
    kobieta(SIOSTRA),
    rodzic(RODZIC, JA),
    rodzic(RODZIC, SIOSTRA).

brat(BRAT,JA):-
    mezczyzna(BRAT),
    rodzic(RODZIC, JA),
    rodzic(RODZIC, BRAT).

syn(SYN,RODZIC):-
    mezczyzna(SYN),
    rodzic(RODZIC, SYN).

corka(CORKA,RODZIC):-
    kobieta(CORKA),
    rodzic(RODZIC, CORKA).

przodek(PRZODEK, POTOMEK):-
    rodzic(PRZODEK, POTOMEK);
    (   
    	rodzic(RODZIC, POTOMEK),
        przodek(PRZODEK, RODZIC)
    ).

potomek(POTOMEK, PRZODEK):-
    rodzic(PRZODEK, POTOMEK);
    (   
    	rodzic(RODZIC, POTOMEK),
        przodek(PRZODEK, RODZIC)
    ).

ma_dzieci(OSOBA):-
    rodzic(OSOBA, _).

jest_dziadkiem(OSOBA):-
    mezczyzna(OSOBA),
    rodzic(OSOBA, DZIECKO),
    rodzic(DZIECKO, _).

rodzenstwo(OSOBA1, OSOBA2):-
    rodzic(RODZIC, OSOBA1),
    rodzic(RODZIC, OSOBA2).

kuzyn(KUZYN, OSOBA):-
    mezczyzna(KUZYN),
    rodzic(RODZIC_KUZYNA, KUZYN),
    rodzic(RODZIC_OSOBY, OSOBA),
    rodzenstwo(RODZIC_KUZYNA, RODZIC_OSOBY).