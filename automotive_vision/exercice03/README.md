# Feature Point Methods/SIFT

Es wird eine vereinfachte Version von SIFT implementiert, welche auf den beiden Schritten
1. Detection of Feature Points
2. Descriptor of Feature Points
beruht.

Die Methode verzichtet darauf eine präferierte Richtung aus der Richtungs-Histogramm zu extrahieren und hat lediglich eine Winkelnauflösung von 45°
wodurch ein Histogramm aus 8 bins besteht.

![Alt text](assets/extract_feature.jpg?raw=true "Detected Feature Points")
![Alt text](assets/match_feature.jpg?raw=true "Match Feature Points")

die roten Linien im 2. Bild verbinden Bild Punkte welche zusammen gematched wurden (indem die euklidische Distanz im Merkmalsraum berechnet wurde)
Das bedeutet das (mehr oder weniger) parallele Linien ein gutes Matching bedeutet. Teilweise gibt es offensichtliche Ausreißer (schräge Linien, also nicht Vertikal).
