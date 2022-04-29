import csv
import matplotlib.pyplot as plt
import numpy as np
import copy #um eine deepcopy von unserem array zu machen

def raeuber(time, x_vec): #linke seite dgl 1.Ordnung x_1
    alpha, beta = -1.2, 0.03
    return (alpha + beta * x_vec[1]) * x_vec[0] #rechte seite der dgl

def beute(time, x_vec): #TODO wofuer wird die time uebergeben?
    gamma, delta = 0.34, -0.03
    return (gamma + delta * x_vec[0]) * x_vec[1]

def runge_kutta2(time, dt, x_vec, fa, fb):

    x_temp = [0, 0]

    x_temp[0] = x_vec[0] + 0.5* dt * fa(time, x_vec) # hier stimmt das 0.5 nicht
    x_temp[1] = x_vec[1] + 0.5* dt * fb(time, x_vec)

    x_vec[0] += dt * fa(time + 0.5 * dt, x_temp) #hier fehlt das 0.5
    x_vec[1] += dt * fb(time + 0.5 * dt, x_temp)

    return x_vec

def runge_kutta4(time, dt, x_vec, fa, fb):

    FR1 = fa(time, x_vec)
    FR2 = fa(time + 0.5 *dt, [x_vec[0]+0.5*dt*FR1, x_vec[1]+0.5*dt*FR1])
    FR3 = fa(time + 0.5 *dt, [x_vec[0]+0.5*dt*FR2, x_vec[1]+0.5*dt*FR2])
    FR4 = fa(time+dt, [x_vec[0] + dt *FR3, x_vec[1] + dt *FR3])

    FB1 = fb(time, x_vec)
    FB2 = fb(time + 0.5 * dt, [x_vec[0] + 0.5 * dt * FB1, x_vec[1] + 0.5 * dt * FB1])
    FB3 = fb(time + 0.5 * dt, [x_vec[0] + 0.5 * dt * FB2, x_vec[1] + 0.5 * dt * FB2])
    FB4 = fb(time + dt, [x_vec[0] + dt * FR3, x_vec[1] + dt * FB3])

    x_temp = copy.deepcopy(x_vec)
    x_vec[0] = x_temp[0] + dt/6.0 * (FR1 + 2*FR2 + 2*FR3+ FR4)
    x_vec[1] = x_temp[1] + dt / 6.0 * (FB1 + 2 * FB2 + 2 * FB3 + FB4)

    return x_vec

def euler(time, dt, y_vec, fa, fb):

    y_temp = copy.deepcopy(y_vec)
    y_vec[0] = y_temp[0] + dt * fa(time, y_temp)
    y_vec[1] = y_temp[1] + dt * fb(time, y_temp)

    return y_vec

def solve(dt, t_ende, x_start, raeuber, beute, verfahren, filename):

    t= 0

    #save start values
    x_vec = copy.deepcopy(x_start)
    data = []

    with open(filename, "w", newline='\n') as csvdatei:
        DataWriter = csv.writer(csvdatei, delimiter='\n', quotechar=" ", quoting=csv.QUOTE_NONNUMERIC)
        data.append("{0};{1};{2}".format(x_start[0], x_start[1], t)) #erste Zeile

        while(t < t_ende):

            t += dt
            x_vec = verfahren(t, dt, x_vec, raeuber, beute) #TODO welches x?
            x_1 = x_vec[0]
            x_2 = x_vec[1]

            data.append("{0};{1};{2}".format(x_1, x_2, t))



        print(len(data))
        data_100 = [data[i] for i in range(0, len(data), 100)] #jeder 100.wert abspeichern
        DataWriter.writerow(data_100)
        print(data_100)

    print("Daten gespeichert!")

def read_my_data(Dateiname=''):  # analog zu readFile
    with open(Dateiname, "r", newline='\n') as csvdatei:
        DataReader = csv.reader(csvdatei, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        x1 = []
        x2 = []
        t = []
        for element in DataReader:  # iterates over Datensaetze (lines)
            x1.append(float(element[0]))
            x2.append(float(element[1]))
            t.append(float(element[2]))

    print("Daten gelesen!")
    return x1, x2, t  # hier wird ein tupel aus listen zurueckgegeben




if __name__ == "__main__":

    t_ende = 1000
    x_start = [30, 80] #Raueber , Beute 30 80

    # TODO Einstellmoeglichkei
    #Runge Kutta 2.Ordnung
    #solve(0.1, t_ende, x_start, raeuber, beute, runge_kutta2, "RK2_dt01.dat")
    #solve(0.01, t_ende, x_start, raeuber, beute, runge_kutta2, "RK2_dt001.dat")
    solve(0.001, t_ende, x_start, raeuber, beute, runge_kutta2, "RK2_dt0001.dat")

    #Euler
    #solve(0.1, t_ende, x_start, raeuber, beute, euler, "E2_dt01.dat")
    #solve(0.01, t_ende, x_start, raeuber, beute, euler, "E2_dt001.dat")
    #solve(0.001, t_ende, x_start, raeuber, beute, euler, "E2_dt0001.dat")

    # Runge Kutta 4.Ordnung
    #solve(0.1, t_ende, x_start, raeuber, beute, runge_kutta4, "RK4_dt01.dat")
    #solve(0.01, t_ende, x_start, raeuber, beute, runge_kutta4, "RK4_dt001.dat")
    #solve(0.001, t_ende, x_start, raeuber, beute, runge_kutta4, "RK4_dt0001.dat")

    #PLOTTEN
    fig1, ax1 = plt.subplots()

    #daten einlesen
    #dat_name = "RK2_dt01.dat" #TODO Einstellmoeglichkeit
    #dat_name = "RK2_dt001.dat"
    dat_name = "RK2_dt0001.dat" #Ellipse/Kreis wird immer glatter

    #dat_name = "E2_dt01.dat" #Was passiert hier?
    #dat_name = "E2_dt001.dat" #leichte Verbesserung
    #dat_name = "E2_dt0001.dat" # aehnlich zu RK Verfahren

    #dat_name = "RK4_dt01.dat" #geringe Aufloesung
    #dat_name = "RK4_dt001.dat" #aufschwingendes Verhalten (stark) , nicht so glatt wie RK2
    #dat_name = "RK4_dt0001.dat" #aufschwingendes Verhalten (leicht) #ähnlich zu RK2

    #TODO AUFGABE 5
    #TODO Vergleich Runge Kutta Verfahren fuer 100 000 t_ende
    #t_ende = 100000
    #solve(0.01, t_ende, x_start, raeuber, beute, runge_kutta2, "RK2_dt001.dat") #ANTWORT RK2 ist viel glatter
    #solve(0.01, t_ende, x_start, raeuber, beute, runge_kutta4, "RK4_dt001.dat")

    # TODO PLOTTEN
    plot_data = read_my_data(dat_name)
    x_1_val = np.array(plot_data[0])
    x_2_val = np.array(plot_data[1])
    time_val = np.array(plot_data[2])


    #PLOT raeber vs beute
    ax1.plot(x_1_val, x_2_val, 'k') # time_val, x_2_val, 'bo') #TODO Einstellmoeglichkeit

    #PLOT raeuber vs time and beute vs time
    #ax1.plot(time_val, x_1_val,'b-', time_val, x_2_val, 'r-')

    plt.xlabel('Raeuber')
    plt.ylabel('Beute')
    plt.title("Raeuber/Beute Modell")
    #plt.xlim(0, 101)
    #plt.ylim(-9, 3.5)

    plt.show()

    # RK2 01 Problem, dass sich Schwingung aufschwingt! Problem des Lösungsverfahren