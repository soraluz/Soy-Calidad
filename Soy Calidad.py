Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

# Elaborar un programa que muestre los diccionarios, y programar las siguientes acciones:
# [1] Agregar
# [2] Eliminar
# [3] Actualizar
# [4] Salir

opcion=1
num_articulos=4

while opcion!=4:
    print("========================================")
    print("Lista de Productos: ")
    print("========================================")
    for id,articulo in Productos.items():
        print(f"{id}\t {articulo}\t {Precios[id]} \t{Stock[id]}\n")
    print("========================================")
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
    opcion=int(input("Elija opción: "))
    print(opcion)
    if opcion==1:
        articulo=input("ingrese el articulo a agregar: ")
        precio=float(input("Ingrese el precio: "))
        stock=int(input("Ingrese su stock: "))
        num_articulos+=1

        Productos[num_articulos]= articulo
        Precios[num_articulos]= precio
        Stock[num_articulos]= stock
        
    elif opcion==2:
        articulo=int(input("Ingrese numero de articulo a eliminar: "))
        if articulo in Productos:
            del Productos[articulo]
        else:
            print("No se encuentra el numero del articulo\n")
            
    elif opcion==3:
        id=int(input("Ingrese el numero de articulo a modificar: "))
        if id in Productos:
            resp=input("Desea modificar el nombre del articulo (S/N): ")
            if resp.upper()=="S":
                articulo=input("Ingrese el nombre del articulo: ")
                Productos[id]=articulo
            else:
                print("Opcion inválida debe escribir S o N \n")
            resp=input("Desea modificar el precio del articulo (S/N): ")
            if resp.upper()=="S":
                precio=float(input("Ingrese el nuevo precio del articulo : "))
                Precios[id]=precio
            else:
                print("Opcion inválida debe escribir S o N \n")
            resp=input("Desea modificar el stock del articulo (S/N): ")
            if resp.upper()=="S":
                stock=int(input("Ingrese el nuevo stock del articulo: "))
                Stock[id]=stock
            else:
                print("Opcion inválida debe escribir S o N \n")
        else:
            print("No se encuentra el numero de articulo ingresado\n")
        
    elif opcion==4:
        print("Saliendo del sistema...")
    else:
        print("Elegiste una opción inválida")
        
