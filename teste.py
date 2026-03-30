import math

# Funções básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: número negativo"
    return math.sqrt(a)

# Testando as funções
if __name__ == "__main__":
    x = 10
    y = 5

    print("Soma:", soma(x, y))
    print("Subtração:", subtracao(x, y))
    print("Multiplicação:", multiplicacao(x, y))
    print("Divisão:", divisao(x, y))
    print("Potência:", potencia(x, y))
    print("Raiz quadrada de x:", raiz_quadrada(x))
