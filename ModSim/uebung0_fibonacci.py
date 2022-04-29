import csv
import matplotlib.pyplot as plt
import numpy as np

def save_my_data(Dateiname = "" , DatenListe = []): # wenn der User keine Parameter uebergibt, werden die Parameter aus der Klammer genommen
    with open(Dateiname, "w", newline='\n') as csvdatei:
        DataWriter = csv.writer(csvdatei, delimiter='\n', quotechar=" ", quoting= csv.QUOTE_NONNUMERIC)
        DataWriter.writerow(DatenListe)
        csvdatei.close()
        print("Daten gespeichert!")
def read_my_data(Dateiname = ''):
    with open(Dateiname, "r", newline='\n') as csvdatei:
        DataReader = csv.reader(csvdatei, delimiter='\n', quotechar=" ", quoting= csv.QUOTE_NONNUMERIC)
        Ausgabe = []
        for element in DataReader: # iterates over Datensaetze (lines)
            Ausgabe.append(float(element[0]))
    csvdatei.close()
    print("Daten gelesen!")
    return Ausgabe

def calculate_fib(index):
    a_0 = 1
    a_1 = 1
    fib_reihe = [a_0, a_1]
    if index >1:
        for i in range(2, index):
            fib_reihe.append( fib_reihe[-1] + fib_reihe[-2] ) #nimmt das letzte und das zweitletzte Element aus der Reihe

    return fib_reihe

def quotient(divisor, divident):
    quo = divisor / divident
    return quo

if __name__ == "__main__":
    # x_value = 0 #index
    # y_value = 0 #quotient bzw. goldener schnitt
    x_plot_data = []
    y_plot_data = []

    first_50_fib = calculate_fib(49)
    print("Die 50.Fibonacci Zahl ist: ", first_50_fib[48])

    fib_quo = [0] #der erste quotient wird auf 0 gesetzt
    for i in range(1,49):
        fib_quo.append(quotient(first_50_fib[i], first_50_fib[i-1]))
        #plot_data.append("{0}; {1}".format(i, fib_quo[-1])) zum speichern in einer csv datei
        x_plot_data.append('{0}'.format(i))
        y_plot_data.append('{0}'.format(fib_quo[-1]))

    save_my_data("GoldenerSchnittXdata.csv", x_plot_data)
    save_my_data("GoldenerSchnittYdata.csv", y_plot_data)

    fig1, ax1 = plt.subplots()

    x_plot_data = read_my_data("GoldenerSchnittXdata.csv")
    y_plot_data = read_my_data("GoldenerSchnittYdata.csv")
    ax1.plot(x_plot_data, y_plot_data)
    plt.xlabel('Index')
    plt.ylabel('Goldener Schnitt')
    plt.title("GoldenerSchnitt.csv")

    plt.show()





