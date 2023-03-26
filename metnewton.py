def newton(f, x0, erro=0.0001, k=100):
  
    x = x0
    for i in range(k):
        fx = f(x)
        dfx = df(x)  # derivada
        if abs(fx) < erro:
            return x
        if dfx == 0:
            raise ValueError("Derivada zero. Impossível continuar.")
        x = x - fx / dfx 
    raise ValueError("Número máximo de iterações excedido.")

def f(x):
    return x**3 - x*9 + 3

def df(x):
    return 3*x**2 - 9

x0 = 0.5
raiz = newton(f, x0)
print(raiz)
