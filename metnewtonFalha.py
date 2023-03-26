"""
Observações: 
- O valor da precisão deve ser inserido na forma decimal
- A função deve ser inserida de modo que a biblioteca math entenda:
  potencia: x**(expotente)
  log: math.log10(x)
  multiplicação: *
"""
import math
from sympy import *
import numpy as np

#input função
fun = input("f(x) = ")

#input critério de parada
erro1 = float(input("\nDigite o valor da primeira precisao desejada: "))
erro2 = float(input("\nDigite o valor da segunda precisao desejada: "))

#input valor inicial
valor0 = float(input("\nDigite o valor inicial de x: "))

#resolve a função
def f(val):
  funval = eval(fun.replace('x', 'val'))
  return funval


#derivada
def der(f):
  x = Symbol('x')
  return diff(f, x)
d = der(fun)


#result der
def dx(float val):
  derVal = eval(d.replace('x', 'val'))
  return derVal


#metodo de newton
if abs(f(valor0)) < erro1:
    print(f"\nO valor mais próximo da raiz tal que |f(x)|< e1 é f({valor0:.4f})={f(valor0):.7f}.")
else:
  k=0
  #func iteração

  fx = f(valor0)
  d = dx(valor0)
  x = valor0 - (fx / d)

  while math.fabs(f(x)) > erro1 or math.fabs(x - valor0) > erro2:
    valor0 = x
    fx = f(valor0)
    d = dx(valor0)
    x = valor0 - (fx / d)

    k=k+1

  print(f"\nO valor mais próximo da raiz tal que |f(x)|< e1 ou |b-a|< e2 é f({x:.4f})={f(x):.7f}, com ",k," iterações.")
