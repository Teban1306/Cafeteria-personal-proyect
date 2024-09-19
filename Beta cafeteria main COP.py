import random

# Lista de productos y precios en COP
menu = {
    1: {'nombre': 'Café Americano', 'precio': 5000},
    2: {'nombre': 'Café con Leche', 'precio': 6000},
    3: {'nombre': 'Capuchino', 'precio': 7000},
    4: {'nombre': 'Té', 'precio': 4000},
    5: {'nombre': 'Sándwich', 'precio': 8000},
    6: {'nombre': 'Pastel', 'precio': 7500},
}

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú de la Cafetería ---")
    for clave, producto in menu.items():
        print(f"{clave}. {producto['nombre']} - ${producto['precio']:,} COP")
    print("----------------------------")

# Función para hacer un pedido
def hacer_pedido():
    pedido = []
    total = 0.0
    opcion = None  # Inicializar la opción

    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Selecciona el número del producto que deseas (o escribe '0' para finalizar el pedido): "))

        if opcion == 0:
            break
        elif opcion in menu:
            cantidad = int(input(f"¿Cuántas unidades de {menu[opcion]['nombre']} deseas? "))
            total_producto = menu[opcion]['precio'] * cantidad
            pedido.append({'producto': menu[opcion]['nombre'], 'cantidad': cantidad, 'total': total_producto})
            total += total_producto
            print(f"Agregaste {cantidad} de {menu[opcion]['nombre']} al pedido. Subtotal: ${total_producto:,.2f} COP")
        else:
            print("Opción no válida.")

    return pedido, total

# Función para procesar el pago
def procesar_pago(total):
    pago = float(input(f"\nTotal a pagar: ${total:,.2f} COP\nIngresa la cantidad con la que vas a pagar: $"))

    while pago < total:
        print("El monto es insuficiente, intenta de nuevo.")
        pago = float(input("Ingresa la cantidad con la que vas a pagar: $"))

    cambio = pago - total
    print(f"Pago exitoso. Tu cambio es: ${cambio:,.2f} COP")

# Función para generar un número de orden aleatorio
def generar_numero_orden():
    return random.randint(1000, 9999)

# Función principal
def main():
    print("¡Bienvenido a la Cafetería Virtual!\n")
    
    # Solicitar el nombre del cliente
    nombre_cliente = input("Por favor, ingresa tu nombre: ")

    # Generar número de orden
    numero_orden = generar_numero_orden()

    # Hacer el pedido
    pedido, total = hacer_pedido()

    if pedido:
        print(f"\nNúmero de orden: {numero_orden}")
        print(f"Nombre del cliente: {nombre_cliente}")
        print("\n--- Resumen del Pedido ---")
        for item in pedido:
            print(f"{item['cantidad']} x {item['producto']} - Total: ${item['total']:,} COP")
        print(f"Total del pedido: ${total:,.2f} COP")

        procesar_pago(total)
        print(f"\n¡Gracias por tu compra, {nombre_cliente}! Tu número de orden es {numero_orden}.")
    else:
        print("No realizaste ningún pedido.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
