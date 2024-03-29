def secante(f, x0, x1, erro=0.0001, k=100):

    for i in range(k):
        fx0 = f(x0)
        fx1 = f(x1)
        dfx = (fx1 - fx0) / (x1 - x0)
        x = x1 - fx1 / dfx
        if abs(x - x1) < erro:
            return x
        x0, x1 = x1, x
    raise ValueError("Número máximo de iterações excedido.")
def f(x):
    return x**3 -9*x + 3

x0 = 1
x1 = 2
raiz = secante(f, x0, x1)
print(raiz)
