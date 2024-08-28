def line():
    import math
    cofa = float(input("Ingrese el coeficiente A: ")) #2.3
    cofb = float(input("Ingrese el coeficiente B: ")) #-4
    cofx1 = float(input("Ingrese el coeficiente X1: ")) #50
    cofx2 = float(input("Ingrese el coeficiente X2: ")) #-32.9
    cofy1 = (cofa*cofx1) + cofb
    cofy2 = (cofa*cofx2) + cofb
    dist = math.sqrt((cofx2 - cofx1)**(2) +(cofy2 - cofy1)**(2))
    print(f"El coeficiente A de su ecuación de la recta es: {cofa}")
    print(f"El coeficiente B de su ecuación de la recta es: {cofb}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {cofx1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {cofx2}")
    print(f"""\nPara la siguiente ecuación:\n\tY = {cofa}X + {cofb}""")
    print(f"""\nDados los siguientes puntos:
\tP1 ({cofx1}, {cofy1})
\tP2 ({cofx2}, {cofy2})""")
    print(f"\nLa distancia entre ellos es: {dist}")
