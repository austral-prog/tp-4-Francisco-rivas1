def line():
    A=float(input("Ingrese el coeficiente A: "))
    B=float(input("Ingrese el coeficiente B: "))
    x1=float(input("Ingrese el coeficiente X1: "))
    x2=float(input("Ingrese el coeficiente X2: "))
    print("El coeficiente A de su ecuación de la recta es:",A)
    print("El coeficiente B de su ecuación de la recta es:",B)
    print("El coeficiente X1 de su ecuación de la recta es:",x1)
    print("El coeficiente X2 de su ecuación de la recta es:" ,x2)
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {A}X + {B}")
    y1=A*x1+B
    y2=A*x2+B
    print("")
    print(f"""Dados los siguientes puntos:
	P1 ({x1}, {y1})
	P2 ({x2}, {y2})""")
    if x1==x2:
        cateto1=0
    else: 
        if x1<0:
            x1=x1*-1
        if x2<0:
            x2=x2*-1
        cateto1=x1+x2

    if y1==y2:
        cateto2=0
    else:
        if y1<0:
            y1=y1*-1
        if y2<0:
            y2=y2*-1
        cateto2=y1+y2
    
    distancia=((cateto1**2) + (cateto2**2))**(1/2)
    print("")
    print("La distancia entre ellos es:",distancia)

