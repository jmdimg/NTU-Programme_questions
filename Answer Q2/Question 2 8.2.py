# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12aaP9V0RoqIVKyWqFce651wddeZZofq3
"""

t0 = 0;S = 10;E = 1; ES =0; P = 0; t = 2 ;h = 0.1


def derivative_of_ES(t, ES):
    return 100*S*E-(150+600)*ES

def rungeKutta_ES(t0, ES0, t, h):
    n = (int)((t - t0)/h)
    ES = ES0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * derivative_of_ES(t0, ES)
        k2 = h * derivative_of_ES(t0 + 0.5 * h, ES + 0.5 * k1)
        k3 = h * derivative_of_ES(t0 + 0.5 * h, ES + 0.5 * k2)
        k4 = h * derivative_of_ES(t0 + h, ES + k3)
 
        # Update next value of S
        ES = ES + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
 
        # Update next value of t0
        t0 = t0 + h
    return ES

print('The value of ES at t is:', rungeKutta_ES(t0, ES, t, h))
ES = rungeKutta_ES(t0, ES, t, h)

def derivative_of_S(t, S):
    return 600*ES-100*S*E

def derivative_of_E(t, E):
    return 600*ES+150*ES-100*S*E

def derivative_of_P(t, P):
    return 150*ES

def rungeKutta_S(t0, S0, t, h):
    n = (int)((t - t0)/h)
    S = S0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * derivative_of_S(t0, S)
        k2 = h * derivative_of_S(t0 + 0.5 * h, S + 0.5 * k1)
        k3 = h * derivative_of_S(t0 + 0.5 * h, S + 0.5 * k2)
        k4 = h * derivative_of_S(t0 + h, S + k3)
 
        # Update next value of S
        S = S + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
 
        # Update next value of t0
        t0 = t0 + h
    return S

def rungeKutta_E(t0, E0, t, h):
    n = (int)((t - t0)/h)
    E = E0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * derivative_of_E(t0, E)
        k2 = h * derivative_of_E(t0 + 0.5 * h, E + 0.5 * k1)
        k3 = h * derivative_of_E(t0 + 0.5 * h, E + 0.5 * k2)
        k4 = h * derivative_of_E(t0 + h, E + k3)
 
        # Update next value of S
        E = E + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
 
        # Update next value of t0
        t0 = t0 + h
    return E
def rungeKutta_P(t0, P0, t, h):
    n = (int)((t - t0)/h)
    P = P0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * derivative_of_P(t0, P)
        k2 = h * derivative_of_P(t0 + 0.5 * h, P + 0.5 * k1)
        k3 = h * derivative_of_P(t0 + 0.5 * h, P + 0.5 * k2)
        k4 = h * derivative_of_P(t0 + h, P + k3)
 
        # Update next value of S
        P = P + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
 
        # Update next value of t0
        t0 = t0 + h
    return P

print ('The value of S at t is:', rungeKutta_S(t0, S, t, h))
print ('The value of E at t is:', rungeKutta_E(t0, E, t, h))
print ('The value of P at t is:', rungeKutta_P(t0, P, t, h))

