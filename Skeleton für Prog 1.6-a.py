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
i = lambda p: prior(p)*scipy.misc.comb ( n, k )*p**k*(1-p)**(n-k)
j = lambda p: i(p) / scipy.integrate.quad ( i, 0, 1 ) 
print(type(i))
print(type(scipy.integrate.quad ( i, 0, 1 ))) 
plt.plot ( y, x, label="polynom"  ) 
## Teile das Intervall (a,b) in n "bins"
x = numpy.linspace ( 0, 1, n )
y = []
for t in range (0, len(x)):
  y.append(j(x[t]))
## Plotten, siehe https://matplotlib.org/
from matplotlib import pyplot as plt

## Plotte y versus x, als Linie, mit Label "label1"
plt.plot ( y, x, label="polynom"  ) 


plt.title ( "titel" )

## Beschriftung der x-Achse
plt.xlabel("x axis")

## Legende
plt.legend()

## Speichere in Bilddatei (pdf, png, ... )
plt.savefig ( "dummy-a.pdf" )
