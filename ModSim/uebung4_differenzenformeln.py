from math import sin, cos, pi
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from decimal import *

def f(x_var):
    return Decimal(cos(x_var))

def df(x_var):
    return Decimal(-sin(x_var))

def d_plus(x_0, h): #rechtsseitige
    return (f(x_0+Decimal(h)) - f(x_0)) / Decimal(h)

def d_minus(x_0, h): #linksseitige
    return (f(x_0) - f(x_0-Decimal(h))) / Decimal(h)

def d_zentral(x_0, h):
    return Decimal(1/2)* (f(x_0+Decimal(h)) - f(x_0-Decimal(h)))/ Decimal(h)

def safe_arange(start, stop, step): #brauchen wir nicht
    return step * np.arange(start / step, stop / step)


if __name__ == "__main__":

    #TODO GENAUIGKEIT EINSTELLEN
    getcontext().prec = 12

    x_0 = Decimal(1)
    h = Decimal(10**(-1)) #Startwert

    # TODO Ausgabe des Fehlers von D+, D- und D fuer verschiedene h
    f_d_plus = []
    f_d_minus = []
    f_d_zentral = []
    low_p, low_m, low_z = (1, 1, 1)
    h_opt_p,h_opt_m, h_opt_z = (1, 1, 1)

    #for i in np.logspace(2,9,num=9-2+1,base=10,dtype='int'): #Alternative
    for _ in range(1,11):
        fehler_d_plus = abs(df(x_0) - d_plus(x_0, h))
        fehler_d_minus = abs(df(x_0) - d_minus(x_0, h))
        fehler_d_zentral = abs(df(x_0) - d_zentral(x_0, h))

        print("h={3}: Fehler fuer: D+: {0}, D-: {1}, D: {2}".format(fehler_d_plus, fehler_d_minus, fehler_d_zentral, h))


        #optimales h speichern
        if fehler_d_plus <low_p:
            h_opt_p = h
            low_p = fehler_d_plus
        if fehler_d_minus <low_m:
            h_opt_m = h
            low_m = fehler_d_minus
        if fehler_d_zentral <low_z:
            h_opt_z = h
            low_z = fehler_d_zentral

        #update h
        h = h * Decimal(10**(-1))

    #optimales h ausgeben
    print("Das optimale h fuer plus:{0} minus:{1}, zentral:{2}".format(h_opt_p,h_opt_m, h_opt_z))

    #compute plot data
    h = Decimal(10 ** (-1))  # Startwert

    #for h in np.logspace(-1,-10,num=100,base=10, dtype='float'):
    for expo in range(-9, 0): #grenzen
        for i in range(1,2): #values per expo
            fehler_d_plus = abs(df(x_0) - d_plus(x_0, h))
            f_d_plus.append(fehler_d_plus)
            fehler_d_minus = abs(df(x_0) - d_minus(x_0, h))
            f_d_minus.append(fehler_d_minus)
            fehler_d_zentral = abs(df(x_0) - d_zentral(x_0, h))
            f_d_zentral.append(fehler_d_zentral)

            #print("h={3}: Fehler fuer: D+: {0}, D-: {1}, D: {2}".format(fehler_d_plus, fehler_d_minus, fehler_d_zentral, h))

            if fehler_d_plus < low_p:
                h_opt_p = h
                low_p = fehler_d_plus
            if fehler_d_minus < low_m:
                h_opt_m = h
                low_m = fehler_d_minus
            if fehler_d_zentral < low_z:
                h_opt_z = h
                low_z = fehler_d_zentral

            h = Decimal(10**expo * i)

    print("Das optimale h fuer plus:{0} minus:{1}, zentral:{2}".format(h_opt_p, h_opt_m, h_opt_z))

    #plotten
    fig1, ax1 = plt.subplots()
    # Diskretisierung

    h_schritt = np.logspace(-1, -10, num=9)

    f_d_p = np.array(f_d_plus)
    f_d_m = np.array(f_d_minus)
    f_d_z = np.array(f_d_zentral)
    print("laenge von f_p" ,len(f_d_p))

    ax1.plot(h_schritt, f_d_p , 'k' , color='tab:blue', label="D_plus ~h")
    ax1.plot(h_schritt, f_d_m, color='tab:orange', label="D_minus ~h")
    ax1.plot(h_schritt, f_d_z, color='tab:green', label="D_zentral ~h^2")
    plt.xlabel('h - Schrittweite')
    plt.ylabel('Fehler')
    plt.title("Fehler in Abhaengigkeit von h")
    #plt.ylim(10**(-9), 10**(-8))
    #plt.xlim(-0.025, 0.1)
    plt.legend()
    #matplotlib.scale.LogScale
    plt.xscale('log')
    plt.yscale('log')

    plt.show()

    #ANTWORT:
    """
    wenn man die Genauigkeit von float(7 Nachkommastellen) auf double(16 Nachkommast.) veraendert,
    dann ist der Rundungsfehler erst bei kleineren h groß! (macht Sinn, weil h ja genauer ist)
    ACHTUNG: in python gibt es keine unterscheidung zwischen float und double!
    deswegen muss man das Modul decimal einbinden, worueber man die Genauigkeit festlegen kann
    """