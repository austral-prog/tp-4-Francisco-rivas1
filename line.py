def line():
    a=float(input("Ingrese el coeficiente A: "))
    b=float(input("Ingrese el coeficiente B: "))
    c=float(input("Ingrese el coeficiente X1: "))
    d=float(input("Ingrese el coeficiente X2: "))
    print("El coeficiente A de su ecuación de la recta es:",a)
    print("El coeficiente B de su ecuación de la recta es:",b)
    print("El coeficiente X1 de su ecuación de la recta es:",c)
    print("El coeficiente X2 de su ecuación de la recta es:" ,d)
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {a}X + {b}")
    y1=a*c+b
    y2=a*d+b
    print("")
    print(f"""Dados los siguientes puntos:
	P1 ({c}, {y1})
	P2 ({d}, {y2})""")
    if c<0:
        c=c*-1
    if d<0:
        d=d*-1
    if y1<0:
        y1=y1*-1
    if y2<0:
        y2=y2*-1
    cateto1=c+d
    cateto2=y1+y2
    distancia=((cateto1**2) + (cateto2**2))**(1/2)
    print("")
    print("La distancia entre ellos es:",distancia)
