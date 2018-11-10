#!/usr/bin/env python3

""" Skeleton file, das eure Lernkurve beschleunigen soll,
    fuer Uebung 1.6.  
"""

## Importieren der wichtigsten Module fuer die Uebungsaufgabe.
import numpy, scipy.misc, math, scipy.integrate

## scipy.misc.comb ( n, k )  ## n ueber k = n! / ( k! (n-k)! )
## math.sin ( math.pi * x ) ## sin ( pi * x )

## lambda Funktionen erlauben Definitionen in einer einzigen Zeile
prior = lambda p: p**2 * ( 1 - p )**3  ## prior(.5) = .03125
n=1000
k=343
## Integral von f ueber das Intervall (a,b)
u = lambda p: math.sin(math.pi*p)**2
print(type(u))
##v = lambda p: u(p) / 
print(type(scipy.integrate.quad ( u, 0, 1 ) ))

## Teile das Intervall (a,b) in n "bins"
x = numpy.linspace ( 0, 1, n )
w = []
##for s in range (0, len(x)):
##  w.append(v(x[s]))
## Plotten, siehe https://matplotlib.org/
from matplotlib import pyplot as plt

## Plotte y versus x, als Linie, mit Label "label1"
##plt.plot ( w, x, label="trigonometric"  ) 


plt.title ( "titel" )

## Beschriftung der x-Achse
plt.xlabel("x axis")

## Legende
plt.legend()

## Speichere in Bilddatei (pdf, png, ... )
plt.savefig ( "dummy-b.pdf" )
