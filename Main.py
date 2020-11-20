import tkinter
from tkinter import *
import math

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

import numpy

root = Tk()
root.title("Coon's patch")

root.geometry("600x250")
root.configure(background='blue')

x1_s = Entry(root, width=20, bg='white')
x1_s.grid(row=0, column=1, padx=(10, 0))

OneW_label = Label(root, text="Enter 1W:", width=10, background='blue', anchor='e')
OneW_label.grid(row=0, column=0, padx=(10, 0), sticky='e')

Array1_label = Label(root, text="Enter Array", width=10, background='blue', anchor='w')
Array1_label.grid(row=0, column=2, padx=(10, 0),)
Array2_label = Label(root, text="Enter Array", width=10, background='blue', anchor='w')
Array2_label.grid(row=1, column=2, padx=(10, 0),)
Array3_label = Label(root, text="Enter Array", width=10, background='blue', anchor='w')
Array3_label.grid(row=2, column=2, padx=(10, 0),)
Array4_label = Label(root, text="Enter Array", width=10, background='blue', anchor='w')
Array4_label.grid(row=3, column=2, padx=(10, 0),)

y1_s = Entry(root, width=20, bg='white')
y1_s.grid(row=0, column=3, padx=(10, 0))

ZeroW_label = Label(root, text="Enter 0W:", width=20, background='blue', anchor='e')
ZeroW_label.grid(row=1, column=0, padx=(10, 0), sticky='e')

x2_s = Entry(root, width=20, bg='white')
x2_s.grid(row=1, column=1, padx=(10, 0))

y2_s = Entry(root, width=20, bg='white')
y2_s.grid(row=1, column=3, padx=(10, 0))

x3_s = Entry(root, width=20, bg='white')
x3_s.grid(row=2, column=3, padx=(10, 0))

y3_s = Entry(root, width=20, bg='white')
y3_s.grid(row=2, column=1, padx=(10, 0))

x4_s = Entry(root, width=20, bg='white')
x4_s.grid(row=3, column=3, padx=(10, 0))

y4_s = Entry(root, width=20, bg='white')
y4_s.grid(row=3, column=1, padx=(10, 0))

UZero_label = Label(root, text="Enter U0: ", width=25, background='blue', anchor='e')
UZero_label.grid(row=2, column=0, padx=(10, 0))

UOne_label = Label(root, text="Enter U1: ", width=25, background='blue', anchor='e')
UOne_label.grid(row=3, column=0, padx=(10, 0))
def func1(yn_s,xn_s):
    lengthn = len(str(yn_s.get()).split(' '))
    yn = str(yn_s.get()).split(' ')
    X00 = []
    Y00 = []
    Z00 = []
    for i in range(lengthn):
        X00.append(float(xn_s.get()))
        Y00.append(float(yn[i]))
        Z00.append(0.0)
    for i in range(len(X00)):
        Z00[i] = ((1 - X00[i]) * Y00[i])
    Xn = []
    Yn = []
    Zn = []

    Xn.append(X00[0])
    Yn.append(Y00[0])
    Zn.append(Z00[0])

    for i in range(len(X00) - 1):
        Xn[-1] = X00[i]
        Yn[-1] = Y00[i]
        Zn[-1] = Z00[i]
        beg_x = (X00[i] - X00[i + 1]) / 1000
        beg_y = (Y00[i] - Y00[i + 1]) / 1000
        beg_z = (Z00[i] - Z00[i + 1]) / 1000
        for j in range(1000):
            X00[i] -= beg_x
            Y00[i] -= beg_y
            Z00[i] -= beg_z
            Xn.append(X00[i])
            Yn.append(Y00[i])
            Zn.append(Z00[i])
    return Xn,Yn,Zn
def func2(yn_s,xn_s):
    lengthn = len(str(xn_s.get()).split(' '))
    yn = str(xn_s.get()).split(' ')

    X00 = []
    Y00 = []
    Z00 = []

    for i in range(lengthn):
        X00.append(float(yn[i]))
        Y00.append(float(yn_s.get()))
        Z00.append(0.0)

    for i in range(len(X00)):
        Z00[i] = ((1 - X00[i]) * Y00[i])

    Xn = []
    Yn = []
    Zn = []

    Xn.append(X00[0])
    Yn.append(Y00[0])
    Zn.append(Z00[0])

    for i in range(len(X00) - 1):
        Xn[-1] = X00[i]
        Yn[-1] = Y00[i]
        Zn[-1] = Z00[i]
        beg_x = (X00[i] - X00[i + 1]) / 1000
        beg_y = (Y00[i] - Y00[i + 1]) / 1000
        beg_z = (Z00[i] - Z00[i + 1]) / 1000
        for j in range(1000):
            X00[i] -= beg_x
            Y00[i] -= beg_y
            Z00[i] -= beg_z
            Xn.append(X00[i])
            Yn.append(Y00[i])
            Zn.append(Z00[i])
    return Xn,Yn,Zn
def Go():


    fig = plt.figure()
    ax = plt.axes(projection="3d")

    W_1,Y1,Z1 = func1(y1_s,x1_s)
    W_0,Y2,Z2 = func1(y2_s,x2_s)
    U_0,Y3,Z3 = func2(y3_s,x3_s)
    U_1,Y4,Z4 = func2(y4_s,x4_s)
    ax.plot(W_1, Y1, Z1, 'g')
    ax.plot(W_0, Y2, Z2, 'g')
    ax.plot(U_0, Y3, Z3, 'g')
    ax.plot(U_1, Y4, Z4, 'g')

    coef_X = abs(W_1[0] - W_0[0])

    step = coef_X * 0.1
    counter = 1 / 10
    Xs = U_1[0] + step
    Xs2 = U_0[0] + step
    while Xs < W_1[-1]:

        uarr = numpy.array([1 - counter, counter, 1])

        line_x = []
        line_y = []
        line_z = []
        counter_y = 1 / 1000

        coef_y = abs(Y2[-1] - Y2[0])
        step_w = 0.001 * coef_y
        Ys0 = Y2[0]
        Ys0 += step_w

        Ys1 = Y1[0]
        Ys1 += step_w

        for i in range(999):
            warr = numpy.array([[1 - counter_y], [counter_y], [1]])

            matrix_z = numpy.array([[-((1 - W_0[0]) * Y2[0]), -((1 - W_0[0]) * Y2[-1]), (1 - W_0[0]) * Ys0],
                                    [-((1 - W_1[0]) * Y1[0]), -((1 - W_1[0]) * Y1[-1]), (1 - W_1[-1]) * Ys1],
                                    [(1 - Xs2) * Y2[0], (1 - Xs) * Y1[-1], 0]])

            matrix_x = numpy.array([[-W_0[0], -W_0[0], W_0[0]], [-W_1[0], -W_1[0], W_1[0]],
                                    [Xs2, Xs, 0]])

            matrix_y = numpy.array(
                [[-Y2[0], -Y2[-1], Ys0], [-Y1[0], -Y1[-1], Ys1],
                 [Y3[0], Y4[-1], 0]])

            answer_x = numpy.dot(numpy.dot(uarr, matrix_x), warr)
            answer_y = numpy.dot(numpy.dot(uarr, matrix_y), warr)
            answer_z = numpy.dot(numpy.dot(uarr, matrix_z), warr)

            line_x.append(answer_x[-1])
            line_y.append(answer_y[-1])
            line_z.append(answer_z[-1])
            counter_y += 1 / 1000
            Ys0 += step_w
            Ys1 += step_w

        Xs += step
        Xs2 += step
        counter += 1 / 10

        ax.plot(line_x, line_y, line_z, "b")


    coef_y = abs(Y2[-1] - Y2[0])
    step_y = 0.1 * coef_y
    Ys0 = Y2[0]
    Ys0 += step_y

    Ys1 = Y1[0]
    Ys1 += step_y

    counter = 1 / 10

    while Ys0 < Y1[-2]:
        counter_x = 1 / 1000

        warr = numpy.array([[1 - counter], [counter], [1]])
        line_x = []
        line_y = []
        line_z = []

        coef_X = abs(W_1[0] - W_0[0])

        step_x = coef_X * 0.001
        Xs = U_1[0] + step_x
        Xs2 = U_0[0] + step_x

        for i in range(999):
            uarr = numpy.array([1 - counter_x, counter_x, 1])


            matrix_z = numpy.array([[-((1 - W_0[0]) * Y2[0]), -((1 - W_0[0]) * Y2[-1]), (1 - W_0[0]) * Ys0],
                                    [-((1 - W_1[0]) * Y1[0]), -((1 - W_1[0]) * Y1[-1]), (1 - W_1[-1]) * Ys1],
                                    [(1 - Xs2) * Y2[0], (1 - Xs) * Y1[-1], 0]])

            matrix_x = numpy.array([[-W_0[0], -W_0[0], W_0[0]], [-W_1[0], -W_1[0], W_1[0]],
                                    [Xs2, Xs, 0]])

            matrix_y = numpy.array(
                [[-Y2[0], -Y2[-1], Ys0], [-Y1[0], -Y1[-1], Ys1],
                 [Y3[0], Y4[-1], 0]])

            answer_x = numpy.dot(numpy.dot(uarr, matrix_x), warr)
            answer_y = numpy.dot(numpy.dot(uarr, matrix_y), warr)
            answer_z = numpy.dot(numpy.dot(uarr, matrix_z), warr)

            line_x.append(answer_x[-1])
            line_y.append(answer_y[-1])
            line_z.append(answer_z[-1])
            counter_x += 1 / 1000
            Xs += step_x
            Xs2 += step_x

        Ys0 += step_y
        Ys1 += step_y

        ax.plot(line_x, line_y, line_z, "m")




    cube_definition = [
        (int(x1_s.get()), int(y4_s.get()), min(Z1[-1],Z2[-1],Z3[-1],Z4[-1])),
        (int(x1_s.get()), min(Y1[-1],Y2[-1],Y3[-1],Y4[-1]), min(Z1[-1],Z2[-1],Z3[-1],Z4[-1])),
        (int(x1_s.get()), int(y4_s.get()), max(Z1[-1],Z2[-1],Z3[-1],Z4[-1])),
        (min(W_0[-1],W_1[-1],U_0[-1],U_1[-1]), int(y4_s.get()), min(Z1[-1],Z2[-1],Z3[-1],Z4[-1]))]

    cube_definition_array = [
        numpy.array(list(item))
        for item in cube_definition
    ]

    points = []
    points += cube_definition_array
    vectors = [
        cube_definition_array[1] - cube_definition_array[0],
        cube_definition_array[2] - cube_definition_array[0],
        cube_definition_array[3] - cube_definition_array[0]
    ]

    points += [cube_definition_array[0] + vectors[0] + vectors[1]]
    points += [cube_definition_array[0] + vectors[0] + vectors[2]]
    points += [cube_definition_array[0] + vectors[1] + vectors[2]]
    points += [cube_definition_array[0] + vectors[0] + vectors[1] + vectors[2]]

    points = numpy.array(points)

    edges = [
        [points[0], points[3], points[5], points[1]],
        [points[1], points[5], points[7], points[4]],
        [points[4], points[2], points[6], points[7]],
        [points[2], points[6], points[3], points[0]],
        [points[0], points[2], points[4], points[1]],
        [points[3], points[6], points[7], points[5]]
    ]


    faces = Poly3DCollection(edges, linewidths=0.3, edgecolors='r')
    faces.set_facecolor((0, 0, 1, 0.1))

    ax.add_collection3d(faces)

    # Plot the points themselves to force the scaling of the axes
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=0)









    plt.show()



calculate_button = Button(root, text="confirm", command=Go, fg="black", width=10,background="pink")
calculate_button.grid(row=4, column=1, padx=(80, 0),columnspan=2)

root.mainloop()

