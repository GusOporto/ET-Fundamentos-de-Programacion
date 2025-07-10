#DICCIONARIOS
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

#FUNCIONES
#stock por marca
def stock_marca(marca):
    stock_m=0
    for clave,valor in productos.items():
        if valor[0].lower()==marca.lower():
            stock_m+=stock[clave][1]
    
    print(f"El Stock total de la marca {marca.upper()} es {stock_m}")

#busqueda por rango de precio
def busqueda_precio(p_min, p_max):
    lista_precio=[]
    for clave,valor in stock.items():
        if valor[1]>0:
            if p_min<=valor[0] and p_max>=valor[0]:
                lista_precio.append(f"{productos[clave][0]}--{clave}")
                
    lista_precio.sort()
    if len(lista_precio)==0:
        print("No hay notebooks en ese rango de precios.")
    else:
        print(lista_precio)

#actualizar precio
def actualizar_precio(modelo, p):
    if modelo  in stock:
        stock[modelo][0]=p
        return True
    else:
        return False

#MENÚ
def main():
    while True:
        try:

            print("*** MENU PRINCIPAL ***")
            print("1. Stock marca.")
            print("2. Búsqueda por precio.")
            print("3. Actualizar precio.")
            print("4. Salir.")

            opc=int(input("Elija una opción: "))

            if opc==1:
                print("- Stock Marca -")
                marca=input("Ingrese la marca que desea buscar: ")
                
                stock_marca(marca)

            elif opc==2:
                while True:
                    try:
                        print("- Busqueda por Precio -")
                        p_min=int(input("Ingrese el precio mínimo a buscar: "))
                        p_max=int(input("Ingrese el precio máximo a buscar: "))

                        busqueda_precio(p_min, p_max)
                        break

                    except ValueError:
                        print("Debe ingresar valores enteros!!")
            
            elif opc==3:
                while True:
                    print("- Actualizar Precio -")
                    modelo=input("Ingrese el modelo que desea actualizar: ")
                    p=int(input("Ingrese el nuevo precio del producto: "))

                    actualizar_precio(modelo, p)

                    if actualizar_precio(modelo,p)==False:
                        print("El modelo no existe!!")
                    elif actualizar_precio(modelo,p)==True:
                        print("Precio actualizado!!")

                    repetir=input("¿Desea actualizar otro precio? (si/no): ")
                    if repetir.lower()=="no":
                        break
                    elif repetir.lower()!="si":
                        print("Respuesta no valida.")
                        break
            
            elif opc==4:
                print("Programa finalizado.")

            else:
                raise ValueError
            
        except ValueError:
            print("Debe seleccionar una opción válida!!")

if __name__=="__main__":
    main()