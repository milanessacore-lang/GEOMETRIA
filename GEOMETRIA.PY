
def hacer_circulo():
    print("haciendo un circulo")
def hacer_cuadrado():
    print("haciendo cuadrado")
def hacer_triangulo():
    print("haciendo un triangulo")
def menu():
    print("menu de figuras geometricas")
    print("1, circulo")
    print("2 cuarado")
    print("3, triangulo")
    print("4, salir")

while True:
    menu()
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