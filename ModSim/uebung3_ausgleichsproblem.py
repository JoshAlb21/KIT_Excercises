import numpy as np
import csv
import matplotlib.pyplot as plt

#TODO Tipp simpy

def getNumberOfPoints(plot_data):  # erscheint in Python unnoetig
    number = len(plot_data[0])
    return number

def read_my_data(Dateiname=''):  # analog zu readFile
    with open(Dateiname, "r", newline='\n') as csvdatei:
        DataReader = csv.reader(csvdatei, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        x = []
        y = []
        for element in DataReader:  # iterates over Datensaetze (lines)
            if element != "":
                x.append(float(element[1])) #element0 = "" (das erste Leerzeichen
                y.append(float(element[2]))

    csvdatei.close()
    print("Daten gelesen!")
    return x, y  # hier wird ein tupel aus listen zurueckgegeben

def f1(x_var): #TODO Externe Funktionen implementieren
    return x_var/(1+x_var)

def f2(x_var):
    return 1/(2+x_var)

if __name__ == "__main__":
    plot_data = read_my_data("input3.dat")
    N = getNumberOfPoints(plot_data)
    print(N, " Datentupel")

    #TODO Matrix A befuellen
    #es ist leichter die zeilen nach einem Scheme zu befuellen (deswegen erst mal transponierte)
    A_t = np.array([[f1(x) for x in plot_data[0]], [f2(x) for x in plot_data[0]]], dtype=float)
    A = A_t.transpose()
    #so nicht gdacht

    #TODO nach lambda 1 und 2 loesen
    y = np.array(plot_data[1])
    left_mat = np.matmul( A_t, A) #Matrixmultiplikation
    right_mat = np.matmul(A_t, y)
    lam = np.linalg.solve(left_mat, right_mat) #LGS solver in Matrix Form
    lam1 , lam2 = lam
    print("Lambda1: {0}, Lambda2: {1}".format(lam1,lam2))

    #TODO Daten plotten mit Funktion
    #ACHTUNG: Dieses Lambda hat nichts mit den Parametern Lambda1/2 zu tun! Das ist eine Funktion in python
    regress = lambda x_var : lam1 * f1(x_var) + lam2 * f2(x_var)

    fig1, ax1 = plt.subplots()

    # Diskretisierung
    x_var = np.arange(0, 101, 0.5)  # schrittweite 0.5
    dots_x = np.array(plot_data[0])

    ax1.plot(x_var, regress(x_var), 'k', dots_x, regress(dots_x), 'bo')
    plt.xlabel('x_Werte')
    plt.ylabel('y_Werte')
    plt.title("Regression von input3.dat")
    plt.xlim(0, 101)
    #plt.ylim(-9, 3.5)

    plt.show()


#TODO Anmerkung input wurde in input3 umbenannt (mehrere Projekte in einem Ordner)