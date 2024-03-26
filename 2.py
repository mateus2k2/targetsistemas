# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def quadrado_perfeito(n):
    return n == int(n ** 0.5) ** 2

def check_fibonacci(n):
    return quadrado_perfeito(5 * n ** 2 + 4) or quadrado_perfeito(5 * n ** 2 - 4)

def main():
    n = int(input("Digite um número: "))
    if check_fibonacci(n):
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

main()