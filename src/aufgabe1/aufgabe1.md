# Aufgabe 1
a) (7,2), (7,4), (7,5), (7,6), (7,3), (7,1), (8,3), (8,1), (4,3), (1,2), (4,1) => Parität = 11 -> ungerade
# Aufgabe 2

a) `h(n) ≤ c(n,n‘) + h(n‘)` -> Die Heuristik ist monoton, wenn die Kosten einer Aktion + die Heuristik nach der Aktion
größer-gleich der Heuristik vor der Aktion sind.

h1 verringert sich maximal um 1 pro Aktion und da die Kosten für eine Aktion
immer 1 sind, muss `h(n) ≤ 1 + h(n')`.

b) h2 verringert sich ebenfall maximal um 1, da wir nach der Manhattan-Distanz
Steine pro Aktion immer nur um 1 in ihre Zielrichtung bewegen können. Da alle Aktionen Kosten von
1 haben, gilt für h2 also auch: `h2(n) ≤ 1 + h2(n')`.

c) `h1(n) ≤ h2(n)` -> Wenn z.B. ein Stein an der falschen Position steht, ist sowohl h1 = 1, als auch h2 >= 1. Dabei
kann h2 nie kleiner sein als h1.
Bei h2 lässt sich die "Qualität" des Zuges besser sehen. Es ist besser sichtbar, ob der Zug einen positiven Effekt
hatte, also näher an das Ziel gekommen ist oder nicht. (Feingranularer)

# Aufgabe 3
d) Ja, weil A* den kürzesten Weg findet

Bei einer monotonen Heuristik
haben die von A* expandierten Knoten
monoton steigende f-Werte.
Damit ist für jeden expandierten
Knoten n der gefundene Pfad nach
n auch optimal.

e) Vermutlich ein enormer Speicherverbrauch und lange Laufzeit, da exponentiell wachsend.