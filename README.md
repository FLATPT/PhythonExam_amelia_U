# Examination: Programmering med Python, NBIHAK TAPHT25D
### Student: Amélia Uebel
### Lärare: David Andersson

# Uppgift: Bygga vidare på spelet "Fruit loop"
Uppgiften var att bygga vidare på spelet "Fruit loop". 
Spelet går ut på att samla så många poäng som möjligt genom att plocka frukter/grönsaker som är slumpmässigt placerade på spelplanen genom att ta det snabbaste väg och undvika att krocka mot väggarna.

## Funktioner
- Spelaren styr sina rörelser med **WASD**-tangenterna
- Spelaren kan få information om alla plockade frukter/grönsaker genom att trycka på **I**-tangenten
- Frukterna är slumpmässigt placerade på spelplanen
- Spelaren måste plocka alla frukter/grönsaker på spelplanen
- Spelaren måste undvika att krocka med väggarna
- Spelare skall välja den kortaste och effektivaste väg att plocka alla frukter/grönsaker för att samla så många poäng som möjligt. 
- Vid varje steg spelaren tar utan att plocka en frukt/grönsak, dras det bort en poäng.
- Spelt avslutas när spelare trycker på **Q/X**-tangenterna.



Jag har byggt vidare spelet genom att implementera examinationens Version 1 - grundkrav.
### Version 1 - grundkrav
A. Spelaren ska börja nära mitten av rummet.
B. Förflyttningar i alla 4 riktningar. (Med tangenterna WASD.)
C. Man ska inte kunna gå igenom väggar.
D. Fruktsallad - alla frukter ska vara värda 20 poäng i stället för 10.
E. Inventory - alla saker som man plockar upp ska sparas i en lista.
F. Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
G. The floor is lava - för varje steg man går ska man tappa 1 poäng.
H. Använd for-loopar för att skapa flera, sammanhängande väggar på kartan. Se till att det inte skapas några rum som man inte kan komma in i. Gör detta i filen grid.py.


Min projekt finns på GitHub: https://github.com/FLATPT/PhythonExam_amelia_U.git

