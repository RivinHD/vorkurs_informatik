import numpy as np
import math

#"C:\Program Files\Microsoft Office\Root\Office16\ONENOTE.EXE" /hyperlink onenote:https://technischeunivers049-my.sharepoint.com/personal/vincent_gerlach_uni-jena_de/Documents/Vorkurs%20Informatik/Analysis.one#Analisis&section-id={3B63203D-0269-4FA7-B69C-E1AA137D589A}&page-id={03D3B974-50E3-4F0A-98F5-44CE01AE22A4}&end

print(sum((v-1)**2 for v in range(2, 14+1))+sum(2*(w+3) for w in range(-2, 8+1))+sum(1 for k in range(10, 31+1)))


def difference_quotient(f, x, e):
    return (f(x + e) - f(x)) / e

def func_f(x):
    return x**3 + 7 /(math.cos((math.pi * x / 5)))

print(difference_quotient(func_f, 10, 0.0000000000001))

def area(func, start, stop, step):
    return sum([abs(func(x)) * step for x in np.arange(start, stop + step, step)])

def func_s(x):
    return x**2 + 4 + x**3

print(area(func_s, -2, 0, 0.000001))
