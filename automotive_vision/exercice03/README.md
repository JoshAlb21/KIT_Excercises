# Feature Point Methods/SIFT

Es wird eine vereinfachte Version von SIFT implementiert, welche auf den beiden Schritten
1. Detection of Feature Points
2. Descriptor of Feature Points
beruht.

Die Methode verzichtet darauf eine präferierte Richtung aus der Richtungs-Histogramm zu extrahieren und hat lediglich eine Winkelnauflösung von 45°
wodurch ein Histogramm aus 8 bins besteht.

![Alt text](assets/extract_feature.jpg?raw=true "Detected Feature Points")
![Alt text](assets/match_feature.jpg?raw=true "Match Feature Points")
