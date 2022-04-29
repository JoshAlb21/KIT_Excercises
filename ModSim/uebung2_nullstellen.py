from math import cos, pi, exp #oder math komplett importieren
import matplotlib.pyplot as plt
import numpy as np


def f1(x):
    return x**3-2*x+2

def df1(x): #alternativ bibliothek dafuer implementieren
    return 3*x**2-2

def f2(x):
    return -x**2 + cos(x*pi)*exp(-8*x)

def df2(x, h = 0.1):
    #zentrale Differenzformel
    return 1/2* (f2(x+h) -f1(x-h) ) / h


def bisektion( func, x_a , x_b):

    #initilisierung
    x_1 = x_a
    x_2 = x_b
    f_1 = func(x_1)
    f_2 = func(x_2)
    delta = 10**(-12) #vorerst gewaehlt
    nullst = None #vorerst gewählt

    #iteration
    finished = False
    while(not finished):
        x_3 = 1/2*(x_1+ x_2) #Bestimme Intervallmitte
        f_3 = func(x_3)

        if f_2*f_3 < 0: #NS zwischen x2 und x3
            x_1 = x_3
            f_1 = f_3
        else: #NS zwischen x1 und x2
            x_2 = x_3
            f_2 = f_3

        #Abbruchbedingung
        if abs(x_2 - x_1) <= delta:
            finished = True
            nullst = x_3

    return nullst

def sekanten( func, x_0, x_1):
    #init
    x_n_min_1 = x_0
    x_n = x_1
    delta = 10**(-12)
    nullst = None

    #iteration
    finished = False
    while (not finished):

        #Sekantenformel
        x_n_plus_1 = x_n_min_1 - func(x_n_min_1) *  (x_n - x_n_min_1)/(func(x_n)-func(x_n_min_1))

        #Abbruchbedingung
        if abs(x_n_plus_1 - x_n) < delta: #TODO nochmal gucken, wieso falsche NS
            finished = True
            nullst = x_n_plus_1
        else:
            x_n_min_1 = x_n
            x_n = x_n_plus_1


    return nullst

def newton(func, dfdx, x_0):

    #init
    x_n = x_0
    delta = 10 ** (-12)
    nullst = None

    #iteration
    finished = False
    count = 0
    while (not finished and count != 200):
        # Newton-Formel
        x_n_plus_1 = x_n - func(x_n) / dfdx(x_n)

        if abs(x_n_plus_1 - x_n) < delta:
            finished = True
            nullst = x_n_plus_1
            print("NewtonVerfahren hat: ",count, " Iterationschritte gebraucht") #TODO das selbe fuer sekanten verfahre und bisektion machen
        else:
            x_n = x_n_plus_1
        count += 1

    return nullst


if __name__ == '__main__':

    #MIT f1
    print("Bisektion")
    result = bisektion(f1 , -3.0, -0.5)
    print("Nulstellen Bisektion: ", result)

    print("Sekanten")
    result = sekanten(f1, -3.0, -0.5)
    print("Nullstellen Sekanten: ", result)

    print("Newton")
    result = newton(f1, df1, -0.5)
    print("Nullstelle Newton: ", result)

    #MIT f2
    print("----------------f2-------------------")
    print("Bisektion")
    result = bisektion(f2, 0, 1)
    print("Nulstellen Bisektion: ", result)

    print("Sekanten")
    result = sekanten(f2, 0, 1)
    print("Nullstellen Sekanten: ", result)

    print("Newton")
    result = newton(f2, df2, 1)
    print("Nullstelle Newton: ", result)

    #TODO Zusatz: Funktionen Plotten
    fig1, ax1 = plt.subplots()

    x_var = np.arange(-5, 5, 0.1)  # schrittweite 0.1
    ax1.plot(x_var, f1(x_var), 'k')
    plt.xlabel('x_Werte')
    plt.ylabel('y_Werte')
    plt.title("Funktion f1")
    plt.xlim(-5, 5)
    plt.ylim(-4, 4)
    plt.grid()
    plt.show()
