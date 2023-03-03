"""
Observações: 
- O valor da precisão deve ser inserido na forma decimal
- A função deve ser inserida de modo que a biblioteca math entenda:
  potencia: x**(expotente)
  log: math.log10(x)
  multiplicação: *
"""

import math

#input a 
#input b
print("Digite o valor do intevalo [a,b]:\n")
a = float(input("a: "))
b = float(input("b: "))

#input erro
erro = float(input("\nDigite o valor da precisao desejada: "))
1

#input função
fun = input("f(x) = ")

def f(val):
  funval = eval(fun.replace('x', 'val'))
  return funval

#compara os sinais dos valores
def compara(val1, val2):
  if val1 * val2 == 0:
    return 0
  elif val1 * val2 < 0:
    return -1
  else:
    return 1

#metodo da bisseccao
if compara(f(a), f(b)) > 0:
  print("Não há raíz neste intervalo.")

else:
  k=0
  while math.fabs(b-a) > erro:
    #novo intervalo
    ni = (a+b)/2

    if f(ni) == 0:
      print(f"A raíz é f({ni:.4f})=0")
      break
    
    elif compara(f(a), f(ni)) < 0:
      b = ni

    else:
      a = ni
    k=k+1
  print(f"\nO valor mais próximo da raiz tal que |b-a|< e é f({ni:.4f})={f(ni):.7f}\nNo intervalo [{a:.4f},{b:.4f}], com ",k," iterações.")
