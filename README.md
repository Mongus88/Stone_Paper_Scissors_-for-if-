Ezzel a feladattal a for ciklust és az if - elif - else elágazásokat todod gyakorolni.

Feladat leírása:  A játékban három tárgy közül tudsz választani kő, papír és olló.
                  Bármit is választasz három lehetséges kimenete lesz nyertél, vesztettél vagy döntettlen.
                  Ha nyertél kapsz egy pontot, ha vesztettél a gép kap egy pontot, döntetlennél senki nem kap pontot.
                  A kő üti az ollót, az olló üti a papírt, a papír üti a követ.
                  Három kört kell játszanod és aki a végén több pontot ért el az nyert. Ezt a 3. kör végén írasd ki.
                  A program büntesse az elgépelést és a gép kapjon egy pontot.


Program felépítése:

Szükségünk van a (1) random modulra, hogy a gép véletlenül tudjon választani.
Létre kell hozni (3) egy lista típusú változót amiben a kő, papír, ólló szerepel és (4-5) 1-1 üres változót amibe majd gyüjtjük a pontokat
(7) for ciklust használunk mert tudjuk, hogy hányszor fut le.
(8) Fel kell tennünk a kérdés amire majd egy választ várunk.
(9-12) Ez a rész adja az elgépelésből származó pontot a gépnek.
(13-14) A gép váalszt a listából és ki is írja.
(15-24) A itt dől el, hogy ki nyerte a kört, vagy hogy döntetlen lett-e.
(25) Eredmény hirdetés a harmadik kör végén.


A (12) sorban lévő continue parancs azért szükséges a kódba mert ha itt nem fejeznénk be a ciklust egy elgépelt választ esetén akkor tovább megy az
if elágazásra ami hamis lesz
elif is hamis lesz
else fog érvényesülni és a gép kap még egy pontot. Tehát egy kör alatt érvénytelen válasz esetén 2 pontot kap a gép.


Lehetséges fejlesztések:

Ha a szó jelentésben azonos a listában szereplővel de formailag nem egyezik az érvénytelen lesz. pl.: "  papír", "papír  ", "Papír", "paPír"  

Több játékos profil hozzáadása, és az eredmények mentése.

Több játékos esetén egymás ellen is lehessen játszani.

Ranglista funkció
