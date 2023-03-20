"""
Observações: 
- O valor da precisão deve ser inserido na forma decimal
- A função deve ser inserida de modo que a biblioteca math entenda:
  potencia: x**(expotente)
  log: math.log10(x)
  multiplicação: *
"""
import math

#input função
fun = input("f(x) = ")

#input função iteração
funIt = input("g(x) = ")

#input critério de parada
erro1 = float(input("\nDigite o valor da primeira precisao desejada: "))
erro2 = float(input("\nDigite o valor da segunda precisao desejada: "))

#input valor inicial
valor0 = float(input("\nDigite o valor inicial de x: "))

#resolve a função
def f(val):
  funval = eval(fun.replace('x', 'val'))
  return funval

def g(val):
  funItval = eval(funIt.replace('x', 'val'))
  return funItval

#metodo do ponto fixo
if abs(f(valor0)) < erro1:
    print(f"\nO valor mais próximo da raiz tal que |f(x)|< e1 é f({valor0:.4f})={f(valor0):.7f}.")
else:
  k=0
  xAnt = valor0
  x = g(xAnt)

  while math.fabs(f(x)) > erro1 or math.fabs(x - xAnt) > erro2:
    xAnt = x
    x = g(xAnt)
    k=k+1

  print(f"\nO valor mais próximo da raiz tal que |f(x)|< e1 ou |b-a|< e2 é f({x:.4f})={f(x):.7f}, com ",k," iterações.")
