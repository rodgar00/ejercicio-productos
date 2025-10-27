from tienda import Product

lista = []

continuar = True
while continuar:
    try:
        print(f"1. Añadir al carrito\n2. Ver carrito\n3. Comprobar si los productos del carrito están activos\n4. Salir")
        opcion = int(input(">> "))
        if opcion == 1:
            producto = input("Introduce tu producto -> ")
            precio = (input("Introduce tu precio -> "))
            producto_completo = Product(producto, precio)
            lista.append(producto_completo)

        elif opcion == 2:
            if lista is not None:
                for item in lista:
                    print(item)
            else:
                print("No hay nada en el carrito")

        elif opcion == 3:
            if lista:
                for producto in lista:
                    print(producto, producto.isActive)
            else:
                print("No hay nada que comprobar")
        else:
            continuar = False

    except ValueError as e:
            print(f"Error: {e}")
