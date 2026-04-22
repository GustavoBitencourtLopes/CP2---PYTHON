a = float(input("Digite quanto vale o primeiro lado: "))
b = float(input("Digite quanto vale o segundo lado: "))
c = float(input("Digite quanto vale o terceiro lado: "))

# Ordenando manualmente (A será o maior)
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

# Verifica se forma triângulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    # Classificação por ângulo
    if a * a == b * b + c * c:
        print("TRIANGULO RETANGULO")
    elif a * a > b * b + c * c:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    # Classificação por lados
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")