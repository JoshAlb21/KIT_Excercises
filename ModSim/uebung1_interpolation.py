import csv
import numpy as np
import matplotlib.pyplot as plt


def save_my_data(Dateiname="",
                 DatenListe=[]):  # wenn der User keine Parameter uebergibt, werden die Parameter aus der Klammer genommen
    with open(Dateiname, "w", newline='\n') as csvdatei:
        DataWriter = csv.writer(csvdatei, delimiter='\n', quotechar=" ", quoting=csv.QUOTE_NONNUMERIC)
        DataWriter.writerow(DatenListe)
        csvdatei.close()
        print("Daten gespeichert!")


def read_my_data(Dateiname=''):  # analog zu readFile
    with open(Dateiname, "r", newline='\n') as csvdatei:
        DataReader = csv.reader(csvdatei, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        x = []
        y = []
        for element in DataReader:  # iterates over Datensaetze (lines)
            x.append(float(element[0]))
            y.append(float(element[1]))

    csvdatei.close()
    print("Daten gelesen!")
    return x, y  # hier wird ein tupel aus listen zurueckgegeben


def getNumberOfPoints(plot_data):  # erscheint in Python unnoetig
    number = len(plot_data[0])
    return number


def newton_algo(D, x, y):
    D[0][0] = y[0]  # a_0

    # row und spalte sollen mit dem Skript uebereinstimmen
    for zeile in range(2, N + 1):  # letztes element nicht mitgezeahlt
        high_index = zeile  # fuer row 2 z.b. D21
        low_index = 1  # in jedem fall 1 außer fuer a0
        row_finished = False

        # erste spalte entspricht y Werten
        D[zeile - 1][0] = y[zeile - 1]

        for spalte in range(2, N + 1):
            print("calculate zeile{0} und spalte{1}".format(zeile, spalte))

            if zeile == spalte and row_finished == False:  # fuer die Diagonal eintraege
                # formel fuer einen Eintrag wie D321
                D[zeile - 1][spalte - 1] = (D[zeile - 1][spalte - 2] - D[zeile - 2][spalte - 2]) / (x[zeile - 1] - x[0])
                row_finished = True
            elif spalte == 2 and row_finished == False:  # fuer die 2 Spalte
                D[zeile - 1][spalte - 1] = (y[zeile - 1] - y[zeile - 2]) / (x[zeile - 1] - x[zeile - 2])
            elif spalte > 2 and row_finished == False:  # fuer alle spalten groesser 2
                D[zeile - 1][spalte - 1] = (D[zeile - 1][spalte - 2] - D[zeile - 2][spalte - 2]) / (
                        x[zeile - 1] - x[zeile - spalte])

    return D


def p(x_var , N):
    if N ==5:
        value = a[0] + a[1] * (x_var - x[0]) + a[2] * (x_var - x[0]) * (x_var - x[1]) + a[3] * (x_var - x[0]) * (
                    x_var - x[1]) * (x_var - x[2]) + a[4] * (x_var - x[0]) * (x_var - x[1]) * (x_var - x[2]) * (
                    x_var - x[3])
        pass
    elif N ==6:
        value = a[0] + a[1] * (x_var - x[0]) + a[2] * (x_var - x[0]) * (x_var - x[1]) + a[3] * (x_var - x[0]) * (
                x_var - x[1]) * (x_var - x[2]) + a[4] * (x_var - x[0]) * (x_var - x[1]) * (x_var - x[2]) * (
                        x_var - x[3]) + a[5] * (x_var - x[0]) * (x_var - x[1]) * (x_var - x[2]) * (
                        x_var - x[3]) * (x_var - x[4])

    return value



if __name__ == "__main__":  # ist nicht zwingend notwendig bei Python

    # VORBEREITUNG: werte aus input.dat speichern als .csv datei
    # in Projekt Ordner kopieren, wo die .py datei liegt

    # TODO loeschen, war nur zum erstellen der csv datei
    """
    #plot_data = read_my_data("input.txt")
    x_values = [1.0, 2.5 ,3.4 , 4.0, 4.5]
    y_values = [1.1, -0.5, 2.0, -1.0, 1.1]
    x_and_y = []
    for i in range(0,len(x_values)):
        x_and_y.append("{0}; {1}".format(x_values[i],y_values[i]))
    save_my_data("input.csv", x_and_y)
    """

    # einlesen der Daten
    plot_data = read_my_data("input.csv")
    N = getNumberOfPoints(plot_data)

    # Vektor erstellen
    x = plot_data[0]
    y = plot_data[1]
    # TODO kommentare weg machen

    # Matrix der Groeße NxN
    # M = np.ones((N+1, N+1)) # erst mal nur mit 1 gefuellt
    D = np.diag([1.0, 1.0, 1.0, 1.0, 1.0])
    print(D)

    # TODO: Berechne dividierte Differenzen (Newton Algorithmus)
    calc_D = newton_algo(D, x, y)

    # TODO: Gebe Matrix aus
    print("Matrix D: \n", calc_D)

    # TODO: Koeffizientenvektor erstellen (mit Diagonaleintraegen)
    a = np.array(calc_D.diagonal())
    print("Vektor a: \n", a)

    # TODO: Interpolationspolynom p(x) mit 5 Koeffizienten
    # das variable x heißt hier x_var
    # p = a[0]+a[1]*(x_var-x[0])+a[2]*(x_var-x[0])*(x_var-x[1])+a[3]*(x_var-x[0])*(x_var-x[1])*(x_var-x[2])+a[4]*(x_var-x[0])*(x_var-x[1])*(x_var-x[2])*(x_var-x[3])
    # python Funktion p(x) gibt mathematische Funktion p(x) zum plotten zurück

    # TODO: Polynom plotten
    fig1, ax1 = plt.subplots()

    # Diskretisierung
    x_var = np.arange(0, 5, 0.1) #schrittweite 0.1
    dots = np.array(x)

    ax1.plot(x_var, p(x_var, N) , 'k', dots, p(dots, N), 'bo')
    plt.xlabel('x_Werte')
    plt.ylabel('y_Werte')
    plt.title("Interpolation von input.csv")
    plt.xlim(0 , 5)
    plt.ylim(-9 , 3.5)

    plt.draw() #zeigt plot und programm lauft weiter

    # TODO: punkt (2.1, -1.4) hinzufügen

    # erstellt neue csv datei mit namen input2

    x_values = [1.0, 2.1, 2.5 ,3.4 , 4.0, 4.5]
    y_values = [1.1, -1.4, -0.5, 2.0, -1.0, 1.1]
    x_and_y = []
    for i in range(0,len(x_values)):
        x_and_y.append("{0}; {1}".format(x_values[i],y_values[i]))
    save_my_data("input2.csv", x_and_y)

    # einlesen der Daten
    plot_data = read_my_data("input2.csv")
    N = getNumberOfPoints(plot_data)
    # Vektor erstellen
    x = plot_data[0]
    y = plot_data[1]
    # Matrix der Groeße NxN
    D = np.diag([1.0]*N)
    print(D)

    # TODO: Berechne dividierte Differenzen (Newton Algorithmus)
    calc_D = newton_algo(D, x, y)

    # TODO: Gebe Matrix aus
    print("Matrix D: \n", calc_D)

    # TODO: Koeffizientenvektor erstellen (mit Diagonaleintraegen)
    a = np.array(calc_D.diagonal())
    print("Vektor a: \n", a)

    # TODO: Polynom plotten
    fig2, ax2 = plt.subplots()

    # Diskretisierung
    x_var = np.arange(0, 5, 0.1)  # schrittweite 0.1
    dots = np.array(x)

    ax2.plot(x_var, p(x_var, N), 'k', dots, p(dots, N), 'bo')
    plt.xlabel('x_Werte')
    plt.ylabel('y_Werte')
    plt.title("Interpolation von input2.csv")
    plt.xlim(0, 5)
    plt.ylim(-9, 3.5)

    plt.show()


