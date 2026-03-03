
while True:
    print("este es el menu para hacer figuras geometricas")
    print("1 circulo")
    print("2 cuadrado")
    print("3 triangulo")
    print("4 salir")
    opcion=int(input("seleccione una firgura    \n"))
    match opcion:
        case 1:
            print("vas a hacer un circulo")
        case 2:
            print("vas a hacer un cuadrado")
        case 3:
            print("vas a hacer un triangulo")
        case 4:
            break
    #pola